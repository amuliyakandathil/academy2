import tkinter
window = tkinter.Tk()
window.title("CONVERTER")
window.minsize(500,400)
miles= tkinter.Entry()
miles.place(x=150,y=50)
label3=tkinter.Label(text="Miles : ")
label3.place(x=50,y=50)
label4=tkinter.Label(text="Kilometer: ")
label4.place(x=50,y=150)
def con():
    m = miles.get()
    k = float(m) * 1.609344
    label2=tkinter.Label(text="The kilometer is : "+ str(k))
    label2.place(x=150,y=150)
btn =tkinter. Button(text = "Convert",command=con)
btn.  place(x=200,y=100)
window.mainloop()