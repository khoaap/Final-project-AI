# Load data and split
from joblib import dump
import matplotlib.pyplot as plt
from sklearn.metrics import confusion_matrix
from sklearn.metrics import classification_report
from sklearn.neighbors import KNeighborsClassifier
from keras.datasets import mnist
(train_X, train_y), (test_X, test_y) = mnist.load_data()

# Data preprocessing
# change the size of the array
train_X = train_X.reshape(train_X.shape[0], train_X.shape[1]*train_X.shape[2])
# change the size of the array
test_X = test_X.reshape(test_X.shape[0], test_X.shape[1]*test_X.shape[2])

# Create and train kNN model with k = 5
knn = KNeighborsClassifier(n_neighbors=5)  # create model
knn.fit(train_X, train_y)  # training
y_pred = knn.predict(test_X)  # test on test_X

# Result evaluation
print("matrix:\n", confusion_matrix(test_y, y_pred))
print("report:\n", classification_report(test_y, y_pred))


# model evaluation using matplotlib.pyplot
train_acc = knn.score(train_X, train_y)
test_acc = knn.score(test_X, test_y)

# plot bar chart showing training and test accuracy
fig, ax = plt.subplots()
plt.ylim(0.0, 1.0)
ax.bar(['Training', 'Test'], [train_acc, test_acc])
ax.set_ylabel('Accuracy')
ax.set_title('KNN Classifier Accuracy')
plt.show()

# Save model to file
dump(knn, 'Model_Knn.joblib')
