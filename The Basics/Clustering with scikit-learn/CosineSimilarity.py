from sklearn.metrics.pairwise import cosine_similarity
import numpy as np
# It calculates the cosine similarities for pairs of data observations
# in a single dataset, or pairs of data observations between two datasets.
# The value at index (i, j) of cos_sims is the cosine similarity between data observations i and j in data.
# Since cosine similarity is symmetric, the cos_sims array contains the same values at index (i, j) and (j, i).

# 2-D dataset
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

# two datasets
data = np.array([
  [ 1.1,  0.3],
  [ 2.1,  0.6],
  [-1.1, -0.4],
  [ 0. , -3.2]])
data2 = np.array([
  [ 1.7,  0.4],
  [ 4.2, 1.25],
  [-8.1,  1.2]])
cos_sims = cosine_similarity(data, data2)
print('{}\n'.format(repr(cos_sims)))
# array([[ 0.9993819 ,  0.99973508, -0.91578821],
#        [ 0.99888586,  0.99993982, -0.9108828 ],
#        [-0.99308366, -0.9982304 ,  0.87956492],
#        [-0.22903933, -0.28525359, -0.14654866]])

# Example
# Function to compute the most similar data observations
# for each data observation in data
cos_sims = cosine_similarity(data)
# Substitute each diagonal value with 0, so that for each
# data observation we find the most similar observation besides itself.
np.fill_diagonal(cos_sims,0)
# The column containing the largest cosine similarity score
# represents the most similar data observation
# Find the column indexes with the largest value
similar_indexes = cos_sims.argmax(axis=1)