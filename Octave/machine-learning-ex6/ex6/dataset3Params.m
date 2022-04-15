function [C, sigma] = dataset3Params(X, y, Xval, yval)
%DATASET3PARAMS returns your choice of C and sigma for Part 3 of the exercise
%where you select the optimal (C, sigma) learning parameters to use for SVM
%with RBF kernel
%   [C, sigma] = DATASET3PARAMS(X, y, Xval, yval) returns your choice of C and 
%   sigma. You should complete this function to return the optimal C and 
%   sigma based on a cross-validation set.
%

% You need to return the following variables correctly.
C = 1;
sigma = 0.3;

% ====================== YOUR CODE HERE ======================
% Instructions: Fill in this function to return the optimal C and sigma
%               learning parameters found using the cross validation set.
%               You can use svmPredict to predict the labels on the cross
%               validation set. For example, 
%                   predictions = svmPredict(model, Xval);
%               will return the predictions on the cross validation set.
%
%  Note: You can compute the prediction error using 
%        mean(double(predictions ~= yval))
%
C_options = [0.01, 0.03, 0.1, 0.3, 1, 3, 10, 30];
sigma_options = [0.01, 0.03, 0.1, 0.3, 1, 3, 10, 30];
items = length(C_options);
result = zeros(items * items, 1);

for i=1:items,
  C_i = C_options(i);
  for j=1:items,
    sigma_j = sigma_options(j);
    % train and compute the prediction:
    model= svmTrain(X, y, C_i, @(x1, x2) gaussianKernel(x1, x2, sigma_j), 1e-3, 20);
    pred = svmPredict(model, Xval);
    
    %compute error on validation data:
    result((i-1) * items + j) = mean(double(pred ~= yval));
  end
end;

%find minimum error value:
[minError, index] = min(result);
C = C_options(floor(index/items)+1);
sigma = sigma_options(index - floor(index/items)*items);
% =========================================================================

end
