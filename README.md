# Flexible_Resume

A flexible resume with configurable options. The output can be easily changed with a few switches to match different requirements.

This resume is based on [https://github.com/sb2nov/resume](https://github.com/sb2nov/resume).

# Option Switches

Option switches are in the beginning of the resume source file.

``` latex
\def\resVersion{GeneralPurpose} % [Software, Hardware, GeneralPurpose]

\def\resShowUrls{1}
\def\resShowTopBanner{1}
\def\resShowTechnicalRange{0}
\def\resShowWorkExperienceDetails{1} % [0-2]
\def\resShowSkillsAndAbilities{1}
\def\resShowHonorsAndAwards{1}
\def\resShowHonorsAndAwardsDetails{0} % [0-2]
\def\resShowProjects{0}
\def\resShowProjectsDetails{1} % [0-1]
```

These are the currently adjustable switches. These values control whether to show some fields, and how much detail to show.

# License

Format is MIT but all the data is owned by Yang Liu.
