import random
import tkinter
window = tkinter.Tk()
window.title("Password")
window.minsize(500,400)
window.configure(bg='white')
letters = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
    'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D',
    'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S',
    'T', 'U', 'V', 'W', 'X', 'Y', 'Z'
]
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
label1=tkinter.Label(text="WELCOME TO PASSWORD GENERATOR " , font =("Times new roman",13,"bold"),fg='black',bg ='white')
label1.place(x=90,y=30)
label2=tkinter.Label(text= "How many letters would you like to have in your password:",fg='black',bg = 'white')
label2.place(x=10,y=100)
no_letters= tkinter.Entry()
no_letters.configure(bg='light grey')
no_letters.place(x=350,y=100)
label2=tkinter.Label(text= "How many Symbols would you like to have in your password:",fg='black',bg = 'white')
label2.place(x=10,y=150)
no_symbols= tkinter.Entry()
no_symbols.configure(bg='light grey')
no_symbols.place(x=350,y=150)
label2=tkinter.Label(text= "How many Numbers would you like to have in your password:",fg='black',bg = 'white')
label2.place(x=10,y=200)
no_numbers= tkinter.Entry()
no_numbers.configure(bg='light grey')
no_numbers.place(x=350,y=200)
def Gen():
    l = no_letters.get()
    s = no_letters.get()
    n = no_letters.get()
    password_list = []
    for char in range(0, int(l) ):
       password_list += random.choice(letters)

    for char in range(0, int(s) ):
       password_list += random.choice(symbols)

    for char in range(0, int(n)):
       password_list += random.choice(numbers)

    random.shuffle(password_list)


    password = ""
    for char in password_list:
       password += char
    label4=tkinter.Label(text="Here is your password:  ",bg='white')
    label4.place(x=90,y=300)   
    label3=tkinter.Label(text=str(password),font = ("Times new roman",15),bg = 'light grey',fg='black')
    label3.place(x=250,y=300)  
btn =tkinter. Button(text = "Generate",command=Gen)
btn.place(x=200,y=250) 
window.mainloop()