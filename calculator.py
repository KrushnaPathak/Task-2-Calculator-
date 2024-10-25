from tkinter import *
win=Tk()
def add():
    a=int(e1.get())
    b=int(e2.get())
    c=a+b
    l4.config(text=""+str(c))

def sub():
    a=int(e1.get())
    b=int(e2.get())
    c=a-b
    l4.config(text=""+str(c))

def mul():
    a=int(e1.get())
    b=int(e2.get())
    c=a*b
    l4.config(text=""+str(c))

def div():
    a=int(e1.get())
    b=int(e2.get())
    c=a/b
    l4.config(text=""+str(c))

win.title("calculator")
win.geometry("600x500")
win.config(bg="#000000")
f1=("arial",20,"bold")

l1=Label(win,text="enter 1 no",font=f1,bg="black",foreground="white")
l1.place(x=50,y=50)
e1=Entry(win,bd=3,font=f1,bg="lightblue",foreground="black")
e1.place(x=200,y=50)

l2=Label(win,text="enter 2 no",font=f1,bg="black",foreground="white")
l2.place(x=50,y=100)
e2=Entry(win,bd=3,font=f1,bg="lightblue",foreground="black")
e2.place(x=200,y=100)

l3=Label(win,text="result",font=f1,bg="black",foreground="white")
l3.place(x=50,y=150)

l4=Label(win,text="_________",font=f1,bg="black",foreground="white")
l4.place(x=190,y=150)

b1=Button(win,text="add",font=f1,bg="lime",foreground="black",command=add)
b1.place(x=50,y=200)

b2=Button(win,text="sub",font=f1,bg="pink",foreground="black",command=sub)
b2.place(x=150,y=200)

b3=Button(win,text="mul",font=f1,bg="lime",foreground="black",command=mul)
b3.place(x=250,y=200)

b4=Button(win,text="div",font=f1,bg="pink",foreground="black",command=div)
b4.place(x=350,y=200)

b5=Button(win,text="exit",font=f1,bg="lime",foreground="black",command=quit)
b5.place(x=450,y=200)


win.mainloop()