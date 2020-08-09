# Flexible_Resume

A flexible resume with configurable options. The output can be easily changed with a few switches to match different requirements.

This resume is based on [https://github.com/sb2nov/resume](https://github.com/sb2nov/resume).

## Building PDF

To build docker image:

```
docker build -t latex .
```

To build PDFs with default configurations:

```
docker run --rm -i --user=`id -u`:`id -g` -v "$PWD":/data latex bash ./GenerateAll.sh
```

To build a PDF with `Config.tex`:

```
docker run --rm -i --user=`id -u`:`id -g` -v "$PWD":/data latex bash -c 'mkdir -p output; pdflatex -output-directory=output ResumeContent.tex'
```

## Option Switches

Options are in `Config.tex` file.

``` latex
\def\resVersion{GeneralPurpose} % [Software, Hardware, GeneralPurpose]
\def\resPresetFormat{Custom} % [OnePage, TwoPage, Custom]
\def\resMyEmail{50459973+ly4096x@users.noreply.github.com}

\ifx\resPresetFormat\resPresetFormatCustom
    \def\resShowUrls{1}
    \def\resShowTopBanner{0}
    \def\resShowTechnicalRange{1}
    \def\resShowEducationDetails{1} % [0-1]
    \def\resShowWorkExperienceDetails{2} % [0-2]
    \def\resShowSkillsAndAbilities{1}
    \def\resShowHonorsAndAwards{1}
    \def\resShowHonorsAndAwardsDetails{2} % [0-2]
    \def\resShowProjects{1}
    \def\resShowProjectsDetails{1} % [0-1]
\fi
```

These are the currently adjustable switches. These values control whether to show some fields, and how much detail to show.

## License

Format is MIT but all the data is owned by Yang Liu.
