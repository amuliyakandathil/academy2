import re
def check(mail):
 text = mail
 pattern = re.compile("\w*@(?!hotmail|yahoo)\w*.[coi][orn][mg]")
 return pattern.match(text)
mail =input("Enter your mail: ")
if check(mail):
 print("Your mail is valid")
else:
 print("Your mail is not valid")
