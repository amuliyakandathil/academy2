import re
text = input("Enter the text")
pattern = re.compile("<[^>]*>")
x = pattern.sub(text)
print(x)



