EMAIL='50459973+ly4096x@users.noreply.github.com'

mkdir -p output
for i in {1..2}; do
pdflatex -output-directory=output -jobname='Resume_Software_OnePage'       '\def\resMyEmail{'"$EMAIL"'} \def\resVersion{Software}       \def\resPresetFormat{OnePage} \input{ResumeContent.tex}'
pdflatex -output-directory=output -jobname='Resume_Software_TwoPage'       '\def\resMyEmail{'"$EMAIL"'} \def\resVersion{Software}       \def\resPresetFormat{TwoPage} \input{ResumeContent.tex}'
pdflatex -output-directory=output -jobname='Resume_GeneralPurpose_OnePage' '\def\resMyEmail{'"$EMAIL"'} \def\resVersion{GeneralPurpose} \def\resPresetFormat{OnePage} \input{ResumeContent.tex}'
pdflatex -output-directory=output -jobname='Resume_GeneralPurpose_TwoPage' '\def\resMyEmail{'"$EMAIL"'} \def\resVersion{GeneralPurpose} \def\resPresetFormat{TwoPage} \input{ResumeContent.tex}'
done
cd output
rm *.out *.aux *.log
