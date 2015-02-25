#!/bin/bash

FILE="theory_of_sound_field_synthesis"

# Run LaTeX and modify metadata of PDF file (this has to be done after the
# compilation of the PDF, because the gnuplot figures overwrites the
# hyperref settings)
latexmk && \
mv ${FILE}.pdf ${FILE}_tmp.pdf && \
pdftk ${FILE}_tmp.pdf \
    update_info metadata.txt \
    output ${FILE}.pdf
rm ${FILE}_tmp.pdf
