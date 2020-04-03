from PIL import Image
from sklearn import datasets, metrics
from sklearn.linear_model import Perceptron
import numpy as np
import os
import matplotlib.pyplot as plot

tab = ["..\\data-mining\\testimages\\" + x for x in os.listdir("..\\data-mining\\testimages") if "png" in x.lower() or "jpeg" in x.lower()]

digits = datasets.load_digits()
training_size = int(digits.images.shape[0] / 2)
training_images = []
for elem in tab:
    training_images.append(Image.open(elem).convert('F'))
# training_images = digits.images[0:training_size]
# training_images = training_images.reshape((training_images.shape[0], -1))
training_target = digits.target[0:training_size]
classifier = Perceptron(max_iter=1000)

# training
for i in range(training_size):
    training_data = np.array(training_images[i])
    training_data = training_data.reshape(1, -1)
    classifier.partial_fit(training_data, [training_target[i]], classes=np.unique(digits.target))

# prediction
predict_images = digits.images[training_size + 1:]
actual_labels = digits.target[training_size + 1:]
predicted_labels = classifier.predict(predict_images.reshape((predict_images.shape[0], -1)))

# classification report
print(metrics.classification_report(actual_labels, predicted_labels))
