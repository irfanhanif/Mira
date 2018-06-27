import numpy as np
import pickle

from sklearn import metrics
from keras.models import load_model

data_path = "data_target/"

X = np.load(data_path + "X.npy")
Y = np.load(data_path + "Y.npy")
X_test = np.load(data_path + "X_test.npy")
Y_test = np.load(data_path + "Y_test.npy")

X = np.expand_dims(X, axis=2)
X_test = np.expand_dims(X_test, axis=2)

mdl = str(raw_input("Choose model: [1]WTL [2]TL1 [3]TL2: "))
if mdl == "1":
    print "Load CNN without transfer learning..."
    model_path = "FinalModel/data-target-model-wtl.h5"
elif mdl == "2":
    print "Load CNN Transfer Learning 1..."
    model_path = "FinalModel/data-target-model-tl-1.h5"
elif mdl == "3":
    print "Load CNN Transfer Learning 2..."
    model_path = "FinalModel/data-target-model-tl-2.h5"
else:
    print "Load CNN Transfer Learning 2..."
    model_path = "FinalModel/data-target-model-tl-2.h5"

model = load_model(model_path)

predictions = model.predict(X_test)
predictions = [np.argmax(predictions[i]) for i in range(len(predictions))]
predictions = np.array(predictions)
labels = [np.argmax(Y_test[i]) for i in range(len(Y_test))]
labels = np.array(labels)

print predictions
print labels

print "Accuracy: " + str(100*metrics.accuracy_score(labels, predictions))
print "Precision: " + str(100*metrics.precision_score(labels, predictions, average="weighted"))
print "Recall: " + str(100*metrics.recall_score(labels, predictions, average="weighted"))
print "f1_score: " + str(100*metrics.f1_score(labels, predictions, average="weighted"))

print model.summary()
print model.evaluate(X_test, Y_test, batch_size=32)
