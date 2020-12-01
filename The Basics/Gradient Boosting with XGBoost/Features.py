import xgboost as xgb
import matplotlib as plt

# Determining important features
model = xgb.XGBClassifier()
model.fit(data, labels)
# Array of feature importances
print('Feature importances:\n{}'.format(
    repr(model.feature_importances_)))

# Plotting important features

# F-scores with default(weight)
model = xgb.XGBRegressor()
model.fit(data, labels)
xgb.plot_importance(model)
plt.show()  # matplotlib plot

# F-scores with different importance metric(Information gain)
model = xgb.XGBRegressor()
model.fit(data, labels)
xgb.plot_importance(model, importance_type='gain')
plt.show() # matplotlib plot

# Not displaying the exact F-score next to each bar
model = xgb.XGBRegressor()
model.fit(data, labels)
xgb.plot_importance(model, show_values=False)
plt.savefig('importances.png') # save to PNG file