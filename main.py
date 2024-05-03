# This is a sample Python script.

# Press Umschalt+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import tkinter as tk
from tkinter import messagebox
from PIL import Image

def open_image():
    image_path = r"C:\Users\Thomas\Pictures\Bewerbungsbilder\ThomasBewerbung.jpg"
    img = Image.open(image_path)
    img.show()

def show_text():
    file_path = r"C:\Users\Thomas\Desktop\NetzwerkConfig.txt"
    with open(file_path, 'r') as file:
        surprise_text = file.read()
    messagebox.showinfo("Surprise Text", surprise_text)

def terminate_app():
    root.destroy()

root = tk.Tk()
root.title("Welcome")
root.geometry("300x200")

welcome_label = tk.Label(root, text="Welcome!", font=("Comic Sans MS", 20))
welcome_label.pack(pady=10)

image_button = tk.Button(root, text="Show Surprise Image", font=("Comic Sans MS", 15), command=open_image)
image_button.pack(pady=10)

text_button = tk.Button(root, text="Show Surprise Text", font=("Comic Sans MS", 15), command=show_text)
text_button.pack(pady=10)

terminate_button = tk.Button(root, text="Terminate", font=("Comic Sans MS", 15), command=terminate_app)
terminate_button.pack(pady=10)

root.mainloop()