from sklearn.metrics.pairwise import cosine_similarity
import numpy as np
# It calculates the cosine similarities for pairs of data observations
# in a single dataset, or pairs of data observations between two datasets.
# The value at index (i, j) of cos_sims is the cosine similarity between data observations i and j in data.
# Since cosine similarity is symmetric, the cos_sims array contains the same values at index (i, j) and (j, i).
data = np.array([
  [ 1.1,  0.3],
  [ 2.1,  0.6],
  [-1.1, -0.4],
  [ 0. , -3.2]])
cos_sims = cosine_similarity(data)
print('{}\n'.format(repr(cos_sims)))
# array([[ 1.        ,  0.99992743, -0.99659724, -0.26311741],
#        [ 0.99992743,  1.        , -0.99751792, -0.27472113],
#        [-0.99659724, -0.99751792,  1.        ,  0.34174306],
#        [-0.26311741, -0.27472113,  0.34174306,  1.        ]])
