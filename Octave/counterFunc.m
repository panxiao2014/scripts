function C = counterFunc(Y)

m = max(Y);
C = zeros(1,m);
len = length(Y);

for i=1:len,
  C(Y(i)) = C(Y(i)) + 1;
end;