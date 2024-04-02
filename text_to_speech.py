import os
import tkinter as tk
from tkinter import scrolledtext, messagebox

import requests
import chunk_service
import tts_service
import pygame
import pyperclip

def display_chunks(chunks, frame):
    for widget in frame.winfo_children():
        widget.destroy()

    for i, chunk in enumerate(chunks, start=1):
        chunk_text = tk.Text(frame, height=4, width=50)
        chunk_text.insert(tk.END, chunk)
        chunk_text.grid(row=i, column=0, padx=10, pady=5)
        chunk_text.configure(state='disabled')

        copy_button = tk.Button(frame, text="Copy Chunk", command=lambda c=chunk: pyperclip.copy(c))
        copy_button.grid(row=i, column=1, padx=10)

        chunk_size = str(len(chunk))
        size_label = tk.Label(frame, text=chunk_size)
        size_label.grid(row=i, column=2, padx=10)

        copy_size_button = tk.Button(frame, text="Copy Size", command=lambda s=chunk_size: pyperclip.copy(s))
        copy_size_button.grid(row=i, column=3, padx=10)

        mp3_button = tk.Button(frame, text="MP3", command=lambda c=chunk, cs=chunk_size: generate_audio(c, cs, frame, i))
        mp3_button.grid(row=i, column=4, padx=10)

def download_file(url, filename):
    """Download an MP3 file and save it to a specific path."""
    response = requests.get(url)
    with open(filename, 'wb') as f:
        f.write(response.content)

def generate_audio(chunk, chunk_size, frame, row):
    mp3_url = tts_service.make_tts_request(chunk, chunk_size)
    if mp3_url:
        # Ensure mp3 directory exists
        if not os.path.exists('mp3'):
            os.makedirs('mp3')

        # Filename example: 'mp3/audio_chunk_1.mp3'
        filename = f"mp3/audio_chunk_{row}.mp3"
        download_file(mp3_url, filename)

        play_button = tk.Button(frame, text="Play", command=lambda: play_audio_clip(filename))
        play_button.grid(row=row, column=5, padx=10)
    else:
        messagebox.showerror("Error", "Failed to generate audio.")

def play_audio_clip(file_path):
    pygame.mixer.init()
    pygame.mixer.music.load(file_path)
    pygame.mixer.music.play()

def generate_button_click(text_area, frame):
    text = text_area.get("1.0", tk.END)
    chunks = chunk_service.generate_chunks(text)
    display_chunks(chunks, frame)

def main():
    root = tk.Tk()
    root.title("Text Chunker and TTS")  # Updated title

    main_frame = tk.Frame(root)
    main_frame.pack(fill=tk.BOTH, expand=True)

    text_area = scrolledtext.ScrolledText(main_frame, height=10)
    text_area.pack(padx=10, pady=5)

    generate_button = tk.Button(main_frame, text="Generate Chunks",
                                command=lambda: generate_button_click(text_area, result_frame))
    generate_button.pack(pady=5)

    result_frame = tk.Frame(main_frame)
    result_frame.pack(fill=tk.BOTH, expand=True)

    exit_button = tk.Button(main_frame, text="Exit", command=root.destroy)
    exit_button.pack(side=tk.BOTTOM, pady=5)

    root.mainloop()

if __name__ == "__main__":
    main()