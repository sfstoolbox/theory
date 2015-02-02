clear all

%% ===== Configuration ===================================================
X = [-1.75 1.75]; % / m
Y = [-1.75 1.75]; % / m
Z = 0; % / m
xs = [0 2.5 0];
src = 'ps';
f = 1000; % / Hz


%% ===== Toolbox settings ================================================
conf.resolution = 1000; % / samples
conf.xref = [0 0 0]; % / m
conf.dimension = '2.5D';
conf.c = 343; % / m/s
conf.driving_functions = 'default';
conf.phase = 0; % / rad
conf.usenormalisation = true;
conf.plot.useplot = false;
conf.showprogress = true;
conf.nfchoa.order = [];


%% ===== Secondary Sources ===============================================
conf.secondary_sources.size = 3; % / m
conf.secondary_sources.center = [0 0 0]; % / m
conf.secondary_sources.geometry = 'circle';
conf.secondary_sources.number = 1000;
conf.secondary_sources.x0 = [];
% get secondary sources and store them, to do this calculation only once
x0 = secondary_source_positions(conf);
% store complete array and repeat the first loudspeaker in order to draw a
% complete circle
gp_save_loudspeakers('array.txt',[x0; x0(1,:)]);
% use fewer secondary sources, because otherwise we will get -infty
conf.secondary_sources.number = 64;
x0 = secondary_source_positions(conf);
conf.secondary_sources.x0 = x0;

%% ===== Near-field compensated higer order Ambisonics ===================
[P,x,y] = sound_field_mono_nfchoa(X,Y,Z,xs,src,f,conf);
file = sprintf('sound_field_nfchoa_ps_f%iHz_nls%i.dat',f,conf.secondary_sources.number);
gp_save_matrix(file,x,y,real(P));
