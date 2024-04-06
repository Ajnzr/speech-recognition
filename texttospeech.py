import pyttsx3
txt_sp=pyttsx3.init()
text=input("Enter the text you want to speak:")
voices=txt_sp.getProperty('voices')
for i in voices:
    print("ID",i.id)
txt_sp.setProperty('voice',voices[0].id)
txt_sp.say(text)
txt_sp.runAndWait()