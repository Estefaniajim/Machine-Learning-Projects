from sklearn.cluster import FeatureAgglomeration

print('Original shape: {}\n'.format(data.shape))
print('First 10:\n{}\n'.format(repr(data[:10])))

agg = FeatureAgglomeration(n_clusters=2)
new_data = agg.fit_transform(data)
print('New shape: {}\n'.format(new_data.shape))
print('First 10:\n{}\n'.format(repr(new_data[:10])))