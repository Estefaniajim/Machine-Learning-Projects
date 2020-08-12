from sklearn import tree

# The code below demonstrates how to apply K-Fold CV to tune a decision tree's maximum depth.
is_clf = True  # for classification
for depth in range(3, 8):
    # Predefined data and labels
    scores = cv_decision_tree(
        is_clf, data, labels, depth, 5)  # k = 5
    mean = scores.mean()  # Mean acc across folds
    std_2 = 2 * scores.std()  # 2 std devs
    print('95% C.I. for depth {}: {} +/- {:.2f}\n'.format(
        depth, mean, std_2))
# 95% C.I. for depth 3: 0.9134917106603686 +/- 0.04
# 95% C.I. for depth 4: 0.9166611095674725 +/- 0.08
# 95% C.I. for depth 5: 0.9134370658516253 +/- 0.07
# 95% C.I. for depth 6: 0.910101880151894 +/- 0.04
# 95% C.I. for depth 7: 0.9033787163100861 +/- 0.02

# The function's first argument defines whether the decision tree is for classification/regression,
# the next two arguments represent the data/labels, and the final two arguments represent
# the tree's maximum depth and number of folds, respectively.
def cv_decision_tree(is_clf, data, labels,
                     max_depth, cv):
    if is_clf:
        d_tree = tree.DecisionTreeClassifier(max_depth=max_depth)
    else:
        d_tree = tree.DecisionTreeRegressor(max_depth=max_depth)
    scores = cross_val_score(d_tree, data, labels, cv=cv)
    return scores