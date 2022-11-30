from __future__ import annotations

from fontTools.ttLib import TTFont


def read_unicodes(font_path: str):
    """
    Read the supported Unicode codepoints from a font.
    """
    font = TTFont(font_path)
    cmap = font.getBestCmap()
    return list(cmap.keys())


def format_unicode_range(font_path):
    """
    Return the unicode-range CSS property for the font-face rule.
    """
    ranges = []
    r = []
    for c in read_unicodes(font_path):
        if r:
            if c - 1 == r[-1]:
                r.append(c)
            else:
                ranges.append(r)
                r = [c]
        else:
            r = [c]
    if r:
        ranges.append(r)
    ur = []
    for r in ranges:
        if len(r) == 1:
            ur.append(f"U+{r[0]:04X}")
        else:
            u0 = min(r)
            u1 = max(r)
            ur.append(f"U+{u0:04X}-{u1:04X}")
    return "unicode-range: " + ", ".join(ur) + ";"
