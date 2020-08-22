import numpy as np
from sklearn.cluster import KMeans
from sklearn.cluster import MiniBatchKMeans

# The K-means clustering algorithm will separate the data into
# K clusters (the number of clusters is chosen by the user) using cluster means,
# also known as centroids.
# These centroids represent the "centers" of each cluster.
# Specifically, a cluster's centroid is equal to the average of all the data
# observations within the cluster.
cluster = np.array([
  [ 1.2, 0.6],
  [ 2.4, 0.8],
  [-1.6, 1.4],
  [ 0. , 1.2]])
centroid = cluster.mean(axis=0)
# array([0.5, 1. ])

# 3 clusters
kmeans = KMeans(n_clusters=3)
kmeans.fit(data) # predefined data
# cluster assignments
# the final cluster assignments for each data observation
print('{}\n'.format(repr(kmeans.labels_)))
# array([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
#        1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
#        1, 1, 1, 1, 1, 1, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
#        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
#        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 2, 2, 2, 2, 0, 2, 2, 2,
#        2, 2, 2, 0, 0, 2, 2, 2, 2, 0, 2, 0, 2, 0, 2, 2, 0, 0, 2, 2, 2, 2,
#        2, 0, 2, 2, 2, 2, 0, 2, 2, 2, 0, 2, 2, 2, 0, 2, 2, 0], dtype=int32)
# centroids
print('{}\n'.format(repr(kmeans.cluster_centers_)))
# array([[5.9016129 , 2.7483871 , 4.39354839, 1.43387097],
#        [5.006     , 3.418     , 1.464     , 0.244     ],
#        [6.85      , 3.07368421, 5.74210526, 2.07105263]])
# Now we make the prediction
new_obs = np.array([
  [5.1, 3.2, 1.7, 1.9],
  [6.9, 3.2, 5.3, 2.2]])
# predict clusters
print('{}\n'.format(repr(kmeans.predict(new_obs))))
# array([1, 2], dtype=int32)

# Mini-batch clustering
kmeans = MiniBatchKMeans(n_clusters=3, batch_size=10)
# predefined data
kmeans.fit(data)
# cluster assignments
print('{}\n'.format(repr(kmeans.labels_)))
# array([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
#        1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
#        1, 1, 1, 1, 1, 1, 0, 0, 0, 2, 0, 2, 0, 2, 0, 2, 2, 2, 2, 2, 2, 0,
#        2, 2, 2, 2, 0, 2, 0, 2, 2, 0, 0, 0, 2, 2, 2, 2, 2, 0, 2, 2, 0, 2,
#        2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0,
#        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
#        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], dtype=int32)
# centroids
print('{}\n'.format(repr(kmeans.cluster_centers_)))
# array([[6.43103448, 2.96034483, 5.13448276, 1.82068966],
#        [5.00217391, 3.4326087 , 1.4826087 , 0.24782609],
#        [5.72777778, 2.78333333, 4.24722222, 1.35      ]])
# Now we make a new prediction
new_obs = np.array([
  [5.1, 3.2, 1.7, 1.9],
  [6.9, 3.2, 5.3, 2.2]])
# predict clusters
print('{}\n'.format(repr(kmeans.predict(new_obs))))
# array([1, 0], dtype=int32)

# Example
# The function will use either KMeans or MiniBatchKMeans for clustering data.
