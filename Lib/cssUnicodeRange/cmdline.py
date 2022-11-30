from __future__ import annotations

import argparse

from cssUnicodeRange import format_unicode_range
from pathlib import Path


def css_unicode_range():
    parser = argparse.ArgumentParser(
        description=(
            "Analyse the supported Unicode codepoints of a webfont and output "
            "the unicode-range CSS property."
        )
    )
    parser.add_argument(
        "font",
        type=str,
        nargs=1,
        help="The path to the webfont to be analysed",
    )
    args = parser.parse_args()
    if args:
        font_path = args.font[0]
        if Path(font_path).exists():
            print(format_unicode_range(font_path))
        else:
            print(f"File not found: {font_path}")
    else:
        parser.print_help()
