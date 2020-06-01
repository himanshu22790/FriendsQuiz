from tkinter import *
import tkinter.messagebox
import pandas as pd
import random
from PIL import Image, ImageTk

qa = pd.read_excel('QuestionsAnswers.xlsx')
questions=qa['Questions']

a1=qa['Answer1']
#print(questions)
#print(a1)

answers=[["Eating","Reading","Cooking","Video Games","Shopping","Play Guitar"],
         ["Making the main course", "Making the dessert",
             "Making sure everything's in order", "Doing nothing but eat","Making everyone laugh",
             "Invite over an ex"],
         ["A nerd","Busy getting laid","Insanely popular","Tough and streetwise",'Stealing lunchboxes',"I was the class clown"],
         ["Responsibility","Failure","Lacking sense of humor","A bad hair day","Being normal","Falling out of the person you married"],
         ["I dont really like dogs","They are delicious","I love monkeys","They are fine","I love them, we shouldn't eat them","Cats with no fur are not cool"],
         ["1","2","3","4","5","6"],
         ["1","2","3","4","5","6"],
         ["1","2","3","4","5","6"],
         ["1","2","3","4","5","6"],
         ["1","2","3","4","5","6"],
]


chandler=[3,4,5,2,0]
ross=[1,2,0,1,2]
rachel=[4,1,2,3,5]
joey=[0,3,1,0,1]
monica=[2,0,4,5,3]
phoebe=[5,5,3,4,4]
user_answer=[]
indexes = []
def gen():
    global indexes
    while (len(indexes) < 5):
        x = random.randint(0,4)
        if x in indexes:
            continue
        else:
            indexes.append(x)


def showresult(score):
    lblQuestion.destroy()
    r1.destroy()
    r2.destroy()
    r3.destroy()
    r4.destroy()
    r4.destroy()
    r5.destroy()
    r6.destroy()
    labelimage = Label(
        window,
        background="#ffffff",
        border=0,
    )
    labelimage.pack(pady=(50, 30))
    labelresulttext = Label(
        window,
        font=("Jokerman", 20),
        background="#ffffff",
    )
    labelresulttext.pack()

    labelresultdesc = Label(
        window,
        font=("Gabriola", 14,'bold'),
        background="#ffffff",
        fg='teal'
    )
    labelresultdesc.pack()
    
    if score=='chandler_score':
        chandler_img = Image.open('chandler.png')
        chandler_img = chandler_img.resize((250, 250), Image.ANTIALIAS)
        chandlerimg = ImageTk.PhotoImage(chandler_img)
        labelimage.configure(image=chandlerimg)
        labelimage.image=chandlerimg
        labelresulttext.configure(text="You are Chandler")
        labelresultdesc.configure(text='Sarcasm is the most important thing for you. \nA loyal and true lover who is loved by all. \nBest friends with Joey')
    elif score == 'monica_score':
        monica_img = Image.open('monica.png')
        monica_img = monica_img.resize((250, 250), Image.ANTIALIAS)
        monicaimg = ImageTk.PhotoImage(monica_img)
        labelimage.configure(image=monicaimg)
        labelimage.image=monicaimg
        labelresulttext.configure(text="You are Monica")
    elif score == 'phoebe_score':
        phoebe_img = Image.open('phoebe.png')
        phoebe_img = phoebe_img.resize((250, 250), Image.ANTIALIAS)
        phoebeimg = ImageTk.PhotoImage(phoebe_img)
        labelimage.configure(image=phoebeimg)
        labelimage.image = phoebeimg
        labelresulttext.configure(text="You are Phoebe")
    elif score == 'joey_score':
        joey_img = Image.open('joey.png')
        joey_img = joey_img.resize((200, 200), Image.ANTIALIAS)
        joeyimg = ImageTk.PhotoImage(joey_img)
        labelimage.configure(image=joeyimg)
        labelimage.image=joeyimg
        labelresulttext.configure(text="You are Joey.")
        labelresultdesc.configure(
            text='aka Dr Drake Ramoray.\nA true foodie (love sandwiches).A loyal and true friend who is loved by all.\n How You Doin?? ')
    elif score == 'ross_score':
        ross_img = Image.open('ross.png')
        ross_img = ross_img.resize((250, 250), Image.ANTIALIAS)
        rossimg = ImageTk.PhotoImage(ross_img)
        labelimage.configure(image=rossimg)
        labelimage.image=rossimg
        labelresulttext.configure(text="You are Ross")
    elif score == 'rachel_score':
        rachel_img = Image.open('rachel.png')
        rachel_img = rachel_img.resize((250, 250), Image.ANTIALIAS)
        rachelimg = ImageTk.PhotoImage(rachel_img)
        labelimage.configure(image=rachelimg)
        labelimage.image=rachelimg
        labelresulttext.configure(text="You are Rachel")


