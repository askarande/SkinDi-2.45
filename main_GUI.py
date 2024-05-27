import os
os.environ['TF_ENABLE_ONEDNN_OPTS'] = '0'

from common import *
from GUI_functions import *
import camera_img
import open_img

img3 = None 
label_grey = None
button_clear = None
result_label = None
button4 = None

def home():
    root.destroy()
    call(["python", r"C:\Users\User\OneDrive\Documents\Custom Office Templates\New folder\SkinDi 2.44\Gui_main.py"])

def res():
    print("\nRes function calling\n")
    call(["python", r"histogram.py"])  
    print("Way off towards x.py\n\n")  

def funcam():
    global fn, img, button_clear, button_image_preprocess
    imgupld.place_forget()
    img, fn = camera_img.camimg()
    print("Camera fn :- ",fn)

    im = Image.fromarray(img)
    imgtk = ImageTk.PhotoImage(image=im)
    img = tk.Label(root, image=imgtk, height=250, width=250)
    img.image = imgtk
    img.place(x=int(w*(25/100)), y=int(h*(15/100)))
    button_select_image.config(state=tk.DISABLED)
    button_image_preprocess.config(state=tk.NORMAL)
    button_clear = tk.Button(frame_process, text="Clear", command=clr, width=18, height=1, font=('Concert One', 15, ' bold '),bg="black",fg="white")
    button_clear.place(x=10, y=330)

def funopn():
    global fn, img, button_clear, button_image_preprocess
    imgupld.place_forget()
    imgtk, fn = open_img.openimage()
    print("\nFile fn :- " + fn + "\n")
    img = tk.Label(root, image=imgtk, height=230, width=250)
    img.image = imgtk
    img.place(x=int(w*(25/100)), y=int(h*(15/100)))
    button_select_image.config(state=tk.DISABLED)
    button_image_preprocess.config(state=tk.NORMAL)
    button_clear = tk.Button(frame_process, text="Clear", command=clr, width=18, height=1, font=('Concert One', 15, ' bold '),bg="black",fg="white")
    button_clear.place(x=10, y=330)

def funtst():
    global fn, result_label, button4, root
    print("funtst fn :- " + fn + "\n")
    msg, fn2 = test_model(fn)
    print("\nmsg :- ", msg)

    # result_text = Text(root, width=27, height=10, font=("bold", 25), bg="black", fg="white")
    # result_text.insert(tk.END, msg)
    # result_text.place(x=380, y=h-200)

    # start_idx = msg.find('Selected Image is')
    # end_idx = msg.find('Image Testing Completed..') + len('Image Testing Completed..')
    # result_text.tag_add("color", f"1.0 + {start_idx} chars", f"1.0 + {end_idx} chars")
    # result_text.tag_config("color", foreground="red")


    result_label = tk.Label(root, text=msg, width=27, font=("bold", 25), bg='black', fg='white')
    result_label.place(x=380, y=h-200)

    print("Button is visible")

    button4 = tk.Button(root, text="Display Histogram", command=res, width=15, height=1,bg="red",fg="black", font=('times', 15, ' bold '))
    button4.place(x=w-350, y=h-160)

    print("Button is clicked")


def fungry():
    global fn, label_grey, img3
    gs, threshold = convert_grey(fn)
    
    # Display grayscale image
    img_grey = Image.fromarray(gs)
    imgtk_grey = ImageTk.PhotoImage(image=img_grey)
    label_grey = tk.Label(root, image=imgtk_grey, height=230, width=230,bg='white')
    label_grey.image = imgtk_grey
    label_grey.place(x=int(w*(45/100)), y=int(h*(15/100)))

    # Display binary threshold image
    im = Image.fromarray(threshold)
    imgtk = ImageTk.PhotoImage(image=im)
    img3 = tk.Label(root, image=imgtk, height=230, width=230)
    img3.image = imgtk
    img3.place(x=int(w*(35/100)), y=int(h*(48/100)))
    button_image_preprocess.config(state=tk.DISABLED)
    button_prediction.config(state=tk.NORMAL)


