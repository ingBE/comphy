clc
clear all

load('Kgrid_x.dat');
load('Kgrid_y.dat');
load('Curv_z.dat');


qx = Kgrid_x;
qy = Kgrid_y;
qz1 = Curv_z;


figure1 = figure;
colormap(winter);
axes1 = axes('Parent',figure1);
hold(axes1,'on');

scatter3(qx,qy,qz1(:,18))


% colormap 'winter'
% box on

view(axes1,[90 0]);
box(axes1,'on');
grid(axes1,'on');



