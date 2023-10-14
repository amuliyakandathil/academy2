import tkinter
window = tkinter.Tk()
window.title("To-Do LIST")
window.minsize(300,400)
window.configure(bg='white')
label1=tkinter.Label(text="Your to-do list" , font =("comic sams ms",15),fg='black',bg ='white')
label1.place(x=10,y=20)
activity= tkinter.Entry()
activity.configure(bg='light grey')
activity.place(x=10,y=70)
label2=tkinter.Label(text="Your list: " , font =("comic sams ms",15),fg='black',bg ='white')
label2.place(x=10,y=150)
task_list = []
def add_act():
    task = activity.get()
    task_list.append(task)
    label3=tkinter.Label(text=task_list, font =("areil",10),fg='green',bg ='white')
    label3.place(x=10,y=200)
def remove_act():
    task = activity.get()
    f = task_list.index(task)
    if f:
     task_list.remove(f)
     label4=tkinter.Label(text=task_list, font =("areil",10),fg='black',bg ='white')
     label4.place(x=10,y=400)
    else:
        label5=tkinter.Label(text=task_list, font =("areil",10),fg='black',bg ='white')
        
        label5.place(x=10,y=400)
def  com_act():
    task = activity.get()
    f = task_list.index(task)
    if f:
        
    
btn1 =tkinter. Button(text = "ADD",command=add_act)
btn1.place(x=10,y=100)
btn2 =tkinter. Button(text = "REMOVE",command=remove_act)
btn2.place(x=60,y=100)
btn3 =tkinter. Button(text = "DONE",)
btn3.place(x=150,y=100)
window.mainloop()
