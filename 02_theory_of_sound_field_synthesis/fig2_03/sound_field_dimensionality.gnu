#!/usr/bin/gnuplot
#
# <+DESCRIPTION+>
#
# AUTHOR: Hagen Wierstorf
# gnuplot 4.6 patchlevel 3

reset
set macros
set loadpath '../../gnuplot'

set terminal epslatex size 5cm,6.5cm color colortext

load 'noborder.cfg'
load 'blues.pal'

unset key
unset colorbox

set size ratio -1 

set cbrange [-40:-5]

set xrange [-2:0]
set yrange [-1.5:0.5]
set output '25d_xy_1.tex'
plot '25d_xy.dat' binary matrix u 1:2:(20*log10($3)) w image
set xrange [0:2]
set yrange [-1.5:0.5]
set output '25d_xy_2.tex'
plot '25d_xy.dat' binary matrix u 1:2:(20*log10($3)) w image

set xrange [-1.5:0.5]
set yrange [-1.5:0]
set output '25d_yz_1.tex'
plot '25d_yz.dat' binary matrix u 1:2:(20*log10($3)) w image
set xrange [-1.5:0.5]
set yrange [0:1.5]
set output '25d_yz_2.tex'
plot '25d_yz.dat' binary matrix u 1:2:(20*log10($3)) w image


# 2D
set cbrange [-40:5]

set xrange [-2:0]
set yrange [-1.5:0.5]
set output '2d_xy_1.tex'
plot '2d_xy.dat' binary matrix u 1:2:(20*log10($3)) w image
set xrange [0:2]
set yrange [-1.5:0.5]
set output '2d_xy_2.tex'
plot '2d_xy.dat' binary matrix u 1:2:(20*log10($3)) w image

set xrange [-1.5:0.5]
set yrange [-1.5:0]
set output '2d_yz_1.tex'
plot '2d_yz.dat' binary matrix u 1:2:(20*log10($3)) w image
set xrange [-1.5:0.5]
set yrange [0:1.5]
set output '2d_yz_2.tex'
plot '2d_yz.dat' binary matrix u 1:2:(20*log10($3)) w image

