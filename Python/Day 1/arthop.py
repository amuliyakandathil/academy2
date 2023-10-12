
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

a = int(input("Enter a number:"))
b = int(input("Enter one more number:"))
sums(a,b)
dif(a,b)
mul(a,b)
div(a,b)
mod(a,b)
squ(a,b)