import os
import tkinter as tk
from tkinter import scrolledtext, messagebox, ttk

from mutagen.mp3 import MP3
import text_chunker
import speech_generator
import requests
import threading
import pygame
import pyperclip

def display_chunks(chunks, frame):
    print("Displaying chunks")
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

        mp3_button = tk.Button(frame, text="MP3", command=lambda c=chunk, cs=chunk_size, fr=frame, r=i: generate_audio(c, cs, fr, r))
        mp3_button.grid(row=i, column=4, padx=10)

def download_file(url, filename):
    print(f"Downloading from {url} to {filename}")
    response = requests.get(url)
    with open(filename, 'wb') as f:
        f.write(response.content)

def play_audio_clip(file_path, frame, row, max_length):
    try:
        mp3_info = MP3(file_path)
        audio_length_seconds = int(mp3_info.info.length)
        print(f"Audio length: {audio_length_seconds} seconds")
    except Exception as e:
        messagebox.showerror("Error", f"Failed to load MP3 metadata: {str(e)}")
        print(f"Error loading MP3 metadata: {str(e)}")
        return

    pygame.mixer.init(frequency=mp3_info.info.sample_rate)
    pygame.mixer.music.load(file_path)
    pygame.mixer.music.play()
    print("Audio playback started")

    progress_bar = ttk.Progressbar(frame, length=100, mode='determinate')
    progress_bar.grid(row=row, column=6, padx=10)
    update_progress_bar(progress_bar, frame, audio_length_seconds)

    def toggle_play_pause():
        if pygame.mixer.music.get_busy():
            pygame.mixer.music.pause()
            play_button.config(text="Play")
            print("Audio paused")
        else:
            pygame.mixer.music.unpause()
            play_button.config(text="Pause")
            print("Audio resumed")

    play_button = tk.Button(frame, text="Pause", command=toggle_play_pause)
    play_button.grid(row=row, column=5, padx=10)

# Incorporate the updated play_audio_clip in the generate_audio function
def generate_audio(chunk, chunk_size, frame, row):
    print(f"Generating audio for chunk size {chunk_size}")
    mp3_url = speech_generator.make_tts_request(chunk, chunk_size)
    if mp3_url:
        if not os.path.exists('mp3'):
            os.makedirs('mp3')
        filename = f"mp3/audio_chunk_{row}.mp3"
        download_file(mp3_url, filename)
        play_audio_clip(filename, frame, row, int(MP3(filename).info.length))
    else:
        messagebox.showerror("Error", "Failed to generate audio.")


def update_progress_bar(progress_bar, frame, max_length):
    def update():
        if pygame.mixer.music.get_busy():
            current_pos = pygame.mixer.music.get_pos() / 1000  # Current position in seconds
            progress = int((current_pos / max_length) * 100)
            progress_bar['value'] = progress
            print(f"Progress updated: {progress}%")
            frame.after(1000, update)  # Continue updating while music is playing
        else:
            frame.after(1000, update)  # Wait without updating progress bar, check again in 1 second

    update()  # Initial call to update

def generate_button_click(text_area, frame, chunk_size_entry):
    text = text_area.get("1.0", tk.END)
    try:
        default_chunk_size = int(chunk_size_entry.get())
    except ValueError:
        messagebox.showerror("Error", "Invalid chunk size. Please enter a valid number.")
        return
    chunks = text_chunker.generate_chunks(text, default_chunk_size)
    display_chunks(chunks, frame)

def clear_fields(text_area, frame):
    text_area.delete('1.0', tk.END)
    for widget in frame.winfo_children():
        widget.destroy()

def main():
    root = tk.Tk()
    root.title("Text to Speech")

    main_frame = tk.Frame(root)
    main_frame.pack(fill=tk.BOTH, expand=True)

    chunk_size_label = tk.Label(main_frame, text="Chunk Size (default: 5000):")
    chunk_size_label.pack(pady=(5, 0))

    chunk_size_entry = tk.Entry(main_frame)
    chunk_size_entry.insert(0, "5000")
    chunk_size_entry.pack(pady=5)

    text_area = scrolledtext.ScrolledText(main_frame, height=10)
    text_area.pack(padx=10, pady=5)

    generate_button = tk.Button(main_frame, text="Generate Chunks",
                                command=lambda: generate_button_click(text_area, result_frame, chunk_size_entry))
    generate_button.pack(pady=5)

    clear_fields_button = tk.Button(main_frame, text="Clear Fields",
                                    command=lambda: clear_fields(text_area, result_frame))
    clear_fields_button.pack(pady=5)

    result_frame = tk.Frame(main_frame)
    result_frame.pack(fill=tk.BOTH, expand=True)

    exit_button = tk.Button(main_frame, text="Exit", command=root.destroy)
    exit_button.pack(side=tk.BOTTOM, pady=5)

    root.mainloop()

if __name__ == "__main__":
    main()
