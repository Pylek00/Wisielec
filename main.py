import random
import sys
import os
import string
game_state = True
play_state = False
P_LATWY = 8
P_NORMALNY = 5
P_TRUDNY = 3
pawel = "pawel"

def wybor_hasla():
    print("Losowanie hasła...")
    lista_hasel=[]
    file = open("hasla.txt", "r")
    for line in file:
        lista_hasel.append(line.strip())
    file.close()

    haslo = random.choice(lista_hasel)
    return haslo

def wyswietl_menu():
    choice = -1
    while choice == -1:

        print("\nWITAJ W GRZE WISIELEC")
        print("1.Zagraj")
        print("2.Wyjdź\n")
        try:
            choice = int(input("Wybierz jedną z opcji: "))
        except:
            print("Podano nieodpowiednia wartosc!")
            choice = -1
        if choice == 1:
            return True
        elif choice == 2:
            return False
        else:
            print("Nie ma takiej wartosci!")
            choice = -1


def wybierz_poziom_trudnosci():
    difficulty = -1
    while difficulty == -1:

        print("Wybierz poziom trudności:")
        print("1. Łatwy")
        print("2. Normalny")
        print("3. Trudny")
        try:
            difficulty = int(input("Poziom trudności: "))
        except:
            print("Podano niepoprawną wartosc!")
            continue
        if difficulty == 1:
            return P_LATWY
        elif difficulty == 2:
            return P_NORMALNY
        elif difficulty == 3:
            return P_TRUDNY
        else:
            print("Nie podano zadnej z powyzszych odpowiedzi!")
            difficulty = -1


def rozgrywka(liczba_szans, haslo):
    play_state = True
    lista_podanych_liter = []
    lista_hasla = []
    for litera in haslo:
        lista_hasla.append("_")

    print("GRA SIĘ ROZPOCZĘŁA!!!")
    while play_state is True:
        print("Obecny stan: " + str(lista_hasla))
        print("Liczba szans: " + str(liczba_szans))
        print("Lista podanych liter(lub nie): " + str(lista_podanych_liter))

        try:
            literka = input("Podaj literę: ")
            print("---------------------------")
        except:
            print("Cos poszlo nie tak")
        finally:
            if len(literka) != 1:
                print("To nie jest jedna litera")
            elif string.ascii_lowercase.__contains__(literka) == False and string.ascii_uppercase.__contains__(literka) == False:
                print("To nie jest litera.")
                continue
            else:
                literka = literka.lower()
                if lista_podanych_liter.__contains__(literka) is False :

                    lista_podanych_liter.append(literka)
                else:
                    print("Ta litera juz zostala podana...")
                    continue
                if haslo.__contains__(literka) is False:
                    liczba_szans -= 1
                    print("Nie udało się odgadnąć litery.")
                else:
                    print("Gratulacje! Odgadłeś literę.")
                    index = 0

                    for litera in haslo:
                        if literka == haslo[index]:
                            lista_hasla[index] = literka
                        index += 1

        if liczba_szans == 0:
            print("Niestety nie udalo się. Hasłem było: "+str(haslo))
            play_state = False
        elif "".join(lista_hasla) == haslo:
            print("Gratulację odgadłeś hasło: "+ str(haslo))
            play_state = False



def game_loop():
    while game_state is True:
        if wyswietl_menu() is True:
            poziom_trudnosci = wybierz_poziom_trudnosci()
            rozgrywka(poziom_trudnosci, wybor_hasla())
        else:
            break
    print("Gra sie zakonczyla")



game_loop()
sys.exit(0)
