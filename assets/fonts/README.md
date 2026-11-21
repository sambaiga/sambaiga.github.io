# Fonts

Jost and Libre Franklin as variable fonts, and JetBrains Mono in regular and bold (all Latin subsets), self-hosted so that no page requests a font from a third
party. Both are licensed under the SIL Open Font License 1.1 (https://openfontlicense.org). They were downloaded from
Google Fonts; the `@font-face` rules are in `assets/scss/_fonts.scss`.

`newcm-math.woff2` is New Computer Modern Math (the face that the books use for equations), subset to Latin, Greek,
mathematical symbols and mathematical alphanumerics, with its OpenType MATH table kept. It is licensed under the GUST
Font License (https://www.gust.org.pl/projects/e-foundry/licenses). The source is `NewCMMath-Regular.otf` from CTAN
(`fonts/newcomputermodern`); the subset is made with `pyftsubset --flavor=woff2`. The rule that applies it is in
`assets/scss/_fonts.scss`.
