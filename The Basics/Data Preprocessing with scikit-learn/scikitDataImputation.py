from sklearn.impute import SimpleImputer
from numpy import nan

# Data imputation methods
data = [[ 1.,  2., nan,  2.],
       [ 5., nan,  1.,  2.],
       [ 4., nan,  3., nan],
       [ 5.,  6.,  8.,  1.],
       [nan,  7., nan,  0.]]
imp_mean = SimpleImputer()
transformed = imp_mean.fit_transform(data)
# [[1.  , 2.  , 4.  , 2.  ],
#  [5.  , 5.  , 1.  , 2.  ],
#  [4.  , 5.  , 3.  , 1.25],
#  [5.  , 6.  , 8.  , 1.  ],
#  [3.75, 7.  , 4.  , 0.  ]]
imp_median = SimpleImputer(strategy='median')
transformed = imp_median.fit_transform(data)
# [[1. , 2. , 3. , 2. ],
#  [5. , 6. , 1. , 2. ],
#  [4. , 6. , 3. , 1.5],
#  [5. , 6. , 8. , 1. ],
#  [4.5, 7. , 3. , 0. ]]
imp_frequent = SimpleImputer(strategy='most_frequent')
transformed = imp_frequent.fit_transform(data)
# [[1., 2., 1., 2.],
#  [5., 2., 1., 2.],
#  [4., 2., 3., 2.],
#  [5., 6., 8., 1.],
#  [5., 7., 1., 0.]]
imp_constant = SimpleImputer(strategy='constant',
                             fill_value=-1)
transformed = imp_constant.fit_transform(data)
# [[ 1.,  2., -1.,  2.],
#  [ 5., -1.,  1.,  2.],
#  [ 4., -1.,  3., -1.],
#  [ 5.,  6.,  8.,  1.],
#  [-1.,  7., -1.,  0.]]