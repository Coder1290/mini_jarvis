import speech_recognition as sr
import pyttsx3

def speak(text: str) -> None:
    """Speak text aloud using pyttsx3 with a fresh engine each call."""
    # print(f"[DEBUG] Speaking: {text}")
    engine = pyttsx3.init(driverName='sapi5')  # Windows SAPI5
    engine.setProperty('rate', 175)
    engine.setProperty('volume', 1.0)

    # Prefer Zira, otherwise David
    # voices = engine.getProperty('voices')
    # chosen = None
    # for v in voices:
    #     if "ZIRA" in v.id.upper():
    #         chosen = v.id
    #         break
    # if not chosen:
    #     for v in voices:
    #         if "DAVID" in v.id.upper():
    #             chosen = v.id
    #             break
    # if chosen:
    #     engine.setProperty('voice', chosen)

    engine.say(text)
    engine.runAndWait()
    engine.stop()

def listen(timeout: float = 5.0, phrase_time_limit: float = 7.0) -> str:
    """Listen for voice input and return recognized text, or empty string on error."""
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source, duration=0.6)
        print("Listening...")
        try:
            audio = r.listen(source, timeout=timeout, phrase_time_limit=phrase_time_limit)
        except Exception as e:
            print(f"[DEBUG] Listen error: {e}")
            return ""

    try:
        command = r.recognize_google(audio)
        print(f"You said: {command}")
        return command.lower().strip()
    except sr.UnknownValueError:
        return ""
    except sr.RequestError:
        return ""