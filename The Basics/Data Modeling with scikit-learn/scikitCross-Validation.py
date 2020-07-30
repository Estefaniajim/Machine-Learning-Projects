from sklearn import linear_model
from sklearn.model_selection import cross_val_score

# Scored cross-validation

# k = 3
# clf = linear_model.LogisticRegression()
# cv_score = cross_val_score(clf, data, labels, cv=3)
# array([0.93684211, 0.96842105, 0.94179894])

# k = 4
# reg = linear_model.LinearRegression()
# cv_score = cross_val_score(reg, data, labels, cv=4)
# array([0.37548118, 0.49022643, 0.52061242, 0.54864085])