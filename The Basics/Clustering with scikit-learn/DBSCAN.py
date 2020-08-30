from sklearn.cluster import DBSCAN

# ε maximum distance between two data
dbscan = DBSCAN(eps=1.2, min_samples=30) # eps = ε, min_samples, min_samples = minimum size of a core sample's neighborhood