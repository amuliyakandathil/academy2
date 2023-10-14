import tkinter
window = tkinter.Tk()
window.title("CALCULATOR")
window.minsize(300,400)
space= tkinter.Entry()
space.configure(bg='light grey')
cal = " "
labelm=tkinter.Label(text="0",bg = 'white')
labelm.place(x=10,y=0)
def insert1():
        global cal
        element=btn1.cget("text")
        cal+=element
        labelm.config(text=cal)
def insert2():
        global cal
        element=btn2.cget("text")
        cal+=element
        labelm.config(text=cal)
def insert3():
        global cal
        element=btn3.cget("text")
        cal+=element
        labelm.config(text=cal)
def insert4():
        global cal
        element=btn4.cget("text")
        cal+=element
        labelm.config(text=cal)
def insert5():
        global cal
        element=btn5.cget("text")
        cal+=element
        labelm.config(text=cal)
def insert6():
        global cal
        element=btn6.cget("text")
        cal+=element
        labelm.config(text=cal)
def insert7():
        global cal
        element=btn7.cget("text")
        cal+=element
        labelm.config(text=cal)
def insert8():
        global cal
        element=btn8.cget("text")
        cal+=element
        labelm.config(text=cal)
def insert9():
        global cal
        element=btn9.cget("text")
        cal+=element
        labelm.config(text=cal)
def insert10():
        global cal
        element=btn10.cget("text")
        cal+=element
        labelm.config(text=cal)
def insert11():
        global cal
        element=btn11.cget("text")
        cal+=element
        labelm.config(text=cal)
def insert12():
        global cal
        element=btn12.cget("text")
        cal+=element
        labelm.config(text=cal)
def insert13():
        global cal
        element=btn13.cget("text")
        cal+=element
        labelm.config(text=cal)
def insert14():
        global cal
        element=btn14.cget("text")
        cal+=element
        labelm.config(text=cal)
def insert15():
        global cal
        element=btn15.cget("text")
        cal+=element
        labelm.config(text=cal)
def cal__():
    global cal
    l = len(cal)
    sy = res = 0
    for i in range(0, l):
        if cal[i] == '+' or cal[i] == '-' or cal[i] == '*' or cal[i] == '/':
            sy = i

    c = result = 0
    num1= cal[0:sy]
    num2 = cal[sy+1:l]
    if num1 and num2:  
        n1 = int(num1)
        n2 = int(num2)
        
    if cal[sy] == '+':
        result = n1 + n2
    elif cal[sy] == '-':
        result = n1 - n2
    elif cal[sy] == '*':
        result = n1 * n2
    elif cal[sy] == '/':
        result = n1 / n2
    labelm.config(text="0")
    labelm.config(text=str(result))
    labelm.place(x=10,y=0)
def clear():
    global cal
    cal = ""
    labelm.config(text="0")
btn1 =tkinter. Button(text = "1",command = insert1 )
btn1.place(x=50,y=80)
btn2=tkinter. Button(text = "2",command = insert2)
btn2.place(x=100,y=80)
btn3 =tkinter. Button(text = "3",command = insert3)
btn3.place(x=150,y=80)
btn4 =tkinter. Button(text = "4",command = insert4)
btn4.place(x=50,y=110)
btn5 =tkinter. Button(text = "5",command = insert5)
btn5.place(x=100,y=110)
btn6 =tkinter. Button(text = "6",command = insert6)
btn6.place(x=150,y=110)
btn7 =tkinter. Button(text = "7",command = insert7)
btn7.place(x=50,y=140)
btn8 =tkinter. Button(text = "8",command = insert8)
btn8.place(x=100,y=140)
btn9 =tkinter. Button(text = "9",command = insert9)
btn9.place(x=150,y=140)
btn11 =tkinter. Button(text = ".",command = insert11)
btn11.place(x=50,y=170)
btn10 =tkinter. Button(text = "0",command = insert10)
btn10.place(x=100,y=170)
btn12 =tkinter. Button(text = "+",command = insert12)
btn12.place(x=200,y=80)
btn13 =tkinter. Button(text = "-",command = insert13)
btn13.place(x=200,y=110)
btn14 =tkinter. Button(text = "*",command = insert14)
btn14.place(x=200,y=140)
btn15 =tkinter. Button(text = "/",command = insert15)
btn15.place(x=150,y=170)
btn15 =tkinter. Button(text = "=",command = cal__)
btn15.place(x=200,y=170)
btn16 =tkinter. Button(text = "clear",command = clear)
btn16.place(x=200,y=40)
window.mainloop()