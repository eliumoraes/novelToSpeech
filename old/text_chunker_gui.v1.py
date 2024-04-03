import tkinter as tk
from tkinter import scrolledtext, messagebox
import pyperclip

def transform_chunk(chunk):
    chunk = chunk.strip().replace("\n", "%0D%0A").replace(" ", "+").replace('"', '%22')
    return f"language=&character=en-GB-ThomasNeural&text={chunk}"

def generate_chunks(text):
    chunks = []
    while text:
        if len(text) > 5000:
            end = text.rfind(".", 0, 5000) + 1
            chunk = text[:end]
            text = text[end:].lstrip()
        else:
            chunk = text
            text = ""
        chunks.append(transform_chunk(chunk))
    return chunks

def display_chunks(chunks, frame):
    for widget in frame.winfo_children():
        widget.destroy()
    for i, chunk in enumerate(chunks, start=1):
        chunk_text = tk.Text(frame, height=4, width=75)
        chunk_text.insert(tk.END, chunk)
        chunk_text.grid(row=i, column=0, padx=10, pady=5)
        chunk_text.configure(state='disabled')
        
        copy_button = tk.Button(frame, text="Copy", command=lambda c=chunk: pyperclip.copy(c))
        copy_button.grid(row=i, column=1, padx=10)

def generate_button_click(text_area, frame):
    text = text_area.get("1.0", tk.END)
    chunks = generate_chunks(text)
    display_chunks(chunks, frame)

def main():
    root = tk.Tk()
    root.title("Text Chunker")

    main_frame = tk.Frame(root)
    main_frame.pack(fill=tk.BOTH, expand=True)

    text_area = scrolledtext.ScrolledText(main_frame, height=10)
    text_area.pack(padx=10, pady=5)

    generate_button = tk.Button(main_frame, text="Generate Chunks", command=lambda: generate_button_click(text_area, result_frame))
    generate_button.pack(pady=5)

    result_frame = tk.Frame(main_frame)
    result_frame.pack(fill=tk.BOTH, expand=True)

    exit_button = tk.Button(main_frame, text="Exit", command=root.destroy)
    exit_button.pack(side=tk.BOTTOM, pady=5)

    root.mainloop()

if __name__ == "__main__":
    main()
