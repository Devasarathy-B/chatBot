from win32com.client import Dispatch
def speech(text):
    speak = Dispatch("SAPI.SpVoice")
    speak.Speak(text)
