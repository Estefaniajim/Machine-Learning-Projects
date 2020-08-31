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
