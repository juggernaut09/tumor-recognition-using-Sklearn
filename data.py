from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split

data = load_breast_cancer()

features = data['data']
labels = data['target']

#Organize the data into train

train, test, train_labels, test_labels = train_test_split(features,labels,test_size= 0.33, random_state= 42)
