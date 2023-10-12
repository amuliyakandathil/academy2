class calculator():
    #def _init_(self,a,b):
        #self.a=a
        #self.b=b
    def sums(self,a,b):
        return a+b
    def dif(self,a,b):
        return a-b    
    def mul(self,a,b):
        return a*b
    def div(self,a,b):
        return a/b
    def mod(self,a,b):
        return a%b
    
a= int(input("Enter a number:"))
b = int(input("Enter one more number:"))    
ob=calculator()
f=1
while (f==1):
        
        ch=int(input(("Enter 1-Addition 2-Subtraction 3-Multiplication 4-Division 5-Moduless 6-Square 0-EXIT")))
        if ch == 1:
            print("The Sum is: "+str(ob.sums(a,b)))
        elif ch == 2:  
            print("The Difference is: " +str(ob.dif(a,b)))
        elif ch==3:
            print("The Product  is: " +str(ob.mul(a,b)))
        elif ch==4:
            print("The Quotient is: " +str(ob.div(a,b)))
        elif ch ==5:
            print("The Moduless is: " +str(ob.mod(a,b)))
        
        elif ch==0:
            print("Exiting")
            f=0
        else:
            print("Invalid option")

