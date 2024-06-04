import os
import subprocess
import SpeakListen as sl

def open_file(filename):
    try:
        # Use os.path.exists to check if the file exists
        if os.path.exists(filename):
            # Open the file using the default application based on the OS
            if os.name == 'nt':  # For Windows
                os.startfile(filename)
            elif os.name == 'posix':  # For macOS and Linux
                subprocess.call(('open' if sys.platform == 'darwin' else 'xdg-open', filename))
            sl.speak(f"Opened {filename} successfully.")
        else:
            sl.speak(f"File '{filename}' does not exist.")
    except Exception as e:
        sl.speak(f"An error occurred: {e}")

