clear all;
close all;
x=[1 1 -1 -1; 1 -1 1 -1];
w=[0 0];
b=0;
t=[1 -1 -1 -1];
for i=1:4
    for j=1:2
        w(j)=w(j)+t(i)*x(j,i);
    end
    b=b+t(i);
end
disp('final weight matrix : ');
disp(w);
disp('final bias value ');
disp(b);

plot(x(1,1),'or','markersize',20,'markerfacecolor',[0 0 1]);hold on
plot(x(1,2),x(2,2),'or','MarkerSize',20,'MarkerFaceColor',[1 0 0]);hold on
plot(x(1,3),x(2,3),'or','markersize',20,'markerfacecolor',[1 0 0]);hold on
plot(x(1,4),x(2,4),'or','markersize',20,'markerfacecolor',[1 0 0]);hold on
