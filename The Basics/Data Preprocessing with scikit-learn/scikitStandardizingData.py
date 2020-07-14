from sklearn.preprocessing import scale

pizza_data = [[2100,   10,  800],
              [2500,   11,  850],
              [1800,   10,  760],
              [2000,   12,  800],
              [2300,   11,  810]]
col_standardized = scale(pizza_data)  # Standardizing each column of pizza_data
# [[-0.16552118 -1.06904497 -0.1393466]
# [ 1.4896906   0.26726124  1.60248593]
# [-1.40693001 -1.06904497 -1.53281263]
# [-0.57932412  1.60356745 -0.1393466]
# [ 0.66208471  0.26726124  0.2090199]]
col_means = col_standardized.mean(axis=0).round(decimals=3)  # Column means (rounded to nearest thousandth)
# [ 0. -0.  0.]
col_stds = col_standardized.std(axis=0)  # Column standard deviations
# [1., 1., 1.]

# Example
# This function will standardize the input NumPy array, data, by using the scale function.
# Input: [[2000  900  100  700]
#         [ 900  410   39  344]
#         [1232  560   67  400]
#         [4012 2032  199 1512]]
def standardize_data(data):
  scaled_data = scale(data)
  return scaled_data
# Output: [[-0.02978671 -0.11884522 -0.02068678 -0.08362497]
#          [-0.93993628 -0.89015859 -1.03020176 -0.84697085]
#          [-0.66523659 -0.65404225 -0.56681784 -0.72689397]
#          [ 1.63495958  1.66304607  1.61770638  1.65748979]]