import xgboost as xgb

# XGBoost linear regression
model = xgb.XGBRegressor(max_depth=2)
model.fit(data, labels)
predictions = model.predict(new_data)
print('Predictions:\n{}'.format(repr(predictions)))