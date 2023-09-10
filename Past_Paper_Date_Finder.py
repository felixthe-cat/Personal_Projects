import re

additional_txt = input("Anything you wanna add before the data: ")
with open('past_paper.txt','r') as f: 
    txt = f.read()
date = re.compile("[0-9]+-[0-9]+-[0-9]+")
for match in date.finditer(txt):
    print(additional_txt + ' ' + match.group(0))

quit()

txt = txt.split('\n')
for line in txt:
    date = re.search("[0-9]+-[0-9]+-[0-9]+", line)
    date = date.group()
    print(date)
for item in date:
    print(item)
