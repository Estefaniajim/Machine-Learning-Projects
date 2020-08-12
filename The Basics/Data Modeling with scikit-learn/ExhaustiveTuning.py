from sklearn import linear_model
from sklearn.model_selection import GridSearchCV

# Implementation of grid search cross-validation
reg = linear_model.BayesianRidge()
params = {
  'alpha_1':[0.1,0.2,0.3],
  'alpha_2':[0.1,0.2,0.3]
}
reg_cv = GridSearchCV(reg, params, cv=5, iid=False)
# predefined train and test sets
reg_cv.fit(train_data, train_labels)
print(reg_cv.best_params_)
# {'alpha_2': 0.3, 'alpha_1': 0.3}