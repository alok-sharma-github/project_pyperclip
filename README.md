# Clipboard Summarizer 
(**project_pyperclip**)

[Read Blog](https://medium.com/@kingofkingsalok/boost-productivity-with-clipboard-summarizer-a-smart-text-summarization-tool-3aed09c0794c)

Clipboard Summarizer is a desktop application that monitors clipboard content and generates summaries of the text copied to the clipboard. It uses state-of-the-art NLP models, specifically T5 (Text-to-Text Transfer Transformer), for text summarization, and provides a user-friendly experience with a system tray icon, allowing users to start, pause, and exit monitoring with ease.

### Features:
- **Clipboard Monitoring:** Continuously monitors the clipboard for new text.
- **Text Summarization:** Automatically summarizes any long text copied to the clipboard.
- **System Tray Integration:** Minimizes to the system tray for convenient access and management.
- **Real-Time Alerts:** Displays text summaries in a popup alert, making it easy to process large amounts of text quickly.

### Technologies Used:
- **Transformers Library (Hugging Face)**: Utilizes a lightweight T5 model for text summarization.
- **Pyperclip**: Monitors and interacts with the system clipboard.
- **PyStray**: Provides system tray functionality for the application.
- **Pillow**: Used for handling the system tray icon.

### Installation:
1. Download the installer from the releases section.
2. Run the installer to set up Clipboard Summarizer on your machine.
3. Once installed, you can launch the application from the system tray.

### Usage:
Once running, the application will automatically start monitoring the clipboard. When text is copied, the application will summarize the content and display the result in a pop-up message.

### Contributing:
Feel free to open issues or submit pull requests for improvements, bug fixes, or new features!
