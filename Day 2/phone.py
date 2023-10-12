import re
def check(ph_no):
 text = ph_no
 pattern = re.compile(".?\d{3}.?\d{3}.?\d{4}")
 return pattern.match(text)
ph_no = input("Enter phone number to be checked")
if check(ph_no):
 print("Your mail is valid")
else:
    rint("Your mail is not valid")