import tkinter as tk
from tkinter import filedialog
from googletrans import Translator
import time
import io

def translate_srt():
    # Select .srt file
    root = tk.Tk()
    root.iconify()
    filepath = filedialog.askopenfilename(filetypes=[("Subtitle files", "*.srt")])

    # Open .srt file and translate
    with open(filepath, "r") as file:
        lines = file.readlines()
        translator = Translator()
    try: 
        # Translate line by line and display progress
        translated_lines = []
        for i, line in enumerate(lines):
            label["text"] = f"Translating... {i+1}/{len(lines)}"
            root.update()
            translated_line = translator.translate(line, dest='pt').text
            translated_lines.append(translated_line)
    except Exception as e:
        label["text"] = "An error occurred while translating the file. Please try again later."
        root.update()
        root.after(5000,root.destroy)
        return

    # Save the translated .srt file
    if 'eng' in filepath:
        new_filepath = filepath.replace('.eng', '.pt')
    elif 'en' in filepath:
        new_filepath = filepath.replace('.en', '.pt')
    else:
        new_filepath = filepath.replace(".srt",".pt.srt")
    with io.open(new_filepath, "w", encoding='utf-8-sig') as file:
        for i, line in enumerate(translated_lines):
            if i == len(translated_lines) - 1 and line == "\n":
                file.write(line)
            else:
                file.write("\n" + line)
    label["text"] = "Translation complete!"
    time.sleep(5)
    root.destroy()
    
root = tk.Tk()
label = tk.Label(root, text="Select a .srt file to translate")
label.pack()

translate_button = tk.Button(root, text="Translate", command=translate_srt)
translate_button.pack()

def on_closing():
    root.quit()

root.protocol("WM_DELETE_WINDOW", on_closing)
try:
    root.mainloop()
except KeyboardInterrupt:
    root.destroy()
