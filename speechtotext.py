import speech_recognition as sr
def speech_rec():
    r=sr.Recognizer()
    mic=sr.Microphone()
    with mic as source:
        print("Speak...")
        r.energy_threshold=1000
        r.adjust_for_ambient_noise(source,duration=1)
        audio=r.listen(source)
        
        try:
            text=r.recognize_google(audio)
            print("You said",text)
       
        except:
            print("Please try again")
speech_rec()
