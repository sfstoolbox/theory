clear all
conf = SFS_config_example;

conf.secondary_sources.x0 = [];
conf.secondary_sources.geometry = 'line';
conf.secondary_sources.number = 1001;
conf.secondary_sources.size = 100;

nls = conf.secondary_sources.number;
L = conf.secondary_sources.size;
f = 1000;

% === 2.5D sound field ===
x0 = secondary_source_positions(conf);
[p,x,y,z] = sound_field_mono(0,[-1.5 0.5],[-2 2],x0,'ps',ones(nls,1),f,conf);
gp_save_matrix('25d_yz.dat',y,z,abs(p));
[p,x,y,z] = sound_field_mono([-2 2],[-1.5 0.5],0,x0,'ps',ones(nls,1),f,conf);
gp_save_matrix('25d_xy.dat',x,y,abs(p));

% === 2D/3D sound field ===
p = ones(300);
gp_save_matrix('2d_yz.dat',y,x,abs(p));
gp_save_matrix('2d_xy.dat',x,y,abs(p));
