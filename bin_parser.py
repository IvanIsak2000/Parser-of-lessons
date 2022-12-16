import requests 
from bs4 import BeautifulSoup
bin_ = ("https://bincol.ru/rasp/view.php?id=00294")
headers ={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36 Edg/107.0.1418.62"}
full_page = requests.get(bin_, headers=headers)	
soup = BeautifulSoup(full_page.content, 'html.parser')
convert = soup.findAll("tr",{"class":"shadow"})
s =""
for string in convert:
    s+=string.getText()+"\n"


print(s)
