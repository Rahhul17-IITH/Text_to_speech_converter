from tkinter import *
from gtts import gTTS
import os
root = Tk()

#styling
#place the widget in gui window
frame1=Frame(root, bg="white", height="250")
frame1.pack(fill = X)
frame2=Frame(root, bg="white", height="750")
frame2.pack(fill = X)

#STYLING the label
label=Label(frame1,text="Text to Speech\n(to paste from clip board, use ctrl+v)",font="bold,30",bg='white')
label.place(x=175,y=70)
#entry used to enter the text

entry=Entry(frame2,width=45,bd=4,font=14)
entry.place(x=100,y=52)
entry.insert(0,"")
#text into audio conversion
def play():
    language="en"
    myobj=gTTS(text=entry.get(), lang=language, slow=False)

    #name and save the audio file
    myobj.save("convert.wav")
    os.system("convert.wav")

#create a button for play
command=play
btn=Button(frame2,text="SUBMIT",width="15",pady=10,font="bold,15",command=play,bg='blue')
btn.place(x=250,y=130)
#title
root.title("text_to_speech_convertor")
root.geometry("650x550")
#start the gui
root.mainloop()
