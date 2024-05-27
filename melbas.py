import numpy as np
from keras.models import Sequential
from keras.layers import Dense, Dropout
from keras.applications import DenseNet121
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from keras.optimizers import Adam
from PIL import Image
from sklearn.utils import shuffle
import os

ben = os.listdir('D:\ISIC_2019_Training_Input\Melanoma')
mal = os.listdir('D:\ISIC_2019_Training_Input\Basal_cell_carcinoma')

ben

len(ben)

mal

len(mal)

ben = ben[:1000]
ben
len(ben)
mal = mal[:1000]
mal
len(mal)
# Let benign be 0 and malignant be 1
train = []
train_y = []
import cv2
samples_per_category = 100
for i in ben:
    x = 'D:\ISIC_2019_Training_Input\Melanoma' + "\\" + str(i)
    if not os.path.exists(x):
        print(f"Error: Image file '{x}' not found.")
        continue
    img = cv2.cvtColor(cv2.imread(x), cv2.COLOR_BGR2RGB)
    img = cv2.resize(img,(200,200))
    img = img/255 # normalising 
    train.append(img.flatten())
    # train.append(x)
    train_y.append(0)
for i in mal:
    x = 'D:\ISIC_2019_Training_Input\Basal_cell_carcinoma' + "\\" + str(i)
    if not os.path.exists(x):
        print(f"Error: Image file '{x}' not found.")
        continue
    img = cv2.imread(x)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    img = cv2.resize(img,(200,200))
    img = img/255 # normalising 
    train.append(img.flatten())
    train_y.append(1)
print("Length of images :- ", len(train))
print("Length of lables :- ", len(train_y))
train = np.array(train)
from sklearn.model_selection import train_test_split
train,val,train_y,val_y = train_test_split(train,train_y,test_size=0.2,random_state=44)
train = train.reshape(train.shape[0],200,200,3)
val = val.reshape(val.shape[0],200,200,3)
from sklearn.preprocessing import LabelEncoder
encoder = LabelEncoder()
encoder = encoder.fit(train_y)
train_y = encoder.transform(train_y)
encoder = encoder.fit(val_y)
val_y = encoder.transform(val_y)
print(str('training rows ' + str(len(train))))
print(str('validation rows ' + str(len(val))))
model = Sequential()
from tensorflow.keras.applications import Xception
from tensorflow.keras.layers import Dense, Conv2D, Flatten, Dropout, MaxPooling2D
from tensorflow.keras.callbacks import ReduceLROnPlateau,EarlyStopping
# Create CNN model
model = Sequential()
model.add(Conv2D(32, (3, 3), activation='relu', input_shape=(200, 200, 3)))
model.add(MaxPooling2D((2, 2)))
model.add(Conv2D(64, (3, 3), activation='relu'))
model.add(MaxPooling2D((2, 2)))
model.add(Conv2D(128, (3, 3), activation='relu'))
model.add(MaxPooling2D((2, 2)))
model.add(Conv2D(128, (3, 3), activation='relu'))
model.add(MaxPooling2D((2, 2)))
model.add(Flatten())
model.add(Dense(512, activation='relu'))
model.add(Dense(1, activation='sigmoid'))
model.summary()
model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])
# Data augmentation
datagen = ImageDataGenerator(
    rotation_range=20,
    width_shift_range=0.2,
    height_shift_range=0.2,
    horizontal_flip=True
)
datagen.fit(train)
from keras.callbacks import ModelCheckpoint
# Checkpoint to save the best model
checkpoint = ModelCheckpoint('best_model.keras', monitor='val_loss', save_best_only=True, mode='auto')
# Train the model
history = model.fit(
    datagen.flow(train, train_y, batch_size=32),
    epochs=10,
    validation_data=(val, val_y),
    callbacks=[checkpoint]
)
# Evaluate the model
test_loss, test_acc = model.evaluate(val, val_y)
print('Test accuracy:', test_acc)
model.save("new_model.h5")
import matplotlib.pyplot as plt
print(history.history.keys())
plt.plot(history.history['val_accuracy'])
# Plot validation accuracy
plt.plot(history.history['val_accuracy'])
plt.xlabel('Epochs')
plt.ylabel('Validation Accuracy')
plt.title('Validation Accuracy Over Epochs')
plt.show()
# Make predictions
predictions = model.predict(val)
accuracy = 0
for prediction, actual in zip(predictions, val_y):
    predicted_class = np.argmax(prediction)
    actual_class = np.argmax(actual)
    if(predicted_class == actual_class):
        accuracy += 1

accuracy = (accuracy / len(val_y))*100

B = "Testing Accuracy is {0}".format(accuracy)

# Print the test loss and accuracy
print("Test Loss:", test_loss)
print("Test Accuracy:", test_acc)
from sklearn.metrics import confusion_matrix
import seaborn as sns

# Load the best model
from keras.models import load_model
best_model = load_model('new_model.h5')# Make predictions on the test data
y_pred = best_model.predict(val)
y_pred_classes = np.argmax(y_pred, axis=1)
# Convert one-hot encoded labels back to categorical labels
y_true_classes = np.argmax(val_y)
y_pred_classes
from keras.models import load_model
import numpy as np
from PIL import Image
def preprocess_image(image_path):
    img = Image.open(image_path)
    img = img.resize((200, 200))  # Resize image to match the input size of the model
    img = np.array(img) / 255.0  # Normalize pixel values
    img = img.reshape((1, 200, 200, 3))  # Reshape to match the input shape of the model
    return img
sample_image_path = r"C:\Users\User\Downloads\basalCellCarcinomaBCC_6163_lg.webp"
sample_image = preprocess_image(sample_image_path)
predictions = best_model.predict(sample_image)
if predictions[0][0] > 0.5:
    print("Basal Cell Carcinoma (BCC)")
else:
    print("Melanoma")
list(set(train_y))