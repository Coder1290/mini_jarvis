import pyttsx3

engine = pyttsx3.init(driverName='sapi5')
voices = engine.getProperty('voices')
print("[DEBUG] Voices:")
for i, v in enumerate(voices):
    print(f"{i}: {v.id}")

# Try first voice; change index to test others
if voices:
    engine.setProperty('voice', voices[0].id)
else:
    print("[WARNING] No voices found.")

engine.setProperty('rate', 175)
engine.setProperty('volume', 1.0)

engine.say("This is a test of Mini Jarvis speaking. If you hear this, TTS is working.")
engine.runAndWait()