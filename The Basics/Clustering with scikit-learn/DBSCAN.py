from sklearn.cluster import DBSCAN

# ε maximum distance between two data
dbscan = DBSCAN(eps=1.2, min_samples=30) # eps = ε, min_samples = minimum size of a core sample's neighborhood

# predefined data
dbscan.fit(data)

# cluster assignments
print('{}\n'.format(repr(dbscan.labels_)))
# array([ 0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,
#         0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,
#         0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  1,
#         1,  1,  1,  1,  1,  1,  1,  1,  1,  1,  1,  1,  1,  1,  1,  1,  1,
#         1,  1,  1,  1,  1,  1,  1,  1,  1,  1,  1,  1,  1,  1,  1,  1,  1,
#         1,  1,  1,  1,  1,  1,  1,  1,  1,  1,  1,  1,  1,  1,  1,  1,  1,
#         1,  1,  1,  1,  1,  1,  1,  1,  1,  1,  1,  1,  1,  1,  1,  1, -1,
#         1,  1,  1,  1,  1,  1,  1,  1,  1,  1,  1,  1,  1,  1,  1,  1,  1,
#         1,  1,  1,  1,  1,  1,  1,  1,  1,  1,  1,  1,  1,  1])

# core samples
print('{}\n'.format(repr(dbscan.core_sample_indices_)))
num_core_samples = len(dbscan.core_sample_indices_)
print('Num core samples: {}\n'.format(num_core_samples))
# array([  0,   1,   2,   3,   4,   5,   6,   7,   8,   9,  10,  11,  12,
#         13,  16,  17,  18,  19,  20,  21,  22,  23,  24,  25,  26,  27,
#         28,  29,  30,  31,  32,  33,  34,  35,  36,  37,  38,  39,  40,
#         42,  43,  44,  45,  46,  47,  48,  49,  50,  51,  52,  53,  54,
#         55,  56,  58,  59,  61,  62,  63,  64,  65,  66,  67,  68,  69,
#         70,  71,  72,  73,  74,  75,  76,  77,  78,  79,  80,  81,  82,
#         83,  84,  85,  86,  87,  88,  89,  90,  91,  92,  94,  95,  96,
#         97,  99, 101, 102, 103, 104, 108, 110, 111, 112, 113, 114, 115,
#        116, 119, 120, 121, 123, 124, 125, 126, 127, 128, 129, 132, 133,
#        134, 136, 137, 138, 139, 140, 141, 142, 143, 144, 145, 146, 147,
#        148, 149])
# Num core samples: 132