from sklearn.metrics import adjusted_rand_score # ARI
from sklearn.metrics import adjusted_mutual_info_score # AMI
import numpy as np

# ARI
true_labels = np.array([0, 0, 0, 1, 1, 1])
pred_labels = np.array([0, 0, 1, 1, 2, 2])

# AMI