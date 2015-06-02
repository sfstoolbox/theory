#!/bin/bash

# Replot all the figures that are produced with the SFS Toolbox.
# This should be done for every new release of the Toolbox.

FIGPATH="02_theory_of_sound_field_synthesis"
SFSPATH="~/git/sfs"
MATLAB="octave"
MOPT="-q -p $SFSPATH --eval 'SFS_start;'"
GNUPLOT="gnuplot"
GOPT=""

cd $FIGPATH

# Fig. 2.2
echo "# Fig. 2.2"
cd fig2_02
eval $MATLAB $MOPT concave_array.m
$GNUPLOT $GOPT concave_array.gnu
cd ..

# Fig 2.4
echo "# Fig. 2.4"
cd fig2_04
eval $MATLAB $MOPT sound_field_plane_wave.m
$GNUPLOT $GOPT sound_field_plane_wave.gnu
cd ..

# Fig 2.5
echo "# Fig. 2.5"
cd fig2_05
eval $MATLAB $MOPT sound_field_point_source.m
$GNUPLOT $GOPT sound_field_point_source.gnu
cd ..

# Fig 2.6
echo "# Fig. 2.6"
cd fig2_06
eval $MATLAB $MOPT sound_field_line_source.m
$GNUPLOT $GOPT sound_field_line_source.gnu
cd ..

# Fig 2.7
echo "# Fig. 2.7"
cd fig2_07
eval $MATLAB $MOPT sound_field_nfchoa_pw.m
$GNUPLOT $GOPT sound_field_nfchoa_pw.gnu
cd ..

# Fig 2.8
echo "# Fig. 2.8"
cd fig2_08
eval $MATLAB $MOPT sound_field_nfchoa_ps.m
$GNUPLOT $GOPT sound_field_nfchoa_ps.gnu
cd ..

# Fig 2.9
echo "# Fig. 2.9"
cd fig2_09
eval $MATLAB $MOPT sound_field_wfs_pw.m
$GNUPLOT $GOPT sound_field_wfs_pw.gnu
cd ..

# Fig 2.10
echo "# Fig. 2.10"
cd fig2_10
eval $MATLAB $MOPT sound_field_wfs_ps.m
$GNUPLOT $GOPT sound_field_wfs_ps.gnu
cd ..

# Fig 2.11
echo "# Fig. 2.11"
cd fig2_11
eval $MATLAB $MOPT sound_field_wfs_ls.m
$GNUPLOT $GOPT sound_field_wfs_ls.gnu
cd ..

# Fig 2.12
echo "# Fig. 2.12"
cd fig2_12
eval $MATLAB $MOPT sound_field_wfs_fs.m
$GNUPLOT $GOPT sound_field_wfs_fs.gnu
cd ..

cd ..
