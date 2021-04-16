print("Starting preprocessing")
import audio,image,webcam,text
while(True):
    print("\n\n***************************\nModes:\n1.Text\n2.Audio\n3.Image\n4.Webcam\n5.Quit\n\n")
    mode=int(input())
    if(mode==1):
        print("Emotion detection based on Text")
        textInput=input("Enter text\n")
        print(text.textDetect(textInput))
    elif(mode==2):
        choice=int(input("1.Listen to Microphone\n2.Pass audio file"))
        if(choice==1):
            print("Microphone will record for 5 seconds")
            textInput=audio.listen()
            print(textInput)
            print(text.textDetect(textInput))
        elif(choice==2):
            filePath=input("Enter path of file\n")
            textInput=audio.file(filePath)
            print(textInput)
            print(text.textDetect(textInput))
    elif(mode==3):
        filePath=input("Enter path of file\n")
        print(image.detect(filePath))
    elif(mode==4):
        print("Webcam will record for 15 seconds")
        print("Press 'q' to Quit")
        print(webcam.live())
    else:
        print("Quiting .....")
        break
