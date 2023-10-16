from bs4 import BeautifulSoup
import requests
response=requests.get(" https://news.ycombinator.com/")
contents=response.text
soup=BeautifulSoup(contents,"html.parser")
headings=soup.find_all(class_="athing")
score=soup.find_all(class_="score")
link=soup.find_all(class_="sitestr")
all1=headings[0:len(headings)]
print("The Headings are:")
for h1 in all1:
    print(h1.getText())
all2=score[0:len(score)]
print("The Scores are:")
for points in all2:
    print(points.getText())
all3=link[0:len(link)]
print("Links of the headings are:")
for anchor in all3:
    print(anchor.getText())