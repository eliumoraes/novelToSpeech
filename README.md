# NovelToSpeech

This repository contains a Python project designed for converting novel text to speech, primarily focusing on novels from [Novelhall](https://www.novelhall.com). The application allows users to paste the novel text into a UI, divides the text into chunks (to accommodate API character limits), generates speech from these chunks, and plays the audio.

## Installation

1. **Install Python**
Ensure you have Python installed on your system. If not, download and install it from [Python's official website](https://www.python.org/).

2. **Install Dependencies**
After installing Python, install the required libraries using pip:
```bash
pip install -r requirements.txt
```

*Note: `tkinter` comes pre-installed with Python. If you encounter issues with `tkinter`, ensure your Python installation includes it by running `python -m tkinter` on Windows or `python3 -m tkinter` on Linux. On Linux, if `tkinter` is missing, install it via your package manager, e.g., `sudo apt-get install python3-tk`.*

3. **How to Run**
- Navigate to the project directory:
```bash
cd path/to/novelToSpeech
```
- Run the main script:
```bash
python novel_to_speech_converter.py
```

4. **Contributing**
Contributions are welcome! Please feel free to submit pull requests or open issues to improve the project or suggest new features.

