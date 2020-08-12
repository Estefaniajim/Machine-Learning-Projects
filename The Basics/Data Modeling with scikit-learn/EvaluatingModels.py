from sklearn import tree, metrics

# The code below shows an example of making predictions with a regression decision tree.
reg = tree.DecisionTreeRegressor()
# predefined train and test sets
reg.fit(train_data, train_labels)
predictions = reg.predict(test_data)

# The code below evaluates a regression model's predictions based on the testing labels.
r2 = metrics.r2_score(test_labels, predictions)
print('R2: {}\n'.format(r2))
mse = metrics.mean_squared_error(
  test_labels, predictions)
print('MSE: {}\n'.format(mse))
mae = metrics.mean_absolute_error(
  test_labels, predictions)
print('MAE: {}\n'.format(mae))
# R2: 0.6898739990448138
# MSE: 27.813149606299206
# MAE: 3.588188976377953

# The code below evaluates a classification model's predictions based on the testing labels.
clf = tree.DecisionTreeClassifier()
# predefined train and test sets
clf.fit(train_data, train_labels)
predictions = clf.predict(test_data)
acc = metrics.accuracy_score(test_labels, predictions)
print('Accuracy: {}\n'.format(acc))
# Accuracy: 0.8811188811188811