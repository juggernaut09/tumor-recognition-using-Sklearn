from sklearn.naive_bayes import GaussianNB
from data import train,train_labels

gnb = GaussianNB()
model = gnb.fit(train,train_labels)



