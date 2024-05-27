# GUI_functions.py

from common import *
from model_prediction import test_model_proc

global fn
fn = ""


# The convert_grey function also uses the fn variable to load the image, convert it to grayscale, and display the grayscale image.
def convert_grey(fn):
    # print(fn)
    # global fn    

    IMAGE_SIZE=300
    # print(fn)
    
    img = Image.open(fn)
    img = img.resize((IMAGE_SIZE,IMAGE_SIZE))
    img = np.array(img)
    
    x1 = int(img.shape[0])
    y1 = int(img.shape[1])

    gs = cv2.cvtColor(cv2.imread(fn, 1), cv2.COLOR_RGB2GRAY)
    gs = cv2.resize(gs, (x1, y1))

    _, threshold = cv2.threshold(gs, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)

    return threshold, gs


# Define a function for testing the model
def test_model(fn):
    # global fn
    if fn!="":
        # update_label("Model Testing Start...............")
        start = time.time()
        X=test_model_proc(fn)
        X1="Selected Image is\n {0}".format(X)
        end = time.time()
        ET="Execution Time: {0:.4} seconds \n".format(end-start)
        msg=X1+'\n'+ "Image Testing Completed.." + '\n'+ ET
        fn=""
    else:
        msg="Please Select Image For Prediction...."
    return msg, fn


