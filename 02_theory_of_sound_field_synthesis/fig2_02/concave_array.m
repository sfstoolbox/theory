clear all;

%% ===== Configuration ===================================================
X = [-9 9]; % / m
Y = [-10 2]; % / m
Z = 0; % / m
f = 700; % / Hz
xs = [0 2.5 0];
src = 'ps';


%% ===== Toolbox settings ================================================
conf.resolution = 1000; % / samples
conf.xref = [0 -3 0]; % / m
conf.dimension = '2.5D';
conf.c = 343; % / m/s
conf.driving_functions = 'default';
conf.phase = 0; % / rad
conf.usenormalisation = true;
conf.plot.useplot = false;
conf.usetapwin = false;
conf.tapwinlen = 0.3;
conf.showprogress = true;


%% ===== Secondary Sources ===============================================
% Create an array with convex and concave elements
% get smal circular arrays
conf.secondary_sources.size = 2; % / m
conf.secondary_sources.center = [0 0 0]; % / m
conf.secondary_sources.geometry = 'circle';
conf.secondary_sources.number = 1000;
conf.secondary_sources.x0 = [];
% get secondary sources and store them, to do this calculation only once
x0 = secondary_source_positions(conf);
% first half
h1 = x0(1:501,:);
% second half
h2 = x0(502:1000,:);
h2(:,5) = -1*h2(:,5); % change direction of sources
% create new array
x00 = h1;                                    % center
x01 = bsxfun(@plus,h2,[2 0 0 0 0 0 0]);      % first right
x_01 = bsxfun(@plus,h2,[-2 0 0 0 0 0 0]);    % first left
x02 = bsxfun(@plus,h1,[4 0 0 0 0 0 0]);      % second right
x_02 = bsxfun(@plus,h1,[-4 0 0 0 0 0 0]);    % second left
x03 = bsxfun(@plus,h2,[6 0 0 0 0 0 0]);      % third right
x_03 = bsxfun(@plus,h2,[-6 0 0 0 0 0 0]);    % third left
x0 = [x_03; x_02; x_01; x00; x01; x02; x03]; % put all together
conf.secondary_sources.x0 = x0;              % store it
gp_save_loudspeakers('concave_array.txt',x0);
x0 = secondary_source_selection(x0,xs,src);
% detect the different parts of the array and store them with an empty line
% between them in order to get now continuous line in the plot
dist = secondary_source_distance(conf.secondary_sources.x0,1);
file = 'concave_array_selected.txt';
fid = fopen(file,'w');
fprintf(fid,'# x0 y0 z0 phi ls_activity\n');
fclose(fid);
idx = 1;
for ii=2:size(x0,1)
    loudspeaker = [];
    if norm(x0(ii,1:3)-x0(ii-1,1:3))>1.5*dist || ii==size(x0,1)
        % Calculate phi
        loudspeaker(:,1:2) = x0(idx:ii-1,1:2);
        [loudspeaker(:,3),~,~] = ...
            cart2sph(x0(idx:ii-1,4),x0(idx:ii-1,5),x0(idx:ii-1,6));
        loudspeaker(:,4) = x0(idx:ii-1,7);
        if isoctave
            dlmwrite(file,loudspeaker,'\t','-append');
        else
            dlmwrite(file,loudspeaker,'delimiter','\t','-append');
        end
        fid = fopen(file,'a');
        fprintf(fid,'\n');
        fclose(fid);
        idx = ii;
    end
end


%% ===== Wave Field Synthesis ============================================
[P,x,y] = sound_field_mono_wfs(X,Y,Z,xs,src,f,conf);
gp_save_matrix('concave_array.dat',x,y,real(P));
