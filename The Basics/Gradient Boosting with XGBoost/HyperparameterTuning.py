import xgboost as xgb
from sklearn.model_selection import GridSearchCV

# Using scikit-learn’s GridSearchCV
model = xgb.XGBClassifier()
params = {'max_depth': range(2, 5)}
cv_model = GridSearchCV(model, params, cv=4, iid=False)
cv_model.fit(data, labels)
print('Best max_depth: {}\n'.format(
  cv_model.best_params_['max_depth']))
# new_data contains 2 new data observations
print('Predictions:\n{}'.format(
  repr(cv_model.predict(new_data))))

