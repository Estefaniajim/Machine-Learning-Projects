from sklearn import linear_model

# reg = linear_model.Lasso(alpha=0.1)
# reg.fit(data, labels)
# Data shape: (150, 4)
# Labels shape: (150,)
# Coefficients: array([ 0.        , -0.        ,  0.40830957,  0.        ])
# Intercept: -0.534699558318563
# R2: 0.895831189504504

# Example
# The function will fit a LASSO regression model to the input data and labels.
# The α hyperparameter for the model is provided to the function via
# the alpha input argument.
def lasso_reg(data, labels, alpha):
  reg = linear_model.Lasso(alpha = alpha)
  reg.fit(data,labels)
  return reg