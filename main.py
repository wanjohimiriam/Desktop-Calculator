from tkinter import *

def btnclick(number):

    global user
    user = user+ str(number)
    text_input.set(user)
def btnclear():
    global user
    user=""
    text_input.set(user)

def btnback():
    global  user
    length = len(user)
    b=''
    for i in range(0, length-1):
        b+=user[i]
    user=b
    text_input.set(user)
def btnequal():
    global user
    user=str(eval(user))
    text_input.set(user)


win=Tk()
win.title('Calculator')
win.geometry('480x460+400+60')
win.resizable(False, False)

f = Frame(win, height=460, width=480, bg="black", bd=10, relief=GROOVE)
f.place(x=.0, y=0)

user = ''
text_input = StringVar()

text_dis = Entry(f, font="arial 27 bold", text = text_input, bd=25, bg='grey', justify='right', relief=RIDGE)
text_dis.place(x=1, y=1)

btn_1 = Button(f, text="1", font="arial 30 bold", bd=5, width=3, bg="grey", command=lambda:btnclick(1))
btn_1.place(x=4, y=100)
btn_2 = Button(f, text="2", font="arial 30 bold", bd=5, width=3, bg="grey", command=lambda:btnclick(2))
btn_2.place(x=92, y=100)
btn_3 = Button(f, text="3", font="arial 30 bold", bd=5, width=3, bg="grey", command=lambda:btnclick(3))
btn_3.place(x=180, y=100)
btn_4 = Button(f, text="4", font="arial 30 bold", bd=5, width=3, bg="grey", command=lambda:btnclick(4))
btn_4.place(x=4, y=185)
btn_5 = Button(f, text="5", font="arial 30 bold", bd=5, width=3, bg="grey", command=lambda:btnclick(5))
btn_5.place(x=92, y=185)
btn_6 = Button(f, text="6", font="arial 30 bold", bd=5, width=3, bg="grey", command=lambda:btnclick(6))
btn_6.place(x=180, y=185)
btn_7 = Button(f, text="7", font="arial 30 bold", bd=5, width=3, bg="grey", command=lambda:btnclick(7))
btn_7.place(x=4, y=270)
btn_8 = Button(f, text="8", font="arial 30 bold", bd=5, width=3, bg="grey", command=lambda:btnclick(8))
btn_8.place(x=92, y=270)
btn_9 = Button(f, text="9", font="arial 30 bold", bd=5, width=3, bg="grey", command=lambda:btnclick(9))
btn_9.place(x=180, y=270)
btn_0= Button(f, text="0", font="arial 30 bold", bd=5, width=3, bg="grey", command=lambda:btnclick(0))
btn_0.place(x=4, y=355)
btn_dot = Button(f, text=".", font="arial 30 bold", bd=5, width=3, bg="grey", command=lambda:btnclick("."))
btn_dot.place(x=92, y=355)
btn_clear = Button(f, text="C", font="arial 30 bold", bd=5, width=3, bg="powder blue", command=btnclear)
btn_clear.place(x=180, y=355)

btn_add = Button(text='+', font='arial 30  bold', bd=5, width=3, bg="powder blue", command=lambda:btnclick("+"))
btn_add.place(x=278, y=110)
btn_mult = Button(text='x', font='arial 30  bold', bd=5, width=3, bg="powder blue", command=lambda:btnclick('x'))
btn_mult.place(x=278, y=195)
btn_sub = Button(text='-', font='arial 30  bold', bd=5, width=3, bg="powder blue", command=lambda:btnclick('-'))
btn_sub.place(x=366, y=110)
btn_div = Button(text='/', font='arial 30  bold', bd=5, width=3, bg="powder blue", command=lambda:btnclick('/'))
btn_div.place(x=366, y=195)
btn_rem = Button(text='%', font='arial 30  bold', bd=5, width=3, bg="powder blue", command=lambda:btnclick('%'))
btn_rem.place(x=278, y=280)

btn_b = Button(text='⌫', font='arial 30  bold', bd=5, width=3, bg="powder blue", command=btnback)
btn_b.place(x=278, y=365)
btn_eql = Button(text='=', font='arial 30  bold',height=3, bd=5, width=3, bg="powder blue", command= btnequal)
btn_eql.place(x=366 , y=280)

win.mainloop()