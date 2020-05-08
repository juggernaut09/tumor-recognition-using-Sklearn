from data import test
from model import model


predictions = model.predict(test)
print(predictions)