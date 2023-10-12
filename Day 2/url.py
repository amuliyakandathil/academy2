import re
url =  input("Enter URL")
pattern = re.compile("https?://(www\.)?([^/]+)")
x = pattern.search(url)
  

if x:
    domains = x.group(2)
    print(domains)