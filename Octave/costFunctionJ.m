function J = costFunctionJ(X, y, theta)

% X is the design matrix containing training examples.
% y is the class labels

m = size(X, 1); %number of rows (training examples)
predictions = X * theta; %predications of hypothesis on all m examples
sqrErrors = (predictions - y).^2;

J = 1/(2*m) * sum(sqrErrors);