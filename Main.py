# Implementacja narzędzia do konwersji pomiędzy podstawowymi formatami zapisu struktur drugorzędowych RNA.

import linecache

#=============Funkcje sprawdzajace format ================================================

def czy_BPseq():
    wynik = 1
    nuk = linecache.getline(nazwa_czasteczki, 1)
    nuk = nuk.split()
    if (len(nuk) != 3):
        return 0

    i = 1
    nr_nuk = int(nuk[0]);
    while (i == nr_nuk):
        i = i + 1
        nuk = linecache.getline(nazwa_czasteczki, i)
        if (len(nuk)==0):
            nr_nuk = 0
        else:
            nr_nuk = int(nuk[0]);
    dl = i
    i = 1
    while (i < dl):
        nuk = linecache.getline(nazwa_czasteczki, i)
        nuk = nuk.split()
        if (int(nuk[0]) < 1 and int(nuk[0]) > dl):
            wynik = 0
        if (int(nuk[2]) < 1 and int(nuk[2]) > dl):
            wynik = 0
        if (nuk[1] != 'A' and nuk[1] != 'C' and nuk[1] != 'G' and nuk[1] != 'U'):
            wynik = 0
        i = i + 1

    return wynik

def czy_DotBracket():
    wynik = 1
    sek = linecache.getline(nazwa_czasteczki, 1)  # wyciaganie pojedynczych linijek
    kn = linecache.getline(nazwa_czasteczki, 2)
    sek = sek.strip()  # usuwanie bialych znakow
    kn = kn.strip()
    for i in sek:
        if (i != 'A' and i != 'C' and i != 'G' and i != 'U'):
            wynik = 0
    for i in kn:
        if (i != '.' and i != '(' and i != ')' and i != '{' and i != '}' and i != '[' and i != ']'):
            wynik = 0
    return wynik

def czy_CT():
    wynik = 1
    dl = linecache.getline(nazwa_czasteczki, 1)
    dl = dl.strip()
    if (len(dl) != 1):
        return 0
    dl = dl.strip()
    i = 2
    while (i < int(dl) + 2):
        nuk = linecache.getline(nazwa_czasteczki, i)
        nuk = nuk.split()
        if (int(nuk[0]) < 1 and int(nuk[0]) > int(dl) + 2):
            wynik = 0
        if (int(nuk[2]) < 1 and int(nuk[2]) > int(dl) + 2):
            wynik = 0
        if (int(nuk[3]) < 0 and int(nuk[3]) > int(dl) + 2):
            wynik = 0
        if (int(nuk[4]) < 0 and int(nuk[4]) > int(dl) + 2):
            wynik = 0
        if (int(nuk[5]) < 1 and int(nuk[5]) > int(dl) + 2):
            wynik = 0
        if (nuk[1] != 'A' and nuk[1] != 'C' and nuk[1] != 'G' and nuk[1] != 'U'):
            wynik = 0
        i = i + 1
    return wynik

def sprawdzanie_formatu():
    if (czy_BPseq() == 1):
        print("Jest to notacja bpseq")
    elif (czy_DotBracket() == 1):
        print("Jest to notacja dot-brakcet ")
    elif (czy_CT() == 1):
        print("Jest to notacja CT")
    else:
        print("Błędne wejście")

#=============Funkcje sprawdzajace do czego konwertowac ==================================

def do_DotBracket ():
    if (czy_BPseq() == 1):
        z_BPseq_do_DotBracket()
    elif (czy_DotBracket() == 1):
        print("To już jest notacja dot-brakcet ")
    elif (czy_CT() == 1):
        z_CT_do_DotBracket()
    else:
        print("Błędne wejście")

def do_CT ():
    if (czy_BPseq() == 1):
        z_BPseq_do_CT()
    elif (czy_DotBracket() == 1):
        z_DotBracket_do_CT()
    elif (czy_CT() == 1):
        print("To już jest notacja CT")
    else:
        print("Błędne wejście")

def do_BPseq ():
    if (czy_BPseq() == 1):
        print("To już jest notacja bpseq")
    elif (czy_DotBracket() == 1):
        z_DotBracket_do_BPseq()
    elif (czy_CT() == 1):
        z_CT_do_BPseq()
    else:
        print("Błędne wejście")

#=============Funkcje konwertujace ========================================================

def z_BPseq_do_DotBracket ():
    return 0

def z_BPseq_do_CT ():
    return 0

def z_CT_do_BPseq ():
    return 0

def z_CT_do_DotBracket ():
    return 0

def z_DotBracket_do_BPseq ():
    return 0

def z_DotBracket_do_CT ():
    return 0

#=============Program ====================================================================

print("Czy chcesz zakończyć działanie programu? 0/tak 1/nie")
wejscie = input()
odp = int(wejscie)

while odp == 1:

    print("Wybierz dzialanie programu: ")
    print("Sprawdzenie formatu czasteczki: 1 ")
    print("Konwersja do formatu CT: 2")
    print("Konwersja do formatu DotBracket: 3")
    print("Konwersja do formatu BPseq: 4")
    print("Konwersja do pozostalych formatow: 5")

    wejscie = input()
    dzialanie = int(wejscie)

    print("Podaj nazwe czasteczki/pliku: ")

    nazwa_czasteczki = input()
    nazwa_czasteczki = nazwa_czasteczki + ".txt"

    plik = open(nazwa_czasteczki, 'r')

    try:
        tekst = plik.read()
    finally:
        plik.close()

    if (dzialanie == 1):
        sprawdzanie_formatu()
    elif (dzialanie == 2):
        do_CT()
    elif (dzialanie == 3):
        do_DotBracket()
    elif (dzialanie == 4):
        do_BPseq()
    elif (dzialanie == 5):
        do_BPseq()
        do_DotBracket()
        do_CT()

    print("Czy chcesz zakończyć działanie programu? 0/tak 1/nie")
    wejscie = input()
    odp = int(wejscie)

