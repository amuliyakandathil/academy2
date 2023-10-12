class calculator():
    def __init__(self,a,b):
        self.a=a
        self.b=b
    def sums(self):
    
        return self.a+self.b
    def dif(self):
        return self.a-self.b   
    def mul(self):
        return self.a*self.b
    def div(self):
        return self.a/self.b
    def mod(self):
        return self.a%self.b
    
a= int(input("Enter a number:"))
b = int(input("Enter one more number:"))    
ob=calculator(a,b)
f=1
while (f==1):
        
        ch=int(input(("Enter 1-Addition 2-Subtraction 3-Multiplication 4-Division 5-Moduless 6-Square 0-EXIT")))
        if ch == 1:
            print("The Sum is: "+str(ob.sums))
        elif ch == 2:  
            print("The Difference is: " +str(ob.dif))
        elif ch==3:
            print("The Product  is: " +str(ob.mul))
        elif ch==4:
            print("The Quotient is: " +str(ob.div))
        elif ch ==5:
            print("The Moduless is: " +str(ob.mod))
        
        elif ch==0:
            print("Exiting")
            f=0
        else:
            print("Invalid option")

