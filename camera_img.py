# camera_img.py

from common import *

def camimg():
    global fn, imgupld  # Assuming fn and imgupld are defined globally
    
    try:
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

        # Update GUI with the captured image
        # imgupld.place_forget()
        fn = "captured_image.jpg"
        img = Image.open("captured_image.jpg")
        img = img.resize((300, 300))
        img = np.array(img)

        return img, fn

        # im = Image.fromarray(img)
        # imgtk = ImageTk.PhotoImage(image=im)
        # img = tk.Label(root, image=imgtk, height=250, width=250)
        # img.image = imgtk
        # img.place(x=300, y=100)

        # print(fn)

    except Exception as e:
        print("Error:", e)
        # Handle the error gracefully, e.g., display an error message box