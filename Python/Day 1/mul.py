num = int(input("Enter a number: "))
print("The multiplication table for " + str(num) +" is: ")
for i in range(1,11):
    print(str(i) +"*"+ str(num) +"="+str(i*num))