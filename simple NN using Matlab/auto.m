clea------------r all;
close all;
x=[-1 -1 -1 -1;-1 1 -1 1];
t=x;
w=zeros(size(x,2));
for i=1:2
    w=w+x(i,1:4)'*t(i,1:4);
end;
disp('trining done');
disp('weight matrix');
disp(w);
disp ('testing');
xtest=[ 0 -1 -1 0 ]; 
%xtest=[ 0 0  1 -1 ] unknown pattern 
%xtest=[ 0 1  0 -1 ] unknown pattern 
%xtest=[ 0 0  -1 -1 ] known pattern 
%xtest=[ 0 -1 -1 0  ] known pattern 




yin=xtest*w;
disp('test output for test input sequenc');
disp(yin);
for j=1:4
    if (yin(j)>=0)
        y(j)=1;
    else 
         y(j)=-1;
    end
end 
disp('output activation function');
disp(y);
disp('result');
if x(1,1:4)==y(1:4) | x(2,1:4)==y(1:4)
    disp ('known pattern');
else
    disp('unknown pattern');
end
