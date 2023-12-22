import random
from colorama import Fore, init, Back, Style
import time
import os

# Inicjalizacja colorama (bez tej linijki konsola po zakończeniu działania programu będzie zielona)
init(autoreset=True)

def losowy_kolor(czerwony, zolty):
    # Szansa na kolor zielony wynosi 100% - (czerwony + zolty),
    # a na czerwony, żółty po odpowiednich procentach
    wybor_koloru = random.choices(
        [Fore.GREEN, Fore.RED, Fore.YELLOW],
        weights=[100 - (czerwony + zolty), czerwony, zolty],
        k=1
    )
    return wybor_koloru[0]
def pieniek(spacje):
    text = "|"
    pieniek = f"{Back.RED}{Back.YELLOW}{text}{Style.RESET_ALL}"
    print(spacje +pieniek)
def rysuj_trojkat(wysokosc, czerwony, zolty):
    for i in range(1, wysokosc + 1):
        spacje = ' ' * (wysokosc - i)
        gwiazdki = ""
        for j in range(2 * i - 1):
            gwiazdki += losowy_kolor(czerwony, zolty) + '*'
        print(spacje + gwiazdki)

def rysuj_trojkat2(wysokosc, czerwony, zolty):
    for i in range(1, wysokosc + 1):
        if i == 1:
            gwiazdki2 = losowy_kolor(czerwony, zolty) + '*' * 3
        else:
            spacje2 = ' ' * (wysokosc - i)
            gwiazdki2 = ""
            for j in range(2 * i - 1):
                gwiazdki2 += losowy_kolor(czerwony, zolty) + '*'
            print(spacje2 + gwiazdki2)



# Wysokość trójkąta
wysokosc = int(input("Podaj wysokość każdego segmentu choinki (zalecane 6): "))
if wysokosc < 2:
    raise TypeError("Liczba jest nieprawidłowa")

# Szansa czerwonej lampki
czerwony = int(input('Podaj szansę na zaświecenie się czerwonej lampki (zalecane 10, min 1, max 49): '))
if czerwony > 49 or czerwony < 1:
    raise TypeError("Liczba jest nieprawidłowa")

# Szansa żółtej lampki
zolty = int(input('Podaj szansę na zaświecenie się źóltej lampki (zalecane 10, min 1, max 49): '))
if zolty > 49 or zolty < 1:
    raise TypeError("Liczba jest nieprawidłowa")
czas = float(input('Podaj czas po którym na choince ma zmienic się zapalenie lampek (sekundy, zalecane 0.5): '))
if czas < 0:
    raise TypeError("Liczba jest nieprawidłowa")


# Animacja choinki
while True:
    os.system('cls' if os.name == 'nt' else 'clear')  # Czyszczenie konsoli
    rysuj_trojkat(wysokosc, czerwony, zolty)
    rysuj_trojkat2(wysokosc, czerwony, zolty)
    pieniek(spacje=' ' * (wysokosc - 1))
    time.sleep(czas)  # czas po którym zmieni się klatka
