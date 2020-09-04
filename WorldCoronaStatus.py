import bs4
import requests
import re

exp = re.compile("(\d.*[0-9])")
country = str(input("Please Enter The Country(eg:india,china,russia,us,etc)\n> "))
base_url = f"https://www.worldometers.info/coronavirus/country/{country.lower()}/"
req = requests.get(base_url)
bs = bs4.BeautifulSoup(req.text, 'html.parser')
soup = bs.find_all("div", class_='maincounter-number')
a=[]
for i in soup:
    a.append(str(i))
res = []
for i in a:
    res+=exp.findall(i)
print("Active Cases " +res[0])
print("Death Cases " +res[1])
print("Recovered " +res[3])
