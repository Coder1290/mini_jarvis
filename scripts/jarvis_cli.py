#its a cli version of jarvis
from core.speech_io import listen, speak
from core.executor import execute_command

def main():
    speak("Hello, I am Mini Jarvis, your Desktop assistant. How can I help you?")
    while True:
        cmd = listen()
        if "exit" in cmd or "quit" in cmd:
            speak("Goodbye!")
            break
        speak(execute_command(cmd))

if __name__ == "__main__":
    main()