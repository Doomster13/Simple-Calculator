import tkinter as tk
win = tk.Tk()
win.title("Calculator")
e = tk.Entry(win,width=60,borderwidth=5)
e.grid(row=0,column=0,columnspan=4,padx=10,pady=10) 

def click(num):
    a=e.get()
    e.delete(0,tk.END)
    e.insert(0,str(a)+str(num))
    
def clr():
    e.delete(0,tk.END)

def add():
    global f_num
    global operation
    num1 = e.get()
    f_num = int(num1)   
    operation = "add"
    e.delete(0, tk.END)

def sub():
    global f_num
    global operation
    num1 = e.get()
    f_num = int(num1)   
    operation = "sub"
    e.delete(0, tk.END)

def multi():
    global f_num
    global operation
    num1 = e.get()
    f_num = int(num1)   
    operation = "multi"
    e.delete(0, tk.END)

def div():
    global f_num
    global operation
    num1 = e.get()
    f_num = int(num1)   
    operation = "div"
    e.delete(0, tk.END)


def eq():
    num2 = e.get()
    e.delete(0, tk.END)
    if operation == "add":
        result = f_num + int(num2)
    elif operation == "sun":
        result = f_num - int(num2)
    elif operation == "multi":
        result = f_num * int(num2)
    elif operation == "div":
        if int(num2)==0:
            e.insert(0,"MATH ERROR")
        else:
            result = f_num / int(num2)
    e.insert(0, result)

b1=tk.Button(win,text="1",padx=40,pady=10,command=lambda:click(1))
b2=tk.Button(win,text="2",padx=40,pady=10,command=lambda:click(2))
b3=tk.Button(win,text="3",padx=40,pady=10,command=lambda:click(3))
b4=tk.Button(win,text="4",padx=40,pady=10,command=lambda:click(4))
b5=tk.Button(win,text="5",padx=40,pady=10,command=lambda:click(5))
b6=tk.Button(win,text="6",padx=40,pady=10,command=lambda:click(6))
b7=tk.Button(win,text="7",padx=40,pady=10,command=lambda:click(7))
b8=tk.Button(win,text="8",padx=40,pady=10,command=lambda:click(8))
b9=tk.Button(win,text="9",padx=40,pady=10,command=lambda:click(9))
b0=tk.Button(win,text="0",padx=40,pady=10,command=lambda:click(0))
bcl=tk.Button(win,text="Clear",padx=77,pady=10,command=clr)
beq=tk.Button(win,text="=",padx=86,pady=10,command=eq)
badd=tk.Button(win,text="+",padx=39,pady=10,command=add)
bsub=tk.Button(win,text="-",padx=40,pady=10,command=sub)
bmulti=tk.Button(win,text="x",padx=40,pady=10,command=multi)
bdiv=tk.Button(win,text="/",padx=41,pady=10,command=div)

b1.grid(row=1,column=0)
b2.grid(row=1,column=1)
b3.grid(row=1,column=2)
b4.grid(row=2,column=0)
b5.grid(row=2,column=1)
b6.grid(row=2,column=2)
b7.grid(row=3,column=0)
b8.grid(row=3,column=1)
b9.grid(row=3,column=2)
b0.grid(row=4,column=0)
bcl.grid(row=4,column=1,columnspan=2)
beq.grid(row=5,column=1,columnspan=2)
badd.grid(row=1,column=3)
bsub.grid(row=2,column=3)
bmulti.grid(row=3,column=3)
bdiv.grid(row=4,column=3)

win.mainloop()