EMAIL='50459973+ly4096x@users.noreply.github.com'
PHONE='+1-(000)-000-0000'
ADDR='100 Anonymous St, New York NY 10001'

DEFAULT_INFO="\\def\\resMyEmail{$EMAIL} \\def\\resMyPhone{$PHONE} \\def\\resMyAddress{$ADDR}"

mkdir -p output
for i in {1..2}; do
pdflatex -output-directory=output -jobname='Resume_Software_OnePage'           "$DEFAULT_INFO"' \def\resVersion{Software}        \def\resPresetFormat{OnePage}    \input{ResumeContent.tex}'
pdflatex -output-directory=output -jobname='Resume_Software_TwoPage'           "$DEFAULT_INFO"' \def\resVersion{Software}        \def\resPresetFormat{TwoPage}    \input{ResumeContent.tex}'
pdflatex -output-directory=output -jobname='Resume_SoftAndHardware_OnePage'    "$DEFAULT_INFO"' \def\resVersion{SoftAndHardware} \def\resPresetFormat{OnePage}    \input{ResumeContent.tex}'
pdflatex -output-directory=output -jobname='Resume_SoftAndHardware_TwoPage'    "$DEFAULT_INFO"' \def\resVersion{SoftAndHardware} \def\resPresetFormat{TwoPage}    \input{ResumeContent.tex}'
pdflatex -output-directory=output -jobname='Resume_SoftAndHardware_NotForWork' "$DEFAULT_INFO"' \def\resVersion{SoftAndHardware} \def\resPresetFormat{NotForWork} \input{ResumeContent.tex}'
done
cd output
rm *.out *.aux *.log
