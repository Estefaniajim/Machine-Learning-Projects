import xgboost as xgb
import numpy as np

# DMatrix
data = np.array([
  [1.2, 3.3, 1.4],
  [5.1, 2.2, 6.6]])
dmat1 = xgb.DMatrix(data)
labels = np.array([0, 1])
dmat2 = xgb.DMatrix(data, label=labels)

# The DMatrix object can be used for training and using a Booster object,
# which represents the gradient boosted decision tree.
# The train function in XGBoost lets us train a Booster with a specified set of parameters.
# predefined data and labels
print('Data shape: {}'.format(data.shape))
print('Labels shape: {}'.format(labels.shape))
dtrain = xgb.DMatrix(data, label=labels)

# training parameters
params = {
  'max_depth': 0,
  'objective': 'binary:logistic'
}
print('Start training')
bst = xgb.train(params, dtrain)  # booster
print('Finish training')
# Data shape: (569, 30)
# Labels shape: (569,)
# Start training
# [23:00:36] /workspace/src/tree/updater_prune.cc:74: tree pruning end, 1 roots, 0 extra nodes, 0 pruned nodes, max_depth=0
# [23:00:36] /workspace/src/tree/updater_prune.cc:74: tree pruning end, 1 roots, 0 extra nodes, 0 pruned nodes, max_depth=0
# [23:00:36] /workspace/src/tree/updater_prune.cc:74: tree pruning end, 1 roots, 0 extra nodes, 0 pruned nodes, max_depth=0
# [23:00:36] /workspace/src/tree/updater_prune.cc:74: tree pruning end, 1 roots, 0 extra nodes, 0 pruned nodes, max_depth=0
# [23:00:36] /workspace/src/tree/updater_prune.cc:74: tree pruning end, 1 roots, 0 extra nodes, 0 pruned nodes, max_depth=0
# [23:00:36] /workspace/src/tree/updater_prune.cc:74: tree pruning end, 1 roots, 0 extra nodes, 0 pruned nodes, max_depth=0
# [23:00:36] /workspace/src/tree/updater_prune.cc:74: tree pruning end, 1 roots, 0 extra nodes, 0 pruned nodes, max_depth=0
# [23:00:36] /workspace/src/tree/updater_prune.cc:74: tree pruning end, 1 roots, 0 extra nodes, 0 pruned nodes, max_depth=0
# [23:00:36] /workspace/src/tree/updater_prune.cc:74: tree pruning end, 1 roots, 0 extra nodes, 0 pruned nodes, max_depth=0
# [23:00:36] /workspace/src/tree/updater_prune.cc:74: tree pruning end, 1 roots, 0 extra nodes, 0 pruned nodes, max_depth=0
# Finish training

# Using a Booster
# After training a Booster, we can evaluate it and use it to make predictions.
# predefined evaluation data and labels
print('Data shape: {}'.format(eval_data.shape))
print('Labels shape: {}'.format(eval_labels.shape))
deval = xgb.DMatrix(eval_data, label=eval_labels)

# Trained bst from previous code
print(bst.eval(deval))  # evaluation

# new_data contains 2 new data observations
dpred = xgb.DMatrix(new_data)
# predictions represents probabilities
predictions = bst.predict(dpred)
print('{}\n'.format(predictions))
# Data shape: (119, 30)
# Labels shape: (119,)
# [0]	eval-error:0.226891
# [0.6236573 0.6236573]

# Example
# Train a Booster object on input data and labels
dtrain = xgb.DMatrix(data, label=labels)
params = {"max_depth": 2, "objective": "multi:softmax", "num_class":3}
bst = xgb.train(params, dtrain)