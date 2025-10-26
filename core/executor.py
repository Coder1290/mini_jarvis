import os
import subprocess
import signal
import psutil

# Map spoken names to actual system commands
APP_COMMANDS = {
    "notepad": "notepad",
    "calculator": "calc",
    "chrome": "chrome",  # works if Chrome is in PATH
    # Add more here...
}

def execute_command(command: str) -> str:
    if not command:
        return "I didn't catch that. Please repeat."

    # --- OPEN APP ---
    if command.startswith("open "):
        app = command.replace("open ", "").strip()
        if app in APP_COMMANDS:
            try:
                subprocess.Popen([APP_COMMANDS[app]])
                return f"Opening {app.capitalize()}."
            except Exception as e:
                return f"Failed to open {app}: {e}"
        else:
            return f"I don't know how to open {app} yet."

    # --- CLOSE APP ---
    if command.startswith("close "):
        app = command.replace("close ", "").strip()
        try:
            closed = False
            for proc in psutil.process_iter(['pid', 'name']):
                name = (proc.info['name'] or "").lower()
                if app.lower() in name:
                    os.kill(proc.info['pid'], signal.SIGTERM)
                    closed = True
            return f"Closing {app.capitalize()}." if closed else f"{app.capitalize()} is not running."
        except Exception as e:
            return f"Failed to close {app}: {e}"

    return "Command not recognized yet."