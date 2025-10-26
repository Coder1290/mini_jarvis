import sys, os, time
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from core.speech_io import listen, speak
from core.executor import execute_command

EXIT_WORDS = ["bye", "goodbye", "good bye", "exit", "quit", "stop"]

def main():
    speak("Hello sir, I am Your Desktop Assistant. How may I help you?")
    while True:
        cmd = listen()
        if not cmd:
            speak("Please say that again.")
            time.sleep(0.3)  # small buffer to let audio finish
            continue

        # normalize text
        cmd = cmd.lower().replace("-", " ").strip()

        # --- EXIT COMMANDS ---
        if any(x in cmd for x in EXIT_WORDS):
            speak("Goodbye Sir! Have a great day!")
            time.sleep(0.3)  # small buffer to let audio finish
            break

        # --- NORMAL COMMANDS ---
        response = execute_command(cmd)
        print(response)
        speak(response)

if __name__ == "__main__":
    main()