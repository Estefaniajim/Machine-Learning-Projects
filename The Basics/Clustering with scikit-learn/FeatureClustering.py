from sklearn.cluster import FeatureAgglomeration

print('Original shape: {}\n'.format(data.shape))
# Original shape: (150, 4)
print('First 10:\n{}\n'.format(repr(data[:10])))
# First 10:
# array([[5.1, 3.5, 1.4, 0.2],
#        [4.9, 3. , 1.4, 0.2],
#        [4.7, 3.2, 1.3, 0.2],
#        [4.6, 3.1, 1.5, 0.2],
#        [5. , 3.6, 1.4, 0.2],
#        [5.4, 3.9, 1.7, 0.4],
#        [4.6, 3.4, 1.4, 0.3],
#        [5. , 3.4, 1.5, 0.2],
#        [4.4, 2.9, 1.4, 0.2],
#        [4.9, 3.1, 1.5, 0.1]])

agg = FeatureAgglomeration(n_clusters=2)
new_data = agg.fit_transform(data)
print('New shape: {}\n'.format(new_data.shape))
# New shape: (150, 2)
print('First 10:\n{}\n'.format(repr(new_data[:10])))
# First 10:
# array([[1.7       , 5.1       ],
#        [1.53333333, 4.9       ],
#        [1.56666667, 4.7       ],
#        [1.6       , 4.6       ],
#        [1.73333333, 5.        ],
#        [2.        , 5.4       ],
#        [1.7       , 4.6       ],
#        [1.7       , 5.        ],
#        [1.5       , 4.4       ],
#        [1.56666667, 4.9       ]])