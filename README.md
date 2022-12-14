# css-unicode-range

`css-unicode-range` is a command line utility that outputs the `unicode-range`
CSS property for a specific webfont file, which can then be used in an
`@font-face` rule.

## Usage

```
usage: css-unicode-range [-h] font

Analyse the supported Unicode codepoints of a webfont and output the unicode-range CSS property.

positional arguments:
  font        The path to the webfont to be analysed

options:
  -h, --help  show this help message and exit
```

### Example

Command line input:

```
css-unicode-range TheSansC5-4_SemiLight.woff2
```

Output:

```
unicode-range: U+0000, U+000D, U+0020-007E, U+00A0-017F, U+018F, U+0192,
U+01A0-01A1, U+01AF-01B0, U+01CD-01DC, U+01E6-01E9, U+01FA-01FF, U+0218-021B,
U+0237, U+0259, U+0298, U+02BC, U+02C6-02C7, U+02C9, U+02D8-02DD, U+0300-0301,
U+0303, U+0307, U+0309, U+0312, U+0315, U+0323, U+0326-0327, U+0394, U+03A9,
U+03BC, U+03C0, U+0E3F, U+1E02-1E03, U+1E06-1E07, U+1E0A-1E0F, U+1E1E-1E21,
U+1E24-1E25, U+1E32-1E39, U+1E40-1E47, U+1E56-1E57, U+1E5A-1E5D, U+1E60-1E63,
U+1E6A-1E6F, U+1E7E-1E85, U+1E92-1E95, U+1E9E, U+1EA0-1EF9, U+2000-200F,
U+2012-2015, U+2017-201E, U+2020-2022, U+2024-2026, U+2030, U+2032-2033,
U+2039-203A, U+203C-203E, U+2044, U+2070, U+2074-208E, U+20A0-20BD, U+2103,
U+2105, U+2109, U+2113, U+2116-2117, U+2120, U+2122, U+2126, U+212E,
U+2153-215F, U+2190-2199, U+219E-21AA, U+21D0-21D9, U+21DD, U+21E6-21E9, U+21F3,
U+2202, U+2205-2206, U+220F, U+2211-2212, U+2215, U+2219-221C, U+221E-221F,
U+2229, U+222B, U+2236, U+2245, U+2248, U+2260-2261, U+2264-2265, U+2297,
U+22A0, U+22C5-22C6, U+22EE, U+2300, U+2302, U+2310, U+2320-2321, U+2349,
U+23AF, U+23D0, U+2500-25A1, U+25AA-25AC, U+25AE, U+25B2-25B3, U+25B6, U+25B8,
U+25BA, U+25BC, U+25C0, U+25C2, U+25C4, U+25C6, U+25CA-25CB, U+25CF,
U+25D8-25D9, U+25E6, U+25FC, U+2605, U+2610-2612, U+261C, U+261E, U+262E-2637,
U+263A-263C, U+2640-2642, U+2660, U+2663, U+2665-2666, U+266A-266B,
U+2680-2685, U+26A2-26A7, U+2713, U+2717, U+2764, U+27F0-27FF, U+2906-2907,
U+E020-E022, U+E040-E04B, U+F6C1-F6C2, U+F6DD-F6DE, U+F8E5-F8E6, U+F8FF,
U+FB00-FB06;
```

Complete `@font-face` rule:

```css
@font-face {
     font-family: "TheSansC5";
     src: url("TheSansC5-4_SemiLight.woff2") format("woff2");
     font-weight: 400;
     font-style: normal;
     unicode-range: U+0000, U+000D, U+0020-007E, U+00A0-017F, U+018F, U+0192, U+01A0-01A1, U+01AF-01B0, U+01CD-01DC, U+01E6-01E9, U+01FA-01FF, U+0218-021B, U+0237, U+0259, U+0298, U+02BC, U+02C6-02C7, U+02C9, U+02D8-02DD, U+0300-0301, U+0303, U+0307, U+0309, U+0312, U+0315, U+0323, U+0326-0327, U+0394, U+03A9, U+03BC, U+03C0, U+0E3F, U+1E02-1E03, U+1E06-1E07, U+1E0A-1E0F, U+1E1E-1E21, U+1E24-1E25, U+1E32-1E39, U+1E40-1E47, U+1E56-1E57, U+1E5A-1E5D, U+1E60-1E63, U+1E6A-1E6F, U+1E7E-1E85, U+1E92-1E95, U+1E9E, U+1EA0-1EF9, U+2000-200F, U+2012-2015, U+2017-201E, U+2020-2022, U+2024-2026, U+2030, U+2032-2033, U+2039-203A, U+203C-203E, U+2044, U+2070, U+2074-208E, U+20A0-20BD, U+2103, U+2105, U+2109, U+2113, U+2116-2117, U+2120, U+2122, U+2126, U+212E, U+2153-215F, U+2190-2199, U+219E-21AA, U+21D0-21D9, U+21DD, U+21E6-21E9, U+21F3, U+2202, U+2205-2206, U+220F, U+2211-2212, U+2215, U+2219-221C, U+221E-221F, U+2229, U+222B, U+2236, U+2245, U+2248, U+2260-2261, U+2264-2265, U+2297, U+22A0, U+22C5-22C6, U+22EE, U+2300, U+2302, U+2310, U+2320-2321, U+2349, U+23AF, U+23D0, U+2500-25A1, U+25AA-25AC, U+25AE, U+25B2-25B3, U+25B6, U+25B8, U+25BA, U+25BC, U+25C0, U+25C2, U+25C4, U+25C6, U+25CA-25CB, U+25CF, U+25D8-25D9, U+25E6, U+25FC, U+2605, U+2610-2612, U+261C, U+261E, U+262E-2637, U+263A-263C, U+2640-2642, U+2660, U+2663, U+2665-2666, U+266A-266B, U+2680-2685, U+26A2-26A7, U+2713, U+2717, U+2764, U+27F0-27FF, U+2906-2907, U+E020-E022, U+E040-E04B, U+F6C1-F6C2, U+F6DD-F6DE, U+F8E5-F8E6, U+F8FF, U+FB00-FB06;
}
```

## Copyright

?? 2022 by [LucasFonts GmbH](https://www.lucasfonts.com/), Berlin. Licensed under the MIT license.

_TheSans_ is a trademark of LucasFonts.
