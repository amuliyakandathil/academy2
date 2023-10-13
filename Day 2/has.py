import re

text = '''
Exploring the serene forest trails, connecting with nature and finding inner peace. #NatureWalks #Mindfulness #Serenit
'''

x = re.compile("[#]\w*")
print(x.findall( text))