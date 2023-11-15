import tkinter as tk
from tkinter import filedialog, messagebox
import os
import numpy as np
import soundfile as sf
import g711

# Version number
VERSION = "1.0.1"

# GUI dimensions
WINDOW_WIDTH = 600
WINDOW_HEIGHT = 50
ENTRY_WIDTH = 60
BUTTON_PADDING_X = 10
BUTTON_PADDING_Y = 5

def convert_files():
    directory = entry.get()
    if directory:
        for filename in os.listdir(directory):
            if filename.lower().endswith(('.mp3', '.ogg', '.webm', '.m4a', '.aifc', '.wav')):
                print(f"Converting: {filename}")
                input_path = os.path.join(directory, filename)
                output_path = os.path.join(directory, filename.rsplit('.', 1)[0] + '_g711.wav')
                data, samplerate = sf.read(input_path)
                encoded_data = g711.encode_alaw(data.astype(np.float32))
                sf.write(output_path, encoded_data, samplerate, format='wav', subtype='PCM_16')
                os.remove(input_path)
        print("Conversion complete")
        convert_button.config(text="Convert", state=tk.NORMAL)

def about_dialog():
    message = f"Cisco Audio File Converter {VERSION}\n\nAuthor: Joshua Dwight\n\nThis app allows you to convert audio files in various formats (MP3, OGG, WEBM, M4A, AIFC, WAV) to the G.711 format used by Cisco systems. To use, enter the directory path, click 'Choose Directory' to select a folder, and click 'Convert' to start the conversion process."
    messagebox.showinfo("About", message)

app = tk.Tk()
app.title(f"Cisco Audio File Converter {VERSION}")
app.geometry(f"{WINDOW_WIDTH}x{WINDOW_HEIGHT}")
app.resizable(False, False)

frame = tk.Frame(app)
frame.pack()

entry = tk.Entry(frame, width=ENTRY_WIDTH)
entry.pack(side=tk.LEFT, padx=BUTTON_PADDING_X, pady=BUTTON_PADDING_Y)

browse_button = tk.Button(frame, text="Choose Directory", command=lambda: entry.insert(tk.END, filedialog.askdirectory()))
browse_button.pack(side=tk.LEFT, padx=BUTTON_PADDING_X, pady=BUTTON_PADDING_Y)

convert_button = tk.Button(frame, text="Convert", command=convert_files)
convert_button.pack(side=tk.LEFT, padx=BUTTON_PADDING_X, pady=BUTTON_PADDING_Y)

menu_bar = tk.Menu(app)
app.config(menu=menu_bar)
about_menu = tk.Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="Help", menu=about_menu)
about_menu.add_command(label=f"About Cisco Audio File Converter {VERSION}", command=about_dialog)

app.mainloop()
