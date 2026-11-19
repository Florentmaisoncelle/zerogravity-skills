#!/usr/bin/env python3
"""Contrôles déterministes d'une miniature YouTube : marges de sécurité et retouche ciblée.

Deux commandes :
  final  : le fichier a la bonne taille et chaque marque critique respecte les marges
           et la zone du chronomètre (coin bas droit).
  edit   : une retouche n'a rien changé en dehors de la zone déclarée modifiable.

Dépendance : Pillow. Aucun accès réseau.
"""

from __future__ import annotations

import argparse
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Iterable, List, Sequence, Tuple

from PIL import Image, ImageChops, ImageDraw

FORMATS_ACCEPTES = ("PNG", "JPEG", "WEBP")


@dataclass(frozen=True)
class Box:
    label: str
    x1: int
    y1: int
    x2: int
    y2: int

    @property
    def width(self) -> int:
        return self.x2 - self.x1 + 1

    @property
    def height(self) -> int:
        return self.y2 - self.y1 + 1

    def intersects(self, other: "Box") -> bool:
        return not (
            self.x2 < other.x1
            or self.x1 > other.x2
            or self.y2 < other.y1
            or self.y1 > other.y2
        )


def _box_errors(box: Box, width: int, height: int) -> List[str]:
    errors: List[str] = []
    if box.x1 < 0 or box.y1 < 0 or box.x2 >= width or box.y2 >= height:
        errors.append(f"{box.label} : la boîte sort de l'image ({box})")
    if box.x2 < box.x1 or box.y2 < box.y1:
        errors.append(f"{box.label} : coordonnées inversées ({box})")
    return errors


def validate_final(
    image_path: Path,
    expected_size: Tuple[int, int],
    safe_boxes: Sequence[Box],
    min_horizontal_margin: int,
    min_vertical_margin: int,
    timestamp_safe_size: Tuple[int, int],
) -> List[str]:
    errors: List[str] = []
    if not image_path.is_file():
        return [f"Image introuvable : {image_path}"]

    try:
        with Image.open(image_path, formats=FORMATS_ACCEPTES) as image:
            width, height = image.size
    except (OSError, Image.DecompressionBombError) as exc:
        return [
            f"Image invalide ou format non pris en charge ({image_path}) : {exc}. "
            "Utiliser PNG, JPEG ou WebP."
        ]

    if (width, height) != expected_size:
        errors.append(
            f"Taille inattendue pour {image_path.name} : {(width, height)} au lieu de {expected_size}"
        )

    if min_horizontal_margin < 0 or min_vertical_margin < 0:
        errors.append("Les marges doivent être positives ou nulles")

    timestamp_width, timestamp_height = timestamp_safe_size
    if timestamp_width <= 0 or timestamp_height <= 0:
        errors.append("La zone du chronomètre doit avoir des dimensions positives")
    elif timestamp_width > width or timestamp_height > height:
        errors.append("La zone du chronomètre doit tenir dans l'image")
    if errors:
        return errors

    timestamp_box = Box(
        "chronomètre YouTube",
        width - timestamp_width,
        height - timestamp_height,
        width - 1,
        height - 1,
    )

    for box in safe_boxes:
        box_errors = _box_errors(box, width, height)
        errors.extend(box_errors)
        if box_errors:
            continue
        horizontal_margin = min(box.x1, width - 1 - box.x2)
        vertical_margin = min(box.y1, height - 1 - box.y2)
        if horizontal_margin < min_horizontal_margin:
            errors.append(
                f"{box.label} : marge horizontale de {horizontal_margin}px, "
                f"{min_horizontal_margin}px exigés"
            )
        if vertical_margin < min_vertical_margin:
            errors.append(
                f"{box.label} : marge verticale de {vertical_margin}px, "
                f"{min_vertical_margin}px exigés"
            )
        if box.intersects(timestamp_box):
            errors.append(f"{box.label} : empiète sur la zone du chronomètre")

    return errors


