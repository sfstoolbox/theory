#!/usr/bin/gnuplot
#
# <+DESCRIPTION+>
#
# AUTHOR: Hagen Wierstorf
# gnuplot 4.6 patchlevel 3

reset
set macros
set loadpath '../../gnuplot'

set terminal epslatex size 8cm,5cm color colortext
set output 'coordinate_system.tex'

load 'border.cfg'
set border 1+2+16
load 'noborder.cfg'
unset tics
set view 37,11
load 'paired.pal'

unset key


set parametric
#set samples 4000
#set isosamples 400

set xrange [0:1.2]
set yrange [0:1.2]
set zrange [0:1.2]
set xyplane at 0
set urange [0:pi/4]
set vrange [0:pi/4]

set lmargin screen 0.18
set rmargin screen 0.98
set tmargin screen 0.88
set bmargin screen 0.28
set xlabel '$x$' offset graph 0,0.08
set ylabel '$y$' offset graph -1.3,0.13
set zlabel '$z$' offset graph 0.18,0

# Arrows
h = sqrt(2)
set arrow from 0,0,0 to 1,1,h front ls 2 lw 3
set arrow from 1,1,0 to 1,1,h nohead ls 1
set arrow from 0,0 to 1,1 nohead back ls 1
set arrow from 1,0 to 1,1 nohead back ls 1
set arrow from 0,1 to 1,1 nohead back ls 1

# Arrows on axes
set arrow from 0,0,0 to 1.2,0,0 front ls 101 lw 2
set arrow from 0,0,0 to 0,1.2,0 front ls 101 lw 2
set arrow from 0,0,0 to 0,0,1.2 front ls 101 lw 2

# Labels
set label '$\phi$'   at 0.25,0.13,0 textcolor ls 1
set label '$\theta$' at 0.23,0.23,0.18 textcolor ls 1
set label '\vec{x}'  at 0.6,0.6,1.1 textcolor ls 2

# Angle between r' and x axis
r0 = 0.4
fvx(v) = r0*cos(v)
fvy(v) = r0*sin(v)
fvz = 0
# Angle between r and r'
r = 0.5
fux(u) = r*cos(u)*cos(pi/4)
fuy(u) = r*cos(u)*sin(pi/4)
fuz(u) = r*sin(u)

splot fvx(v),fvy(v),fvz ls 1 lw 1,\
      fux(u),fuy(u),fuz(u) ls 1 lw 1
