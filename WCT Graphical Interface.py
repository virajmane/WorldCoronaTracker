import bs4
import requests
from tkinter import *

window = Tk()
window.title("Corona")
window.geometry("440x440+0+0")

exp = re.compile("(\d.*[0-9])")
def tracker():
    country = textfield.get()
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
    Label(window, text=f"Country: {country}\nActive Cases: {res[0]}\nDeath Cases: {res[1]}\nRecovered: {res[3]}\n").pack()

textfield = StringVar()
Label(window, text="World Corona Status").pack()
Entry(window, textvariable=textfield).pack()
Button(window,text="Search",command=lambda :tracker()).pack()
window.mainloop()