def calc():
    global indexes,user_answer, chandler, monica, phoebe, rachel, ross, joey
    global user_answer, indexes
    global chandler_score, rachel_score, phoebe_score, ross_score, joey_score, monica_score
    chandler_score = 0
    monica_score = 0
    ross_score = 0
    rachel_score = 0 
    phoebe_score = 0 
    joey_score = 0
    score=0
    x=0
    for i in indexes:
        if user_answer[x]==chandler[i]:
            chandler_score=chandler_score + 5
            #x1=chandler_score
        elif user_answer[x] == monica[i]:
            monica_score = monica_score + 5
            #x2=monica_score
        elif user_answer[x] == joey[i]:
            joey_score = joey_score + 5
            #x3=joey_score
        elif user_answer[x] == phoebe[i]:
            phoebe_score = phoebe_score + 5
            #x4 = phoebe_score
        elif user_answer[x] == ross[i]:
            ross_score = ross_score + 5
        elif user_answer[x] == rachel[i]:
            rachel_score = rachel_score + 5
        x = x+1   
    #print(type(chandler_score))
    score = {chandler_score:'chandler_score',phoebe_score: 'phoebe_score',
             ross_score: 'ross_score', rachel_score: 'rachel_score', monica_score:'monica_score',
              joey_score:'joey_score'}

    print(chandler_score)
    print(monica_score)
    print(joey_score)
    print(phoebe_score)
    print(ross_score)
    print(rachel_score)
    score=score.get(max(score))
    print(score)
    showresult(score)


        

ques=1
def selected():
    global lblQuestion, r1, r2, r3, r4, r5, r6
    global radioVar, user_answer
    global ques
    x=radioVar.get()
    user_answer.append(x)
    radioVar.set(-1)
    if ques < 5:
        lblQuestion.config(text=questions[indexes[ques]])
        r1['text']=answers[indexes[ques]][0]
        r2['text']=answers[indexes[ques]][1]
        r3['text']=answers[indexes[ques]][2]
        r4['text']=answers[indexes[ques]][3]
        r5['text']=answers[indexes[ques]][4]
        r6['text']=answers[indexes[ques]][5]
        ques=ques+1
    else:
        calc()

def startQuiz():
    global lblQuestion, r1, r2, r3, r4, r5, r6
    lblQuestion = Label(
        window,
        text=questions[indexes[0]],
        font=('Gabriola', 18,"bold"),
        width=500,
        justify='center',
        wraplength=400,
        background='white',
    )
    lblQuestion.pack(pady=(50,35))
    global radioVar
    radioVar = IntVar()
    radioVar.set(-1)

    r1 = tkinter.Radiobutton(
        window,
        text= answers[indexes[0]][0],
        font=('Perpetua', 14, "bold"),
        value=0,
        variable=radioVar,
        background='white',
        fg = 'green',
        command=selected,
        )
    r1.pack()

    r2 = tkinter.Radiobutton(
        window,
        text=answers[indexes[0]][1],
        font=('Perpetua',14,"bold"),
        value=1,
        variable=radioVar,
        background='white',
        fg = 'magenta',
        command=selected,
        )
    r2.pack()

    r3 = tkinter.Radiobutton(
        window,
        text= answers[indexes[0]][2],
        font=('Perpetua', 14, "bold"),
        value=2,
        variable=radioVar,
        background='white',
        fg='navy',
        command=selected,
        )
    r3.pack()

    r4 = tkinter.Radiobutton(
        window,
        text=answers[indexes[0]][3],
        font=('Perpetua', 14, "bold"),
        value=3,
        variable=radioVar,
        background='white',
        fg = 'brown',
        command=selected,
        )
    r4.pack()

    r5 = tkinter.Radiobutton(
        window,
        text=answers[indexes[0]][4],
        font=('Perpetua', 14, "bold"),
        value=1,
        variable=radioVar,
        background='white',
        fg = 'maroon',
        command=selected,
        )
    r5.pack()

    r6 = tkinter.Radiobutton(
        window,
        text=answers[indexes[0]][5],
        font=('Perpetua', 14, "bold"),
        value=1,
        variable=radioVar,
        background='white',
        fg = 'purple',
        command=selected,
        )
    r6.pack()

    #rstButton = Button(window, text='Restart',command=startPressed, background='white', border=0)
    #rstButton.pack()

def startPressed():
    #labelimage.destroy()
    labeltext.destroy()
    lblInst.destroy()
    btnStart.destroy()
    gen() #added
    startQuiz()


window = Tk()
img1 = PhotoImage(file='Friends.png')
window.title('Friends Quiz')
window.geometry('700x600')
window.config(backgroun='white')
window.resizable(0,0)

labelimage=Label(window,image=img1, background = 'white')
labelimage.pack(pady=(40,0)) #tuple

labeltext = Label (
    window,
    text="QUIZ:\nWhich Friends character are you?",
    font=("Jokerman",18,"bold"), 
    fg='teal', 
    background="white"
    )
labeltext.pack()

#img2 = Image.open("start.png")
#img2 = img2.resize((100, 100), Image.ANTIALIAS)
#photoImg = ImageTk.PhotoImage(img2)
img2=PhotoImage(file='start1.png')

btnStart = Button(
    window,
    image=img2,
    relief = FLAT,
    background='white',
    border=0,
    command=startPressed,
    )
btnStart.pack(pady=(40,0))

lblInst = Label(
    window,
    text='You will get 20s to answer every question.\nClick on Play Now once you are ready',
    background='white',
    font='Papyrus',
    fg='navy',
    )
lblInst.pack(pady=(60,30))


window.mainloop()
