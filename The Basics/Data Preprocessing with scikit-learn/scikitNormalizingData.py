from sklearn.preprocessing import Normalizer

data = [[4, 1, 2, 2],
       [3, 4, 0, 0],
       [7, 5, 9, 2]]
normalizer = Normalizer()
transformed = normalizer.fit_transform(data)
# [[0.8       , 0.2       , 0.4       , 0.4       ],
#  [0.6       , 0.8       , 0.        , 0.        ],
#  [0.55513611, 0.39652579, 0.71374643, 0.15861032]]

# Example
# The function will apply L2 normalization to the input NumPy array, data.
# Input:[[2000  900  100  700]
#        [ 900  410   39  344]
#        [1232  560   67  400]
#        [4012 2032  199 1512]]
def normalize_data(data):
  normalizer = Normalizer()
  norm_data = normalizer.fit_transform(data)
  return norm_data
# Output:[[0.86792607 0.39056673 0.0433963  0.30377413]
#         [0.85891432 0.39128319 0.03721962 0.32829614]
#         [0.87204702 0.39638501 0.04742464 0.28313215]
#         [0.84484854 0.42789936 0.0419055  0.31839756]]