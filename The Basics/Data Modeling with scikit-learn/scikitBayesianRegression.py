from sklearn import linear_model
reg = linear_model.BayesianRidge()
# Data shape: (150, 4)
# Labels shape: (150,)
# reg.fit(data, labels)
# reg.coef_
# Coefficients: array([-0.11174619, -0.03900476,  0.24330537,  0.57343721])
# reg.intercept_
# Intercept: 0.17022693722601356
# reg.score(data, labels)
# R2: 0.9303454031271241
# reg.alpha_
# Alpha: 20.983865171760993
# reg.lambda_
# Lambda: 9.545491382343116

# Example
# The function will fit a Bayesian ridge regression model to the input data and labels
def bayes_ridge(data, labels):
  reg = linear_model.BayesianRidge()
  reg.fit(data,labels)
  return reg