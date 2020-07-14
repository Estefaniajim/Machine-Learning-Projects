from sklearn.preprocessing import MinMaxScaler

# Range compression in scikit-learn
data = [[1.2, 3.2],
        [-0.3, -1.2],
        [6.5, 10.1],
        [2.2, -8.4]]
default_scaler = MinMaxScaler()  # the default range is [0,1]
transformed = default_scaler.fit_transform(data)
# [[0.22058824, 0.62702703],
#  [0.        , 0.38918919],
#  [1.        , 1.        ],
#  [0.36764706, 0.        ]]
custom_scaler = MinMaxScaler(feature_range=(-2, 3))
transformed = custom_scaler.fit_transform(data)
# [[-0.89705882,  1.13513514],
#  [-2.        , -0.05405405],
#  [ 3.        ,  3.        ],
#  [-0.16176471, -2.        ]]
new_data = [[1.2, -0.5],
            [5.3, 2.3],
            [-3.3, 4.1]]
default_scaler = MinMaxScaler()  # the default range is [0,1]
transformed = default_scaler.fit_transform(new_data)
# [[0.52325581, 0.        ],
# [1.        , 0.60869565],
# [0.        , 1.        ]]
default_scaler = MinMaxScaler()  # new instance
default_scaler.fit(data)  # different data value fit
transformed = default_scaler.transform(new_data)
# [[ 0.22058824,  0.42702703],
# [ 0.82352941,  0.57837838],
# [-0.44117647,  0.67567568]]

# Examples
# The function will compress the input NumPy array, data, into the range given by value_range.
# Input:
# data = [[2000  900  100  700]
#  [ 900  410   39  344]
#  [1232  560   67  400]
#  [4012 2032  199 1512]]
# value_range = (10, 20)
def ranged_data(data, value_range):
    min_max_scaler = MinMaxScaler(feature_range=value_range)
    scaled_data = min_max_scaler.fit_transform(data)
    return scaled_data
# Output: [[13.53470437 13.02096178 13.8125     13.04794521]
#          [10.         10.         10.         10.        ]
#          [11.06683805 10.92478422 11.75       10.47945205]
#          [20.         20.         20.         20.        ]]