clear all;

%% ===== Configuration ===================================================
X = [-2 2];
Y = [-2 2];
Z = 0;
xs = [0 0 0];
f = 800;

%% ===== Toolbox settings ================================================
conf.resolution = 1000;
conf.xref = [0 1 0];
conf.plot.useplot = false;
conf.c = 343;
conf.phase = 0;
conf.usenormalisation = true;
conf.showprogress = true;

%% ===== Main ============================================================
[P,x,y,z] = sound_field_mono_point_source(X,Y,Z,xs,f,conf);
gp_save_matrix('sound_field_point_source.dat',x,y,real(P));
