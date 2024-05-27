from common import *

# Create a new Tkinter window
result_window = tk.Tk()
result_window.geometry("1300x700")
result_window.title("Skin Disease Detection Result")

image3 =Image.open('accuracy.png')
background_image1=ImageTk.PhotoImage(image3)
background_label1 = tk.Label(result_window, image=background_image1)
background_label1.image = background_image1
background_label1.place(x=300, y=100)

image4 =Image.open('loss.png')
background_image2=ImageTk.PhotoImage(image4)
background_label2 = tk.Label(result_window, image=background_image2)
background_label2.image = background_image2
background_label2.place(x=700, y=100)

# Run the main event loop for the result window
result_window.mainloop()


