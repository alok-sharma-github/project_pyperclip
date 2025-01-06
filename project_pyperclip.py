import pyperclip
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
import time
import pymsgbox
from pystray import Icon, Menu, MenuItem
import threading
import os 
from PIL import Image
import sys

# Function to show alert in a separate thread
def show_alert(message, title):
    pymsgbox.alert(message, title)
    
# Clipboard monitoring flag
monitoring = threading.Event()

# Load the model and tokenizer locally
def load_summarizer():
    print("Loading summarization model...")
    model_name = "t5-small"  # Lightweight model for summarization
    tokenizer = AutoTokenizer.from_pretrained(model_name)
    model = AutoModelForSeq2SeqLM.from_pretrained(model_name)
    return tokenizer, model

try:
    tokenizer, model = load_summarizer()
except Exception as e:
    print(f"Error loading summarization model: {e}")
    pymsgbox.alert("Failed to load summarization model. Please check your installation.", "Error")
    sys.exit()


def summarize_text(text):
    max_input_length = tokenizer.model_max_length
    if len(text) > max_input_length:
        text = text[:max_input_length]
        print("Input text truncated to fit model limits.")
    inputs = tokenizer.encode("summarize: " + text, return_tensors="pt", max_length=512, truncation=True)
    outputs = model.generate(inputs, max_length=50, min_length=10, length_penalty=2.0, num_beams=4, early_stopping=True)
    return tokenizer.decode(outputs[0], skip_special_tokens=True)

def summarize_clipboard_text():
    try:
        text = pyperclip.paste()
        if not isinstance(text, str):
            raise ValueError("Clipboard content is not text.")
        if len(text) > 100:
            summary = summarize_text(text)
            threading.Thread(target=show_alert, args=(summary, "Summary"), daemon=True).start()
        else:
            threading.Thread(target=show_alert, args=("The selected text is too short to summarize.", "Error"), daemon=True).start()
    except Exception as e:
        print("Error summarizing clipboard text:", e)

def monitor_clipboard():
    monitoring.set()
    last_text = ""
    print("Monitoring clipboard for text...")
    while monitoring.is_set():
        try:
            text = pyperclip.paste()
        except Exception as e:
            print("Error reading clipboard:", e)
            time.sleep(1)
            continue
        if text != last_text:  # Detect new text
            last_text = text
            summarize_clipboard_text()
        time.sleep(1)  # Check the clipboard every second

# Menu actions for the tray icon
def on_start(icon, item):
    if not monitoring.is_set():
        threading.Thread(target=monitor_clipboard, daemon=True).start()
        # threading.Thread(target=show_alert, args=("Monitoring started.", "Clipboard Summarizer"), daemon=True).start()
    else:
        threading.Thread(target=show_alert, args=("Monitoring is already running.", "Clipboard Summarizer"), daemon=True).start()

def on_pause(icon, item):
    monitoring.clear()
    # threading.Thread(target=show_alert, args=("Monitoring paused.", "Clipboard Summarizer"), daemon=True).start()

def on_exit(icon, item):
    monitoring.clear()
    icon.stop()

# Validate icon path
# Validate icon path for standalone executable
if hasattr(sys, '_MEIPASS'):  # Check if running as a PyInstaller executable
    icon_path = os.path.join(sys._MEIPASS, "clipboard.png")
else:
    icon_path = "clipboard.png"
if not os.path.exists(icon_path):
    print(f"Icon file '{icon_path}' not found. Using default icon.")
    icon_path = None

# Load the icon image
def load_icon(icon_path):
    try:
        return Image.open(icon_path)
    except Exception as e:
        print(f"Failed to load icon: {e}")
        return None

# Load the icon image
icon_image = load_icon(icon_path)
if not icon_image:
    print("Could not load the tray icon. Exiting.")
    sys.exit()

# Create the system tray icon and menu
menu = Menu(
    MenuItem("Start Monitoring", on_start),
    MenuItem("Pause Monitoring", on_pause),
    MenuItem("Exit", on_exit)
)
tray_icon = Icon("Clipboard Summarizer", icon_image, "Clipboard Summarizer", menu)

if __name__ == "__main__":
    tray_icon.run()