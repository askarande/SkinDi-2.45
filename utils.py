# utils.py

import tkinter as tk
from tkinter.filedialog import askopenfilename
from PIL import Image, ImageTk
from subprocess import call
import pygame
import pygame.camera
from main_GUI import imgupld
import cv2
import numpy as np

def openimage(root):
   
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

    img = tk.Label(root, image=imgtk, height=230, width=250)
    img.image = imgtk
    img.place(x=30, y=10)

    return fileName

# The convert_grey function also uses the fn variable to load the image, convert it to grayscale, and display the grayscale image.
def convert_grey(root, fn):
    # global fn    

    IMAGE_SIZE=300    
    img = Image.open(fn)
    img = img.resize((IMAGE_SIZE,IMAGE_SIZE))
    img = np.array(img)
    
    x1 = int(img.shape[0])
    y1 = int(img.shape[1])

    gs = cv2.cvtColor(cv2.imread(fn, 1), cv2.COLOR_RGB2GRAY)
    gs = cv2.resize(gs, (x1, y1))

    _, threshold = cv2.threshold(gs, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)

    # Display grayscale image
    img_grey = Image.fromarray(gs)
    imgtk_grey = ImageTk.PhotoImage(image=img_grey)
    label_grey = tk.Label(root, image=imgtk_grey, height=230, width=230,bg='white')
    label_grey.image = imgtk
    label_grey.place(x=700, y=100)

    # Display binary threshold image
    im = Image.fromarray(threshold)
    imgtk = ImageTk.PhotoImage(image=im)
    img3 = tk.Label(root, image=imgtk, height=230, width=230)
    img3.image = imgtk
    img3.place(x=530, y=400)

def camimg(root, imgupld):
    global fn

    # Initialize Pygame
    pygame.init()
    pygame.camera.init()

    # Set the resolution of the camera
    CAMERA_WIDTH = 640
    CAMERA_HEIGHT = 480

    # Create a Pygame window
    screen = pygame.display.set_mode((CAMERA_WIDTH, CAMERA_HEIGHT))
    pygame.display.set_caption("Camera Capture")

    # Get the list of available cameras
    cam_list = pygame.camera.list_cameras()

    # Check if there's at least one camera available
    if cam_list:
        # Create a camera object
        camera = pygame.camera.Camera(cam_list[0], (CAMERA_WIDTH, CAMERA_HEIGHT))
        camera.start()
        
        # Create a font for the button text
        font = pygame.font.Font(None, 36)

        # Main loop
        running = True
        capture_image = False
        while running:
            # Capture an image from the camera
            image = camera.get_image()

            # Display the image on the screen
            screen.blit(image, (0, 0))
            
            # Create a button rectangle
            button_rect = pygame.Rect(10, 10, 100, 50)
            pygame.draw.rect(screen, (255, 0, 0), button_rect)
            
            # Create button text
            text_surf = font.render("Click", True, (255, 255, 255))
            text_rect = text_surf.get_rect(center=button_rect.center)
            screen.blit(text_surf, text_rect)
            
            # Update the display
            pygame.display.flip()
            
            # Event handling
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    # Check if the click is inside the button rectangle
                    if button_rect.collidepoint(event.pos):
                        capture_image = True
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        running = False

            # Save the captured image if the button was clicked
            if capture_image:
                pygame.image.save(image, "captured_image.jpg")
                print("Image captured and saved as 'captured_image.jpg'")
                break  # Exit the loop

    # Stop the camera
    camera.stop()

    # Quit Pygame
    pygame.quit()
    imgupld.place_forget()
    fn = "captured_image.jpg"
    img = Image.open("captured_image.jpg")
    img = img.resize((300,300))
    img = np.array(img)
    
    im = Image.fromarray(img)
    imgtk = ImageTk.PhotoImage(image=im)
    img = tk.Label(root, image=imgtk, height=250, width=250)
    img.image = imgtk
    img.place(x=300, y=100)
    
    print(fn)
