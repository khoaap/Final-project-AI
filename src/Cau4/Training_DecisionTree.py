#Load data and split
from keras.datasets import mnist
(train_X, train_y), (test_X, test_y) = mnist.load_data()

#Data preprocessing
train_X = train_X.reshape(train_X.shape[0], train_X.shape[1]*train_X.shape[2]) #change the size of the array
test_X = test_X.reshape(test_X.shape[0], test_X.shape[1]*test_X.shape[2]) #change the size of the array

# # Create and train  Decision Tree model
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score
dt = DecisionTreeClassifier() #create model
dt.fit(train_X, train_y) #training
y_pred = dt.predict(test_X) #test on test_X

#Result evaluation
accuracy = accuracy_score(test_y, y_pred)
from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix
print("matrix:\n",confusion_matrix(test_y,y_pred))
print("report:\n",classification_report(test_y,y_pred))
print("Accuracy:", accuracy.round(2))


# model evaluation using matplotlib.pyplot
import matplotlib.pyplot as plt
train_acc = dt.score(train_X, train_y)
test_acc = dt.score(test_X, test_y)

# plot bar chart showing training and test accuracy
fig, ax = plt.subplots()
plt.ylim(0.0, 1.0)
ax.bar(['Training', 'Test'], [train_acc, test_acc])
ax.set_ylabel('Accuracy')
ax.set_title('Decision Tree Classifier Accuracy')
plt.show()


#Save model to file
from joblib import dump
dump(dt, 'Model_DecisionTree.joblib')

# Visualization of decision trees
from sklearn import tree
fig, ax = plt.subplots(figsize=(50, 30))
tree.plot_tree(dt, ax=ax)
plt.show()