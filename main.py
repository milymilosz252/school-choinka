import random
from colorama import Fore, init

# Inicjalizacja colorama (bez tej linijki konsola po zakończeniu działania programu będzie zielona)
init(autoreset=True)

def losowy_kolor(czerwony, zolty):
    # Szansa na kolor zielony wynosi 100% - (czerwony + zolty),
    # a na czerwony, żółty po odpowiednich procentach
    wybor_koloru = random.choices(
        [Fore.GREEN, Fore.RED, Fore.YELLOW],
        weights=[100 - (czerwony + zolty ), czerwony, zolty],
        k=1
    )
    return wybor_koloru[0]

def rysuj_trojkat(wysokosc, czerwony, zolty):
    for i in range(1, wysokosc + 1):
        spacje = ' ' * (wysokosc - i)
        gwiazdki = ""
        for j in range(2 * i - 1):
            gwiazdki += losowy_kolor(czerwony, zolty) + '*'
        print(spacje + gwiazdki)

def rysuj_trojkat2(wysokosc, czerwony, zolty ):
    for i in range(1, wysokosc + 1):
        if i == 1:
            gwiazdki2 = losowy_kolor(czerwony, zolty) + '*' * 3
        else:
            spacje2 = ' ' * (wysokosc - i)
            gwiazdki2 = ""
            for j in range(2 * i - 1):
                gwiazdki2 += losowy_kolor(czerwony, zolty) + '*'
            print(spacje2 + gwiazdki2)

def rysuj_pienek(spacje):
    print(spacje + Fore.LIGHTBLACK_EX + "|")

# Wysokość trójkąta
wysokosc = int(input("Podaj wysokość każdego segmentu choinki: "))
if wysokosc < 2:
    raise TypeError("Liczba jest nieprawidłowa")

# Szansa czerwonej bombki
czerwony = int(input('Podaj szansę na pojawienie się czerwonej bombki (zalecane 20, min 1, max 49): '))
if czerwony > 49 or czerwony < 1:
    raise TypeError("Liczba jest nieprawidłowa")

# Szansa żółtej bombki
zolty = int(input('Podaj szansę na pojawienie się żółtej bombki (zalecane 20, min 1, max 49): '))
if zolty > 49 or zolty < 1:
    raise TypeError("Liczba jest nieprawidłowa")


# Wykonanie funkcji
rysuj_trojkat(wysokosc, czerwony, zolty)
rysuj_trojkat2(wysokosc, czerwony, zolty )
rysuj_pienek(spacje= ' ' * (wysokosc - 1))