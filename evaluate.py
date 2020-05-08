from data import test_labels
from predict import predictions
from sklearn.metrics import accuracy_score

accuracy = accuracy_score(test_labels,predictions)
print(accuracy)
