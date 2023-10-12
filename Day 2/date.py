import re
date = input("Enter a date: ")
def check(date):
    pattern = re.compile("\d{2}\/\d{2}\/\d{4}")
    return pattern.match(date)
if check(date):
    print("Format Matched")
else:
    print("Format Not Matched")