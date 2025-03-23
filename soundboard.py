import pygame
import tkinter as tk
from tkinter import filedialog, ttk
import os

# Initialize pygame mixer
pygame.mixer.init()

# Get the directory of the script
script_dir = os.path.dirname(os.path.abspath(__file__))

# Function to play sound
def play_sound(sound_file):
    pygame.mixer.music.load(sound_file)
    pygame.mixer.music.play()

# Function to stop sound
def stop_sound():
    pygame.mixer.music.stop()

# Function to open file dialog and select sound
def add_sound():
    file_path = filedialog.askopenfilename(filetypes=[("Audio Files", "*.mp3 *.wav")])
    if file_path:
        sound_name = os.path.basename(file_path)
        sound_buttons.append((sound_name, file_path))
        organize_tabs()

# Function to load sounds from 'sounds' folder
def load_sounds():
    sounds_folder = os.path.join(script_dir, 'sounds')
    if os.path.exists(sounds_folder) and os.path.isdir(sounds_folder):
        sound_files = [f for f in os.listdir(sounds_folder) if f.endswith(('.mp3', '.wav'))]
        for file_name in sound_files:
            file_path = os.path.join(sounds_folder, file_name)
            sound_buttons.append((file_name, file_path))
        organize_tabs()
    else:
        print("'sounds' folder not found at:", sounds_folder)

# Function to organize sounds into tabs with 10 sounds per tab
def organize_tabs():
    for tab in notebook.tabs():
        notebook.forget(tab)

    num_tabs = (len(sound_buttons) // 10) + (1 if len(sound_buttons) % 10 != 0 else 0)

    for i in range(num_tabs):
        tab_frame = tk.Frame(notebook)
        notebook.add(tab_frame, text=f"Page {i + 1}")
        for sound_name, file_path in sound_buttons[i * 10:(i + 1) * 10]:
            btn = tk.Button(tab_frame, text=sound_name, command=lambda f=file_path: play_sound(f))
            btn.pack(pady=5)

# Set up GUI
root = tk.Tk()
root.title("Simple Soundboard")
root.geometry("400x400")

notebook = ttk.Notebook(root)
notebook.pack(expand=True, fill='both')

sound_buttons = []

add_button = tk.Button(root, text="Add Sound", command=add_sound)
add_button.pack(pady=10)

stop_button = tk.Button(root, text="Stop Sound", command=stop_sound)
stop_button.pack(pady=10)

# Load sounds from 'sounds' folder
load_sounds()

root.mainloop()