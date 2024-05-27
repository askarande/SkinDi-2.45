from common import *

def openimage():
   
    global fn
    # Inside the openimage function, the askopenfilename function from the tkinter library opens a file dialog, allowing the user to select an image file.
    fileName = askopenfilename(initialdir='/dataset', title='Select image for Aanalysis ',
                               filetypes=[("all files", "*.*")])
    
    IMAGE_SIZE=300
    imgpath = fileName
    fn = fileName

    img = Image.open(imgpath)
    img = img.resize((IMAGE_SIZE,IMAGE_SIZE))
    img = np.array(img)

    im = Image.fromarray(img)
    imgtk = ImageTk.PhotoImage(image=im)

    return imgtk, fn

    # img = tk.Label(root, image=imgtk, height=230, width=250)
    
    # imgupld.place_forget()

    # img.image = imgtk
    # img.place(x=int(w*(25/100)), y=int(h*(15/100)))

    # button_select_image.config(state=tk.DISABLED)