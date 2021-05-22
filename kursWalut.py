import requests
import time

waluta = input("Jaka waluta Cię interesuje?\n  Wpisz PLN / GBP / USD\n")

r = requests.get('http://api.exchangeratesapi.io/v1/latest?access_key=533cdf6afa135f17eee3f59774fa657a')
text = r.text
pozycjaWaluty = text.find(waluta.upper())
pozycja = int(pozycjaWaluty)
cenaEUR = text[pozycja+5:pozycja+9]

pozycjaDaty = text.find('date')
data = int(pozycjaDaty)
wartoscDaty = text[data+7:data+17]

while 1 == 1:
    print("Aktualna cena Euro to:", cenaEUR, waluta)
    print("Data:", wartoscDaty)
    t = time.localtime()
    current_time = time.strftime("%H:%M:%S", t)
    print("Godzina:",current_time)
    time.sleep(15)