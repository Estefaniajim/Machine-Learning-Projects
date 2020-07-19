from sklearn import linear_model
import numpy as np

pizza_data = [[2100,  800],
       [2500,  850],
       [1800,  760],
       [2000,  800],
       [2300,  810]]
pizza_prices = [10.99, 12.5,  9.99, 10.99, 11.99]
reg = linear_model.LinearRegression()
reg.fit(pizza_data, pizza_prices)
# new pizza data
new_pizzas = np.array([[2000,  820],
                       [2200,  830]])
price_predicts = reg.predict(new_pizzas)
print('{}\n'.format(repr(price_predicts)))
print('Coefficients: {}\n'.format(repr(reg.coef_)))
print('Intercept: {}\n'.format(reg.intercept_))
# Using previously defined pizza_data, pizza_prices
r2 = reg.score(pizza_data, pizza_prices)
print('R2: {}\n'.format(r2))

# Example
# The function will fit a basic least squares
# regression model to the input data and labels.
def linear_reg(data, labels):
  reg = linear_model.LinearRegression()
  reg.fit(data,labels)
  return reg