def show_upload_options():
    imgupld.place(x=int(w*(32/100)), y=int(h*(15/100)))
    
def hide_upload_options():
    imgupld.place_forget()

def window():
    root.destroy()

# Create the main application window
def init_gui():
    root = tk.Tk()
    root.configure(background="#BFEFFF")
    return root

def create_gui():
    global root, imgupld, button_select_image, w, h, frame_process, button_image_preprocess, button_prediction
    root = init_gui()
    # root = tk.Tk()
    # root.configure(background="seashell2")
    w, h = root.winfo_screenwidth(), root.winfo_screenheight()  # These lines get the screen width and height of the user's display.
    print("width :- ", w)
    print("height :- ", h)
    root.geometry(f"{w}x{h}+0+0")
    root.title("Skin Disease Detection System")

    # Set up the background image
    image2 = Image.open('white.jpg')  # Adjust this line to the correct image path
    image2 = image2.resize((w, h), Image.LANCZOS)
    background_image = ImageTk.PhotoImage(image2)
    background_label = tk.Label(root, image=background_image)
    background_label.place(x=0, y=0)

    frame_top = tk.LabelFrame(root, width=1280, height=80, bd=0, bg="#804ecc")
    frame_top.place(x=0, y=0, width=w, height=h*(9/100))

    lbl = tk.Label(frame_top, text="Skin Disease Detection System", font=('Concert One', int(h*(3.75/100)), 'bold'), bg="#804ecc", fg="white")
    lbl.pack(side=tk.LEFT, padx=20, expand=True)  # Use LEFT to align it on the left

    button_logout = tk.Button(frame_top, text=" Log Out ", command=home, width=7, height=1, font=('Concert One', 15, 'bold'), bg="red", fg="white")
    button_logout.pack(side=tk.RIGHT, padx=20)  # RIGHT to align it on the right

    frame_process = tk.LabelFrame(root, text=" --Process--", width=int(w*(19/100)), height=int(h*(58/100)), bd=5, font=('Concert One', 14, 'bold'), bg="#804ecc", fg="white")
    frame_process.place(x=w*(3/100), y=h*(14/100))

    button_select_image = tk.Button(frame_process, text=" Select Image ", command=show_upload_options, width=18, height=1, font=('Concert One', 15, 'bold'), bg="white", fg="black")
    button_select_image.place(x=int((w*(19/100)) * (4/100)), y=50)

    button_image_preprocess = tk.Button(frame_process, text="Image Preprocess", command=fungry, width=18, height=1, font=('Concert One', 15, 'bold'), bg="white", fg="black")
    button_image_preprocess.place(x=int((w*(19/100)) * (4/100)), y=120)

    button_prediction = tk.Button(frame_process, text="CNN Prediction", command=funtst, width=18, height=1, font=('Concert One', 15, 'bold'), bg="white", fg="black")
    button_prediction.place(x=int((w*(19/100)) * (4/100)), y=190)

    button_exit = tk.Button(frame_process, text="Exit", command=window, width=18, height=1, font=('Concert One', 15, ' bold '),bg="red",fg="white")
    button_exit.place(x=10, y=380)

    imgupld = tk.LabelFrame(root, width=00, height=00, bd=3, bg="white", highlightthickness=1, highlightbackground="black")
    # imgupld.place(x=int(w*(32/100)), y=int(h*(15/100)))

    # Text for upload from device and capture from camera buttons
    upld_dvc_text = "Upload Image\nfrom Device"
    upld_cmr_text = "Capture Image\nfrom Camera"

    # def btnbg():
    img2 = Image.open("uplddvcimg2.jpg")    
    img2 = img2.resize((300, 230), Image.LANCZOS)
    img2 = ImageTk.PhotoImage(img2)

    img3 = Image.open("upldcamimg2.jpg")    
    img3 = img3.resize((300, 230), Image.LANCZOS)
    img3 = ImageTk.PhotoImage(img3)

    uplddvc = tk.Button(imgupld, text=upld_dvc_text, image=img2, command=funopn, width=200, height=200, font=('times', 15, ' bold '),fg="black")
    uplddvc.pack(side=tk.LEFT, padx=10, pady=5)

    upldcmr = tk.Button(imgupld, text=upld_cmr_text, image=img3, command=funcam, width=200, height=200, font=('times', 15, ' bold '),fg="black")
    upldcmr.pack(side=tk.LEFT, padx=10, pady=5)

    msg2 = """
Our project utilizes Convolutional Neural Networks (CNNs) \nto develop an advanced skin cancer detection system \ncapable of accurately predicting the presence of Malignant, \nBenign, Melanoma, and Basal Cell Carcinoma.

    Skin Cancer Overview:
    • Skin cancer is the abnormal growth of skin cells due to\n  exposure to UV radiation.
    • It's the most common type of cancer worldwide, but can be\n  highly treatable when detected early.

    Malignant vs. Benign Tumors:
    • Malignant tumors are cancerous and can invade nearby\n  tissues and spread to other parts of the body.
    • Benign tumors are non-cancerous and don't invade nearby\n  tissues.

    Melanoma:
    • Melanoma is the most aggressive form of skin cancer.
    • It develops in melanocytes, the cells that produce melanin.
    • Early detection is crucial as it can spread rapidly.

    Basal Cell Carcinoma:
    • Most common type of skin cancer.
    • It develops in areas exposed to the sun, such as the face\n and  neck.
    • It appears as a waxy bump or a flat, flesh-colored or brown\n  scar-like lesion.
                                                    ***** 
    """

    # Ensure that the frame position + height does not exceed screen height
    frame_height =int(h*(70/100))
    frame_width = int(w*(30/100))
    # print(frame_height, frame_width)
    frame_x = w - frame_width - 20  # Subtract width of the frame and a margin if needed
    frame_y = 80

    if frame_y + frame_height > h:
        frame_y = h - frame_height - 20  # Adjust Y to ensure the frame stays within the screen

    frame_info = tk.LabelFrame(root, text=" --Information--", width=frame_width, height=frame_height, bd=5,
                                font=('Concert One', 14, 'bold'), bg="white", fg="black")
    frame_info.place(x=frame_x, y=frame_y)

    result_label = tk.Label(frame_info, text=msg2, justify='left', width=0, font=('Concert One', int((frame_height + frame_width)*(1.20/100))), bg='white', fg='black')
    result_label.place(x=4, y=0)

    button_image_preprocess.config(state=tk.DISABLED)
    button_prediction.config(state=tk.DISABLED)

    root.mainloop()

# def clr():
#     global img, img3, label_grey, button_clear
#     print("clr")
#     button_select_image.config(state=tk.NORMAL)
#     img.place_forget()
#     # if img3.winfo_exists() and img3.winfo_ismapped():
#     if img3.winfo_ismapped():
#         img3.place_forget()

#     if label_grey.winfo_ismapped():
#         label_grey.place_forget()

#     result_label.place_forget()
#     button4.place_forget()
#     # button_clear.place_forget()

def clr():
    global img, img3, label_grey, button_clear, result_label, button4
    print("clr")
    button_select_image.config(state=tk.NORMAL)
    button_image_preprocess.config(state=tk.DISABLED)
    button_prediction.config(state=tk.DISABLED)
    img.place_forget()
    if img3 is not None:
        img3.place_forget()
    if label_grey is not None:
        label_grey.place_forget()
    if result_label is not None:
        result_label.place_forget()
    if button4 is not None:
        button4.place_forget()
    if button_clear is not None:
        button_clear.place_forget()



