is_clf = True  # for classification
tree = None  # a Decision Trees
data = None
labels = None


def cross_val_score(is_clf, data, laberls, depth, n):
    return None


def cv_decision_tree(is_clf, data, labels,
                     max_depth, cv):
    if is_clf:
        d_tree = tree.DecisionTreeClassifier(max_depth=max_depth)
    else:
        d_tree = tree.DecisionTreeRegressor(max_depth=max_depth)
    scores = cross_val_score(d_tree, data, labels, cv=cv)
    return scores


for depth in range(3, 8):
    # Predefined data and labels
    scores = cv_decision_tree(
        is_clf, data, labels, depth, 5)  # k = 5
    mean = scores.mean()  # Mean acc across folds
    std_2 = 2 * scores.std()  # 2 std devs
    print('95% C.I. for depth {}: {} +/- {:.2f}\n'.format(
        depth, mean, std_2))
