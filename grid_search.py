from sklearn.model_selection import GridSearchCV
from sklearn import svm, datasets


iris = datasets.load_iris()

X = iris.data

y = iris.target


# model
model = svm.SVC()
# grid
parameters = {'kernel': ['linear', 'rbf'], 'C': [1, 10]}

# Perform grid search with cross-validation
grid_search = GridSearchCV(model, parameters, cv=5)
grid_search.fit(X, y)

# Print the best hyperparameters and the corresponding accuracy
print("Best Hyperparameters: ", grid_search.best_params_)
print("Best Accuracy: ", grid_search.best_score_)
