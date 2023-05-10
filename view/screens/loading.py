import tkinter as tk
from PIL import Image, ImageTk
import pygame


def show_loading_screen(window):
    window.withdraw()  # Hide the main window

    # Get display info
    pygame.display.init()
    vinfo = pygame.display.Info()

    # Create and display the loading window
    loading_window = tk.Toplevel(window)
    loading_window.overrideredirect(True)  # Remove window borders
    loading_window.geometry(f"426x240+{vinfo.current_w // 2 - 213}+{vinfo.current_h // 2 - 120}")

    # Gather frames of the loading GIF
    welcome_image = Image.open("assets/images/loading.gif")
    frames = []
    try:
        while True:
            welcome_image.seek(len(frames))
            frame = welcome_image.copy()
            frames.append(frame)
    except EOFError:
        pass

    # Make canvas
    canvas = tk.Canvas(loading_window, width=frames[0].width, height=frames[0].height)
    canvas.pack()

    # Display each frame in the canvas
    for frame in frames:
        photo = ImageTk.PhotoImage(frame)
        canvas.create_image(0, 0, anchor='nw', image=photo)
        canvas.update()
        canvas.after(10)

    # Close the loading window and display the main window
    loading_window.destroy()
    window.deiconify()
