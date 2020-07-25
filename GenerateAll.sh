mkdir -p output
pdflatex -output-directory=output -jobname='Resume_Software_OnePage' '\def\resVersion{Software} \def\resPresetFormat{OnePage} \input{ResumeContent.tex}'
pdflatex -output-directory=output -jobname='Resume_Software_TwoPage' '\def\resVersion{Software} \def\resPresetFormat{TwoPage} \input{ResumeContent.tex}'
pdflatex -output-directory=output -jobname='Resume_GeneralPurpose_OnePage' '\def\resVersion{GeneralPurpose} \def\resPresetFormat{OnePage} \input{ResumeContent.tex}'
pdflatex -output-directory=output -jobname='Resume_GeneralPurpose_TwoPage' '\def\resVersion{GeneralPurpose} \def\resPresetFormat{TwoPage} \input{ResumeContent.tex}'
cd output
rm *.out *.aux *.log