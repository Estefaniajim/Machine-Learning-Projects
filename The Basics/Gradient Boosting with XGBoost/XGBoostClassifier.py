import xgboost as xgb

# Scikit-learn API

# Binary Classification
model = xgb.XGBClassifier()
model.fit(data, labels)
# new_data contains 2 new data observations
predictions = model.predict(new_data)
print('Predictions:\n{}'.format(repr(predictions)))

# Multiclass Classification
model = xgb.XGBClassifier(objective='multi:softmax')
model.fit(data, labels)
# new_data contains 2 new data observations
predictions = model.predict(new_data)
print('Predictions:\n{}'.format(repr(predictions)))