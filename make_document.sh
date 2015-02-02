#!/bin/bash
# --- C O N F I G U R A T I O N ---------
FILE=theory_of_sound_field_synthesis
# --- M A I N ---------------------------
# check if we have to add an extra latex run
if ! [[ -f phd-thesis.aux ]]
then
    latex $FILE
fi
if ! [[ -f $FILE.bbl ]]
then
    biber $FILE
fi
# run latex
latex $FILE
dvipdf $FILE
# apply metadata (this has to be done after the compilation of the PDF, because
# the gnuplot figures overwrites the hyperref settings)
mv $FILE.pdf ${FILE}_tmp.pdf
pdftk ${FILE}_tmp.pdf \
    update_info metadata.txt \
    output $FILE.pdf
rm ${FILE}_tmp.pdf
