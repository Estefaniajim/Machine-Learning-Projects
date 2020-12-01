import xgboost as xgb

# Saving and loading binary data
dtrain = xgb.DMatrix(data, label=labels)
params = {
  'max_depth': 3,
  'objective':'binary:logistic'
}
bst = xgb.train(params, dtrain)
# 2 new data observations
dpred = xgb.DMatrix(new_data)
print('Probabilities:\n{}'.format(
  repr(bst.predict(dpred))))
bst.save_model('model.bin')

# Restoring a booster
new_bst = xgb.Booster()
new_bst.load_model('model.bin')
print('Probabilities:\n{}'.format(
  repr(new_bst.predict(dpred))))

