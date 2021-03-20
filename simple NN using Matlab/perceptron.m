clear all;
close all;
clc;
x=[1 1 0 0; 1 0 1 0];
w=[0 0];
b=0;
alpha=1;
t=[1 -1 -1 -1];
theta=0;
yes=1;
epoch=0;
while yes 
    yes=0;
    for i=1:4
        yin=b+x(1,i)*w(1)+x(2,i)*w(2);
    if(yin>theta)
        y=1;
    end;
    if((yin<=theta) && (yin>=-theta))
        y=0;
    end;
    if( yin<-theta)
        y=-1;
    end
     if(y-t(i))
         yes=1;     
         for j=1:2
             w(j)=w(j)+t(i)*x(j,i);
         end
    b=b+t(i)*alpha;
     end
    end
    epoch=epoch+1;
    end

disp('Perceptron ');

disp('final weights ');disp(w);
disp('final bias ');
disp(b);
disp('epoch ');
disp(epoch);


plot(x(1,1),'or','markersize',20,'markerfacecolor',[0 0 1]);hold on
plot(x(1,2),x(2,2),'or','MarkerSize',20,'MarkerFaceColor',[1 0 0]);hold on
plot(x(1,3),x(2,3),'or','markersize',20,'markerfacecolor',[1 0 0]);hold on
plot(x(1,4),x(2,4),'or','markersize',20,'markerfacecolor',[1 0 0]);hold on
