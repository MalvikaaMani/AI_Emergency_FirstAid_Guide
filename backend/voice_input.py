import speech_recognition as sr

def capture_voice_input():
    r = sr.Recognizer()

    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source)

    try:
        return r.recognize_google(audio)
    except:
        return None
