import speech_recognition as sr

init_rec = sr.Recognizer()
print("Let's speak!!")

with sr.Microphone() as source:
    print("Please start speaking...")
    audio_data = init_rec.listen(source, timeout=15)  # Changed record to listen
    print("Recognizing your text.............")

try:
    text = init_rec.recognize_google(audio_data)
    print("You said: " + text)
except sr.UnknownValueError:
    print("Google Web Speech API could not understand audio")
except sr.RequestError as e:
    print(f"Could not request results from Google Web Speech API; {e}")

# Optional: You can add more error handling for different exceptions as needed
