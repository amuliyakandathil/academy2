from bs4 import BeautifulSoup
import requests
response=requests.get(" https://news.ycombinator.com/")
contents=response.text
soup=BeautifulSoup(contents,"html.parser")
headings=soup.find_all(class_="athing")
score=soup.find_all(class_="score")
link=soup.find_all(class_="sitestr")
all=headings[0:len(headings)]
print("The Headings are:")
for h1 in all:
    print(h1.getText())
all=score[0:len(score)]
print("The Scores are:")
for points in all:
    print(points.getText())
all=link[0:len(link)]
print("Links of the headings are:")
for anchor in all:
    print(anchor.getText())