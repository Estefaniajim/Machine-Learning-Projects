from sklearn import linear_model
pizza_data = [[2100,  800],
       [2500,  850],
       [1800,  760],
       [2000,  800],
       [2300,  810]]
pizza_prices = [10.99, 12.5,  9.99, 10.99, 11.99]
reg = linear_model.Ridge(alpha=0.1)
reg.fit(pizza_data, pizza_prices)
r2 = reg.score(pizza_data, pizza_prices)
print('R2: {}\n'.format(r2))
alphas = [0.1, 0.2, 0.3]
reg = linear_model.RidgeCV(alphas=alphas)
reg.fit(pizza_data, pizza_prices)
print('Coefficients: {}\n'.format(repr(reg.coef_)))
print('Intercept: {}\n'.format(reg.intercept_))
print('Chosen alpha: {}\n'.format(reg.alpha_))