def validate_edit(
    before_path: Path,
    after_path: Path,
    allowed_box: Box,
    pixel_threshold: int,
    max_outside_change: float,
) -> List[str]:
    errors: List[str] = []
    if not before_path.is_file():
        errors.append(f"Image d'avant introuvable : {before_path}")
    if not after_path.is_file():
        errors.append(f"Image d'après introuvable : {after_path}")
    if errors:
        return errors

    if isinstance(pixel_threshold, bool) or not 0 <= pixel_threshold <= 255:
        errors.append("Le seuil de pixel doit être compris entre 0 et 255")
    if isinstance(max_outside_change, bool) or not 0 <= max_outside_change <= 1:
        errors.append("La part de changement tolérée hors zone doit être comprise entre 0 et 1")
    if errors:
        return errors

    try:
        with Image.open(before_path, formats=FORMATS_ACCEPTES) as before_image:
            before = before_image.convert("RGBA")
        with Image.open(after_path, formats=FORMATS_ACCEPTES) as after_image:
            after = after_image.convert("RGBA")
    except (OSError, Image.DecompressionBombError) as exc:
        return [f"Image de retouche invalide ou format non pris en charge : {exc}. Utiliser PNG, JPEG ou WebP."]

    if before.size != after.size:
        return [f"La retouche a changé la taille de l'image : {before.size} -> {after.size}"]

    width, height = before.size
    box_errors = _box_errors(allowed_box, width, height)
    if box_errors:
        return box_errors

    diff = ImageChops.difference(before, after)
    ImageDraw.Draw(diff).rectangle(
        (allowed_box.x1, allowed_box.y1, allowed_box.x2, allowed_box.y2),
        fill=(0, 0, 0, 0),
    )

    channel_masks = [
        channel.point(lambda value: 255 if value > pixel_threshold else 0)
        for channel in diff.split()
    ]
    changed_mask = channel_masks[0]
    for channel_mask in channel_masks[1:]:
        changed_mask = ImageChops.lighter(changed_mask, channel_mask)
    changed_pixels = changed_mask.histogram()[255]
    outside_pixels = width * height - allowed_box.width * allowed_box.height
    changed_fraction = changed_pixels / max(1, outside_pixels)

    if changed_fraction > max_outside_change:
        errors.append(
            f"La retouche a changé {changed_pixels} pixels hors de {allowed_box.label} "
            f"({changed_fraction:.6%}) ; maximum toléré {max_outside_change:.6%}"
        )

    return errors


def parse_box(value: str) -> Box:
    try:
        label, coordinates = value.split(":", 1)
        x1, y1, x2, y2 = (int(part) for part in coordinates.split(","))
    except (ValueError, TypeError) as exc:
        raise argparse.ArgumentTypeError("la boîte s'écrit nom:x1,y1,x2,y2") from exc
    return Box(label=label, x1=x1, y1=y1, x2=x2, y2=y2)


def _print_result(errors: Iterable[str]) -> int:
    errors = list(errors)
    if errors:
        for error in errors:
            print(f"ECHEC {error}")
        return 1
    print("OK")
    return 0


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Contrôle une miniature finale (marges) ou une retouche ciblée."
    )
    subparsers = parser.add_subparsers(dest="command", required=True)

    final_parser = subparsers.add_parser("final", help="contrôler une miniature finale")
    final_parser.add_argument("--image", type=Path, required=True)
    final_parser.add_argument("--expected-width", type=int, default=1280)
    final_parser.add_argument("--expected-height", type=int, default=720)
    final_parser.add_argument("--safe-box", type=parse_box, action="append", default=[])
    final_parser.add_argument("--min-horizontal-margin", type=int, default=64)
    final_parser.add_argument("--min-vertical-margin", type=int, default=36)
    final_parser.add_argument("--timestamp-safe-width", type=int, default=154)
    final_parser.add_argument("--timestamp-safe-height", type=int, default=72)

    edit_parser = subparsers.add_parser("edit", help="contrôler une retouche ciblée")
    edit_parser.add_argument("--before", type=Path, required=True)
    edit_parser.add_argument("--after", type=Path, required=True)
    edit_parser.add_argument("--allowed-box", type=parse_box, required=True)
    edit_parser.add_argument("--pixel-threshold", type=int, default=8)
    edit_parser.add_argument("--max-outside-change", type=float, default=0.001)

    return parser


def main(argv: Sequence[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    if args.command == "final":
        return _print_result(
            validate_final(
                args.image,
                expected_size=(args.expected_width, args.expected_height),
                safe_boxes=args.safe_box,
                min_horizontal_margin=args.min_horizontal_margin,
                min_vertical_margin=args.min_vertical_margin,
                timestamp_safe_size=(args.timestamp_safe_width, args.timestamp_safe_height),
            )
        )
    return _print_result(
        validate_edit(
            args.before,
            args.after,
            allowed_box=args.allowed_box,
            pixel_threshold=args.pixel_threshold,
            max_outside_change=args.max_outside_change,
        )
    )


if __name__ == "__main__":
    sys.exit(main())
