from sklearn.cluster import AgglomerativeClustering
# Agglomerative clustering
agg = AgglomerativeClustering(n_clusters=3)
# predefined data
agg.fit(data)
# cluster assignments
print('{}\n'.format(repr(agg.labels_)))