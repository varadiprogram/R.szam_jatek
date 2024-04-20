import random

print("Gondolj egy számra 1-100ig és megpróbálom kitalálni, de ha 10bol egyszersem talalod ki akkor veszettél.\n")
gondolt_szam = random.randint(1, 100)
elet = 10

while True:
    te_szamod = int(input("Szám: "))
    print("Ennyi életed van: ", elet)

    if elet == 1:
        print("V E S Z T E T T É L!")
        print("Gondolt szám: ", gondolt_szam)
        break

    if te_szamod > gondolt_szam:
        print("A szám kisebb")
        elet = elet - 1
        print("Ennyi életed maradt: ", elet)

    elif te_szamod < gondolt_szam:
        print("A szám nagyobb")
        elet = elet - 1
        print("Ennyi életed maradt: ", elet)

    elif te_szamod == gondolt_szam:
        print("Gondolt szám: ", gondolt_szam)
        break
print("N Y E R T É L!!!")
