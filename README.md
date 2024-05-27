# SkinDi 2.45

SkinDi 2.45 is an advanced skin disease detection system utilizing Convolutional Neural Networks (CNNs) to accurately predict the presence of various skin conditions. The project focuses on identifying Malignant, Benign, Melanoma, and Basal Cell Carcinoma from images of skin lesions.

## Key Features:
- **Image Preprocessing**: Converts images to grayscale and applies binary thresholding to enhance feature detection.
- **CNN Prediction**: Employs a trained CNN model to classify skin lesions into specific categories.
- **User Interface**: Provides a user-friendly GUI for selecting, preprocessing, and predicting skin diseases from images.
- **Execution Time Display**: Shows the time taken to process and predict the skin condition.
- **Histogram Display**: Visualizes the distribution of pixel intensities in the processed images.

## Usage:
1. **Upload Image**: Users can upload an image from their device or capture one using the system's camera.
2. **Preprocess Image**: Converts the uploaded image to grayscale and applies thresholding for better analysis.
3. **Predict Disease**: The system uses a CNN model to predict the type of skin disease present in the image.
4. **Display Results**: Results are displayed along with the execution time, and users can view the histogram of the image.

## Technologies Used:
- Python
- TensorFlow/Keras
- OpenCV
- Tkinter for GUI
- PIL (Python Imaging Library)


