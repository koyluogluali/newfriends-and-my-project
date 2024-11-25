import random
import time
from new_gravity import alone_man
seviyeler = {
    "kolay": ["dairy", "mouse", "computer"],
    "orta": ["programming", "algorithm", "developer"],
    "zor": ["neural network", "machine learning", "artificial intelligence"]    
}
while True:
    a = input("zorluğu seç (kolay,orta,zor,çıkış için:q)")

    #kelimeler = random.choice(seviyeler[a])
    if a == "kolay":
        e=random.choice(seviyeler["kolay"])
        print(e)
    elif a == "orta":
        e=random.choice(seviyeler["orta"])
        print(e)
    elif a == "zor":
        e=random.choice(seviyeler["zor"])
        print(e)
    elif a=="q":
        print ("çıktınız ama bu oyuna gireceksin yoksa kötü şeyler olur")
        break
    else:
        print("seviyeyi yanlış girdin")
    
