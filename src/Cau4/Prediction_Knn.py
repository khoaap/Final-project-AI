import os
from PIL import Image
import numpy as np

image_list = [] #test data list

#Load data from folder
path = '5_input_samples/'
for filename in os.listdir(path):
    img = Image.open(path+filename).convert('L') #convert to grayscale
    img_data = np.asarray(img).reshape(-1) #reshape to 2D array
    image_list.append(img_data)

#print img to the screen
import matplotlib.pyplot as plt
for i in range(5):
    plt.imshow(np.asarray(image_list[i]).reshape(28,28), cmap='gray')
    plt.show()

#Load model from file
from joblib import load
knn = load('Model_Knn.joblib')

# Perform prediction on test data
y_pred = knn.predict(image_list)
print("Predictions:", y_pred)