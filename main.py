words = ['Allah','Tree','Food','Salah','Ramadan','Python','DIU','Laptop','Exam','Happy','Moon','Parrot']


def time():
    global timeleft,score,wrong
    if (timeleft > 0):
        timeleft -= 1
        timeLabelCount.configure(text=timeleft)
        timeLabelCount.after(1000,time)
    else:
        gamePlayDetailLabel.configure(text='HIT = {} | Wrong = {} | Score = {}'.format(score,wrong,score-wrong))
        retry = messagebox.askretrycancel('Notification','For Play Again Hit Retry Button')
        if(retry == True):
            score = 0
            timeleft = 60
            wrong = 0
            timeLabelCount.configure(text=timeleft)
            wordLabel.configure(text=words[0])
            scoreLabelCount.configure(text=score)

def startGame(event):
    global score,wrong
    if(timeleft == 60):
        time()
    gamePlayDetailLabel.configure(text='')
    if(wordEntry.get() == wordLabel['text']):
        score += 1
        scoreLabelCount.configure(text=score)
    else:
        wrong += 1
    random.shuffle(words)
    wordLabel.configure(text=words[0])
    wordEntry.delete(0,END)


from tkinter import *
import random
from tkinter import messagebox

####################################### Root Method ####################################
root = Tk()
root.geometry('850x535+250+100')
root.configure(bg='LightSeaGreen')
root.title('Game Of Speed Typing Test')
root.iconbitmap('GameOfSpeedTypingTest.ico')

######################################## Variables #######################################
score = 0
timeleft = 60
count = 0
sliderWords = ''
wrong = 0

######################################## Label Method ####################################
fontLabel = Label(root,text='Welcome To The Game Of Speed Typing Test',font=('Calibra',26,'bold'),bg='LightSeaGreen',fg='DarkRed',width=39)
fontLabel.place(x=10,y=10)


random.shuffle(words)
wordLabel = Label(root,text=words[0],font=('Calibra',32,'italic bold'),bg='LightSeaGreen')
wordLabel.place(x=353,y=192)

scoreLabel = Label(root,text='Your Score : ',font=('Calibra',24,'bold'),bg='LightSeaGreen')
scoreLabel.place(x=10,y=100)

scoreLabelCount = Label(root,text=score,font=('Calibra',24,'bold'),bg='LightSeaGreen',fg='MediumBlue')
scoreLabelCount.place(x=78,y=150)

timerLabel = Label(root,text='Time Left : ',font=('Calibra',24,'bold'),bg='LightSeaGreen')
timerLabel.place(x=636,y=100)

timeLabelCount = Label(root,text=timeleft,font=('Calibra',24,'bold'),bg='LightSeaGreen',fg='MediumBlue')
timeLabelCount.place(x=700,y=150)

gamePlayDetailLabel = Label(root,text='Type Word & Hit Enter Button',font=('Calibra',26,'bold'),bg='LightSeaGreen',
                            fg='DarkGrey')
gamePlayDetailLabel.place(x=170,y=360)

######################################## Entry Method ####################################
wordEntry = Entry(root,font=('Calibra',21,'italic bold'),bd=9,justify='center')
wordEntry.place(x=252,y=260)
wordEntry.focus_set()

########################################               ####################################
root.bind('<Return>',startGame)

root.mainloop()