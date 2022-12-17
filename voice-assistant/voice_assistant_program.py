import pyttsx3
import speech_recognition as sr
import datetime
import pyaudio
import wikipedia
import webbrowser
import os
import random
import smtplib
from tkinter import *
import threading








engine= pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty('voice',voices[0])

'''def len_Calculate():
    
    l2_width= l2.winfo_reqwidth()
    print(l2.winfo_reqwidth())
    if l2_width < 250:
        w= 400-l2_width-2
        return w
    else:
        w=150
        return w    '''
            



def takeCommand():
    global a,l2
    r=sr.Recognizer()  
    with sr.Microphone() as source:
        
        L.config(text="Listening...")
        print('Listening....') 
        r.pause_threshold=1
        audio = r.listen(source)

        try:
            
            L.config(text="Recognising...")
            print('recognising')
            query = r.recognize_google(audio,language='en-in')

            for widgets in frame.winfo_children():
               widgets.destroy()
            ll=Label(frame,text="You",bg='blue4',fg='gold')
            ll.place(relx=1,x=-2,y=a,anchor=NE)
            a= a + ll.winfo_reqheight() + 2
            l2=Label(frame,text=query,wraplength=300,justify=LEFT,font=('lucida 16'),bg='CadetBlue1',fg='midnight blue')
            l2.place(relx=1, x =-5, y=a,anchor=NE)
            
            a= a + l2.winfo_reqheight() + 5

           
            
            print(f'user said:{query}')
           
        except Exception as e:
            print('Say that again')
            return 'None' 
    return query        

        

def main():
     B.config(text='Running',state=DISABLED)
     for widgets in frame.winfo_children():
         widgets.destroy()
     global a
     a=10
     wishme()
     while True:
        a=10
        query=takeCommand().lower()
        L.config(text="Alexa")

        if 'wikipedia' in query:
            speak('searching wikipedia')
            query = query.replace('wikipedia',' ')
            result= wikipedia.summary(query,sentences=2)
            z=wikipedia.page(query)
            w=z.images[0]
            l1.config(image=w)
            
            speak('according to wikipedia')
            speak(result)
            
            

        elif "open google" in query:
            speak('opening google for you sir.')
            webbrowser.open('google.com')    

        elif 'open youtube' in query:
            speak('opening youtube for you sir.')
            webbrowser.open('youtube.com')  

        elif 'play music' in query:
            speak('playing music for you sir.')
            music_dir='E:\\SONGS'
            songs= os.listdir(music_dir)
            os.startfile(os.path.join(music_dir,songs[0]))


        elif 'open code' in query:
            speak('opening visual studio code  for you sir.')
            codepath= "C:\\Users\\Asus\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe" 
            os.startfile(codepath)

        elif  'send email to'in query:
              
            if 'samarth' in query:
                to=dict.get('samarth')
            elif 'shubham' in query:
                to=dict.get('shubham')  
            elif 'ravi purohit' in query:
                to=dict.get('ravi')   
            elif 'saurabh' in query:
                to=dict.get('saurabh')     
            try:

                    speak('tell me the content of this mail')
                    content=takeCommand()
                    sendEmail(to,content)
                    speak('email has been sent.')
            except Exception as e:
                speak('sorry email not sent.')

        elif "what\'s up" in query or 'how are you' in query:
            stMsgs = ['Just doing my thing!', 'I am fine!', 'Nice!', 'I am nice and full of energy']
            speak(random.choice(stMsgs))

        elif 'exit' in query:
            break


        else:
            print("I can't here that. Please try again.") 
            engine.say("I can't here that. Please try again.")
            engine.runAndWait()

     B.config(text='Start Again',state=NORMAL)        
            

           

def speak(audio):
    global a
    print(audio)

    ll=Label(frame,text="Jarvis",bg='blue4',fg='gold')
    ll.place(relx=0,x=5,y=a,anchor=NW)
    a= a + ll.winfo_reqheight() + 2

    l1=Label(frame,text= audio ,wraplength=300,justify=LEFT,font=('lucida 16'),bg='CadetBlue2',fg='midnight blue')
    l1.place(relx = 0, x =5, y = a, anchor = NW)

    engine.say(audio)
    engine.runAndWait()

    a= a+ l1.winfo_reqheight()+5
   


def sendEmail(to,content):
    server= smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login('18bit053@ietdavv.edu.in',"S@ur@bh1998")
    server.sendmail("18bit053@ietdavv.edu.in",to,content)    

   
        

def wishme():
    hour=int(datetime.datetime.now().hour)  
    if hour>=6 and hour<12:
        speak("good morning mr. saurabh.")
       
    elif hour>=12 and hour<18:
        speak("good afternoon mr. saurabh")

    else:
        speak("good evening mr. Saurabh")   

    speak("hello sir, how may i help you.")   

def mycommand():
    t1 = threading.Thread(target=main)
    t1.start()


dict= {
        'samarth': '18bit053@ietdavv.edu.in',
        'shubham': 'bsss.3332@gmail.com',
        'ravi': 'purohitravi64@gmail.com',
        'saurabh': 'tsss.1920@gmail.com',
    }
if __name__=="__main__":
     


   root=Tk()
   root.title("Jarvis")
   root.geometry("400x580")

   frame=Frame(root,bg="blue4",height=500,width=400)
   frame.pack(side=TOP,expand=True,fill=BOTH)

   frame2=Frame(root,bg="LightSteelBlue4",height=80,width=400)
   frame2.pack(side=BOTTOM,expand=True,fill=BOTH)

   L= Label(frame2,text='Alexa',bg='LightSteelBlue3',fg='DodgerBlue4',font=('lucida 16'),height=2,width=13)
   L.place(relx=0.5,rely=0.5,anchor=CENTER)

   B=Button(frame2,text='Running',bg='red',fg='black',font='lucida 14',command=mycommand,padx=5,pady=5,state=DISABLED)
   B.place(relx=1,rely=0.5,x=-5,anchor=E)

   

   t1 = threading.Thread(target=main)
   t1.start()

   
  
  

   #l=Label(frame,text=,wraplength=5)
   
   

  
   


   
   '''button=Button(root,text='Wish Me',bg='red',fg='yellow',font='lucida 14',command=wishme)
   button.pack()
   button1=Button(root,text='Command',bg='red',fg='yellow',font='lucida 14',command=main)
   button1.pack()
   Label(root,text='').pack()
   Label(root,text='').pack()
   Label(root,text='').pack()
   Label(root,text='').pack()

   button2=Button(root,text='Exit',bg='red',fg='yellow',font='lucida 14',command=root.quit)
   button2.pack()'''
   root.mainloop()


    
   



             

               

