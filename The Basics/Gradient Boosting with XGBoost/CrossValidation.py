import xgboost as xgb

# predefined data and labels
dtrain = xgb.DMatrix(data, label=labels)
params = {
  'max_depth': 2,
  'lambda': 1.5,
  'objective':'binary:logistic'
}
cv_results = xgb.cv(params, dtrain)
print('CV Results:\n{}'.format(cv_results))

# predefined data and labels
dtrain = xgb.DMatrix(data, label=labels)
params = {
  'max_depth': 2,
  'lambda': 1.5,
  'objective':'binary:logistic'
}
cv_results = xgb.cv(params, dtrain, num_boost_round=5)
print('CV Results:\n{}'.format(cv_results))