from tkinter import *
class app:

    def __init__(self):
        self.root=Tk()
        self.root.geometry('400x400')
        self.root.title('A Simple Calculator')
        self.root.configure(bg='black')
        Label(self.root,text='First Number',font=('verdana',20),bg='black',fg='blue').grid(row=0,column=0)
        self.t1=Entry(self.root,font=('arial',15))
        self.t1.grid(row=0,column=1)
        Label(self.root,text='2nd Number', font=('verdana',20),bg='black',fg='blue').grid(row=1,column=0)
        self.t2=Entry(self.root,font=('arial',15))
        self.t2.grid(row=1, column=1)
        Label(self.root,text='Result', font=('verdana',20),bg='black',fg='blue').grid(row=2,column=0)
        self.t3=Entry(self.root,font=('arial',15))
        self.t3.grid(row=2, column=1)
        self.b1=Button(self.root,text='+', font=('verdana',20),bg='red',fg='blue',command=self.sum)
        self.b1.grid(row=3,column=0)
        self.b2=Button(self.root,text='-', font=('verdana',20),bg='red',fg='blue',command=self.diff)
        self.b2.grid(row=3,column=1)
        self.b3=Button(self.root,text='x', font=('verdana',20),bg='red',fg='blue',command=self.mul)
        self.b3.grid(row=4,column=0)
        self.b4=Button(self.root,text='/', font=('verdana',20),bg='red',fg='blue',command=self.div)
        self.b4.grid(row=4,column=1)
        self.root.mainloop()

    def sum(self):
        a=self.t1.get()
        b=self.t2.get()
        c=int(a)+int(b)
        self.t3.delete(0,END)
        self.t3.insert(0,c)

    def diff(self):
        a=self.t1.get()
        b=self.t2.get()
        c=int(a)-int(b)
        self.t3.delete(0,END)
        self.t3.insert(0,c)

    def mul(self):
        a=self.t1.get()
        b=self.t2.get()
        c=int(a)*int(b)
        self.t3.delete(0,END)
        self.t3.insert(0,c)
    
    def div(self):
        a=self.t1.get()
        b=self.t2.get()
        c=int(a)/int(b)
        self.t3.delete(0,END)
        self.t3.insert(0,c)

ob=app()
