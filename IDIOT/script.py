import tkinter as tk
from tkinter import PhotoImage
import webbrowser
import os

# Function to open the website
def open_website():
    webbrowser.open("https://youareanidiot.cc/")  # Replace with your desired URL

# Create the main window
root = tk.Tk()
root.title("Clickable Folder")
root.geometry("300x300")

# Load a folder icon image
folder_icon_path = "folder.png"  # Make sure this image exists in the same directory
if not os.path.exists(folder_icon_path):
    print("Put a folder.png image in the same directory.")
    exit()

folder_icon = PhotoImage(file=folder_icon_path)

# Create a button with the folder image
folder_button = tk.Button(root, image=folder_icon, command=open_website, borderwidth=0)
folder_button.pack(pady=80)

# Run the application
root.mainloop()
