import numpy as np
from sklearn.cluster import KMeans
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

