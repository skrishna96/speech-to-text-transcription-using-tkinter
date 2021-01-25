from tkinter import *
import speech_recognition as sr
import pymysql


def speechToText():
     r = sr.Recognizer()

     with sr.Microphone() as source:
        try:
             audio = r.listen(source,timeout=5)
             message = r.recognize_google(audio)
             entrytext.focus()
             entrytext.delete(0, END)
             entrytext.insert(0, message)
             try:
                 con=pymysql.connect(host='localhost',user='****',password='****',database='stt')
                 cur = con.cursor()
                 cur.execute('insert into speechtotext(text) values(%s)',(entrytext.get()))
                 con.commit()
                 con.close()
             except Exception as e:
                 messagebox.showerror('error',f'Error due to {e}')

        except sr.UnknownValueError:
            print('Google Speech Recognition could not understand audio')

        except sr.RequestError as e:
            print('Could not request results from Google Speech Recognition Service')


speechwindow = Tk()
speechwindow.title("Speech to Text converter")
speechwindow.geometry("700x500+350+100")

photo = PhotoImage(file='microphone.png').subsample(15,15)

titleLabel = Label(speechwindow,text='Speech to Text converter',font=('arial',22,'bold'),fg='black')
titleLabel.place(x=160,y=30)

entrytext = Text(speechwindow,font=('arial',14),bg='lightgray',height=5,width=20)
entrytext.place(x=230,y=100)

recordButton = Button(speechwindow, image=photo, bd=0, activebackground='#c1bfbf', overrelief='groove', relief='sunken',command = speechToText)
recordButton.place(x=320,y=250)

speechwindow.mainloop()


