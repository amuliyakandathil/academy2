st1 = input("Enter a string: ")
vowel_co=0
conse_co = 0
for c in st1:
    if (c == "A") or (c =="E") or (c =="I") or c =="O" or c == "U" or c =="a" or c =="e" or c =="i" or c =="o" or c =="u":
        vowel_co +=1
    else:
        conse_co+=1
        
print("The number of vowels is: " + str(vowel_co))
print("The number of consontess is: " + str(conse_co))