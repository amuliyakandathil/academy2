a = int(input("Enter a number:"))
b = int(input("Enter one more number:"))

def sums(a,b):
    c = a+b
    print("The sum is: " + str(c))
def dif(a,b):
    c = a-b
    print("The Diffrence is: " + str(c))
def mul(a,b):
    c = a*b
    print("The Product is: " + str(c))
    
def div(a,b):
    c = a/b
    print("The quotient is: " + str(c))
def mod(a,b):
    c = a%b
    print("The moduless is: " + str(c))
def squ(a,b):
    c = a*a
    print("The square is: " + str(c))
    c = b*b
    print("The square is: " + str(c))
def cal(a,b):
    f=1
    while (f==1):
        
        ch=int(input(("Enter 1-Addition 2-Subtraction 3-Multiplication 4-Division 5-Moduless 6-Square 0-EXIT")))
        if ch == 1:
            sums(a,b)
        elif ch == 2:  
            dif(a,b)
        elif ch==3:
            mul(a,b)
        elif ch==4:
            div(a,b)
        elif ch ==5:
            mod(a,b)
        elif ch==6:
            squ(a,b)
        elif ch==0:
            print("Exiting")
            f=0
        else:
            print("Invalid option")
cal(a,b)          
