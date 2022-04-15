function [J, grad] = linearRegCostFunction(X, y, theta, lambda)
%LINEARREGCOSTFUNCTION Compute cost and gradient for regularized linear 
%regression with multiple variables
%   [J, grad] = LINEARREGCOSTFUNCTION(X, y, theta, lambda) computes the 
%   cost of using theta as the parameter for linear regression to fit the 
%   data points in X and y. Returns the cost in J and the gradient in grad

% Initialize some useful values
m = length(y); % number of training examples

% You need to return the following variables correctly 
J = 0;
grad = zeros(size(theta));

% ====================== YOUR CODE HERE ======================
% Instructions: Compute the cost and gradient of regularized linear 
%               regression for a particular choice of theta.
%
%               You should set J to the cost and grad to the gradient.
%

%compute hypothesis:
H = X * theta;

%make theta 1 to be zero since it is not used for regularization:
thetaTemp = [0;theta(2:length(theta))];

%compute cost J:
tempJ = H .- y;
J = 1 / (2 * m) * (tempJ' * tempJ) + lambda / (2 * m) * (thetaTemp' * thetaTemp);

%compute gradient:
grad = 1 / m .* (X' * tempJ) + lambda / m .* thetaTemp;










% =========================================================================

grad = grad(:);

end
