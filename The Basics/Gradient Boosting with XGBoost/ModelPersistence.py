from sklearn import svm
from sklearn import datasets
import pickle
from joblib import dump, load

clf = svm.SVC()
X, y= datasets.load_iris(return_X_y=True)
clf.fit(X, y)

s = pickle.dumps(clf)
clf2 = pickle.loads(s)
clf2.predict(X[0:1])
dump(clf, 'filename.joblib')
clf = load('filename.joblib')