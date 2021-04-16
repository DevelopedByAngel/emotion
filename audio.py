#Modules needed =>speechrecognition, pyaudio
import speech_recognition as sr
#intializing recognizer and microphone
def listen():
  r=sr.Recognizer()
  mic=sr.Microphone()#default mic
  print(mic)
  with mic as sou:
      #listening to background noise for 1 second
    print("Listening to background noise")
    r.adjust_for_ambient_noise(sou,duration=1)
    #listening to voice
    print("Speak")
    audio=r.listen(sou,5)
  try:
    print("Recognizing.......")
      #recognize through google syntax => recognize_google(data, language="en-EN") => en- english
    text=r.recognize_google(audio)
    return(text)
    #if voice not clear exception occurs
  except sr.UnknownValueError:
    text=""
    print("cannot understand.........")
    return("Error occured.... Please Try Again")
def file(file):
  r=sr.Recognizer()
  print("Starting recognition.......")
  try:
    with sr.AudioFile(file) as src:
      data=r.record(src)
      text=r.recognize_google(data)
      return(text)
  except Exception:
    return("Error occured.... Please Try Again")

