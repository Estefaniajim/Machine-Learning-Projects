from sklearn.preprocessing import RobustScaler

data = [[ 1.2,  2.3],
       [ 2.1,  4.2],
       [-1.9,  3.1],
       [-2.5,  2.5],
       [ 0.8,  3. ],
       [ 6.3,  2.1],
       [-1.5,  2.7],
       [ 1.4,  2.9],
       [ 1.8,  3.2]]
robust_scaler = RobustScaler()
transformed = robust_scaler.fit_transform(data)
# [[ 0.        , -1.        ],
#  [ 0.27272727,  2.16666667],
#  [-0.93939394,  0.33333333],
#  [-1.12121212, -0.66666667],
#  [-0.12121212,  0.16666667],
#  [ 1.54545455, -1.33333333],
#  [-0.81818182, -0.33333333],
#  [ 0.06060606,  0.        ],
#  [ 0.18181818,  0.5       ]]

# Examples
# The function will apply outlier-independent scaling to the input NumPy array, data.
# Input: [[2000  900  100  700]
#         [ 900  410   39  344]
#         [1232  560   67  400]
#         [4012 2032  199 1512]]
def robust_scaling(data):
  robust_scaler = RobustScaler()
  scaled_data = robust_scaler.fit_transform(data)
  return scaled_data
# Output: [[ 0.28360414  0.25738077  0.25482625  0.2901354 ]
#          [-0.52880355 -0.48448145 -0.68725869 -0.39845261]
#          [-0.28360414 -0.25738077 -0.25482625 -0.2901354 ]
#          [ 1.76957164  1.97123391  1.78378378  1.86073501]]