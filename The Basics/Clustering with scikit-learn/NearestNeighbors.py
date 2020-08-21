import numpy as np
from sklearn.neighbors import NearestNeighbors

# The default value for k when initializing the NearestNeighbors object is 5

# 5 nearest neighbors for a new data observation
data = np.array([
  [5.1, 3.5, 1.4, 0.2],
  [4.9, 3. , 1.4, 0.2],
  [4.7, 3.2, 1.3, 0.2],
  [4.6, 3.1, 1.5, 0.2],
  [5. , 3.6, 1.4, 0.2],
  [5.4, 3.9, 1.7, 0.4],
  [4.6, 3.4, 1.4, 0.3],
  [5. , 3.4, 1.5, 0.2],
  [4.4, 2.9, 1.4, 0.2],
  [4.9, 3.1, 1.5, 0.1]])
nbrs = NearestNeighbors()
nbrs.fit(data)
new_obs = np.array([[5. , 3.5, 1.6, 0.3]])
dists, knbrs = nbrs.kneighbors(new_obs)

# nearest neighbors indexes
print('{}\n'.format(repr(knbrs)))
# array([[7, 4, 0, 6, 9]])

# nearest neighbor distances
print('{}\n'.format(repr(dists)))
# array([[0.17320508, 0.24494897, 0.24494897, 0.45825757, 0.46904158]])

only_nbrs = nbrs.kneighbors(new_obs,
                            return_distance=False)
print('{}\n'.format(repr(only_nbrs)))
# array([[7, 4, 0, 6, 9]])

# We can specify a new value of K
nbrs = NearestNeighbors(n_neighbors=2)
nbrs.fit(data)
new_obs = np.array([
  [5. , 3.5, 1.6, 0.3],
  [4.8, 3.2, 1.5, 0.1]])
dists, knbrs = nbrs.kneighbors(new_obs)