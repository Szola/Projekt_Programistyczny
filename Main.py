# Implementacja narzędzia do konwersji pomiędzy podstawowymi formatami zapisu struktur drugorzędowych RNA.

import linecache


def min(a, b):
    if (a < b):
        return a
    else:
        return b


def max(a, b):
    if (a > b):
        return a
    else:
        return b


# =============Funkcje sprawdzajace format ================================================

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
        if (len(nuk) == 0):
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
        if (
                                            i != '.' and i != '(' and i != ')' and i != '{' and i != '}' and i != '[' and i != ']' and i != '<' and i != '>'):
            wynik = 0
    return wynik


def czy_CT():
    wynik = 1
    dl = linecache.getline(nazwa_czasteczki, 1)
    dl = dl.strip()
    if (len(dl) > 3):
        print("jehehehehhe")
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


# =============Funkcje sprawdzajace do czego konwertowac ==================================

def do_DotBracket():
    if (czy_BPseq() == 1):
        z_BPseq_do_DotBracket()
    elif (czy_DotBracket() == 1):
        print("To już jest notacja dot-brakcet ")
    elif (czy_CT() == 1):
        z_CT_do_DotBracket()
    else:
        print("Błędne wejście")


def do_CT():
    if (czy_BPseq() == 1):
        z_BPseq_do_CT()
    elif (czy_DotBracket() == 1):
        z_DotBracket_do_CT()
    elif (czy_CT() == 1):
        print("To już jest notacja CT")
    else:
        print("Błędne wejście")


def do_BPseq():
    if (czy_BPseq() == 1):
        print("To już jest notacja bpseq")
    elif (czy_DotBracket() == 1):
        z_DotBracket_do_BPseq()
    elif (czy_CT() == 1):
        z_CT_do_BPseq()
    else:
        print("Błędne wejście")


# =============Funkcje konwertujace ========================================================

def z_BPseq_do_DotBracket():
    wynik_sek = []
    wynik_kn = []
    nuk = linecache.getline(nazwa_czasteczki, 1)
    nuk = nuk.split()

    i = 1
    nr_nuk = int(nuk[0]);
    while (i == nr_nuk):
        i = i + 1
        nuk = linecache.getline(nazwa_czasteczki, i)
        if (len(nuk) == 0):
            nr_nuk = 0
        else:
            nr_nuk = int(nuk[0]);
    dl = i-1

    i = 0
    while (i < dl):
        wynik_sek.append(".")
        wynik_kn.append(".")
        i = i + 1

    i = 0
    j = 0
    while (i < dl * 6):
        wynik_sek[j] = tekst[i + 2]
        i = i + 6
        j = j + 1

    i = 0
    while (i < dl * 6):
        j = 0
        while (j < dl * 6):
            licz = j + 4
            if (tekst[licz] == tekst[i]):
                wynik_kn[min(int(tekst[i]) - 1, int(tekst[j]) - 1)] = "("
                wynik_kn[max(int(tekst[i]) - 1, int(tekst[j]) - 1)] = ")"
            j = j + 6
        i = i + 6

    print("Konwersja do Dot-Bracket: ")
    print("".join(wynik_sek))
    print("".join(wynik_kn))


def z_BPseq_do_CT():
    nuk = linecache.getline(nazwa_czasteczki, 1)
    nuk = nuk.split()

    i = 1
    nr_nuk = int(nuk[0]);
    while (i == nr_nuk):
        i = i + 1
        nuk = linecache.getline(nazwa_czasteczki, i)
        if (len(nuk) == 0):
            nr_nuk = 0
        else:
            nr_nuk = int(nuk[0]);
    dl = i - 1

    i = 0
    tab = []
    while (i < (12 * dl + 2)):
        tab.append(' ')
        i = i + 1

    tab[0] = dl
    i = 0
    j = 0
    while (i < 12 * dl):
        tab[i + 2] = tekst[j]
        tab[i + 4] = tekst[j + 2]
        if (int(tekst[j]) == 1):
            tab[i + 6] = 0
        else:
            tab[i + 6] = int(tekst[j]) - 1
        if (int(tekst[j]) == dl):
            tab[i + 8] = 0
        else:
            tab[i + 8] = int(tekst[j]) + 1
        tab[i + 10] = tekst[j + 4]
        tab[i + 12] = tekst[j]
        i = i + 12
        j = j + 6

    print("Konwersja do CT: ")
    i = 0
    print(tab[0])
    while (i < 12 * dl):
        print(tab[i + 2], tab[i + 4], tab[i + 6], tab[i + 8], tab[i + 10], tab[i + 12])
        i = i + 12


def z_CT_do_BPseq():
    dl = int(tekst[0])
    tab = []
    i = 0
    while (i < dl * 6):
        tab.append('')
        i = i + 1

    i = 0
    j = 0
    while (i < dl * 6):
        tab[i] = tekst[j + 2]
        tab[i + 2] = tekst[j + 4]
        tab[i + 4] = tekst[j + 10]
        i = i + 6
        j = j + 12

    i = 0
    print("Konwersja do BPSeq: ")
    while (i < 6 * dl):
        print(tab[i], tab[i + 2], tab[i + 4])
        i = i + 6


def z_CT_do_DotBracket():
    wynik_sek = []
    wynik_kn = []
    dl = int(tekst[0])

    i = 0
    while (i < dl):
        wynik_sek.append(".")
        wynik_kn.append(".")
        i = i + 1

    i = 0
    j = 0
    while (j < dl):
        wynik_sek[j] = tekst[i + 4]
        i = i + 12
        j = j + 1

    z = 0
    i = 0
    while (z < dl):
        licz1 = i + 2
        j = 0
        y = 0
        while (y < dl):
            licz2 = j + 10
            if (tekst[licz1] == tekst[licz2]):
                wynik_kn[min(int(tekst[i+2])-1, int(tekst[j+2])-1)] = "("
                wynik_kn[max(int(tekst[i+2])-1, int(tekst[j+2])-1)] = ")"
            j = j + 12
            y = y + 1
        i = i + 12
        z = z + 1

    print("Konwersja do Dot-Bracket: ")
    print("".join(wynik_sek))
    print("".join(wynik_kn))


def z_DotBracket_do_BPseq():
    sek = linecache.getline(nazwa_czasteczki, 1)
    kn = linecache.getline(nazwa_czasteczki, 2)
    kn2 = kn
    dl = len(sek) - 1
    tab = []
    i = 0

    while (i < dl * 6):
        tab.append('-')
        i = i + 1

    i = 0
    j = 0

    while (i < dl * 6):
        tab[i] = j + 1
        tab[i + 2] = sek[j]
        i = i + 6
        j = j + 1

    i = 0
    j = 0
    while (i<6*dl):
        if (kn[j] == "."):
            tab[i + 4] = 0
        i = i + 6
        j = j + 1


    i = 0
    print("Konwersja do BPSeq: ")
    while (i < 6 * dl):
        print(tab[i], tab[i + 2], tab[i + 4])
        i = i + 6


def z_DotBracket_do_CT():
    sek = linecache.getline(nazwa_czasteczki, 1)
    kn = linecache.getline(nazwa_czasteczki, 2)
    kn2 = kn

    dl = len(sek) - 1

    tab = []
    i = 0

    while (i < (12 * dl + 2)):
        tab.append('-')
        i = i + 1

    tab[0] = dl

    i = 0
    j = 0
    while (i < 12 * dl):
        tab[i + 2] = j + 1
        tab[i + 4] = sek[j]
        if (j + 1 == 1):
            tab[i + 6] = 0
        else:
            tab[i + 6] = j
        if (j + 1 == dl):
            tab[i + 8] = 0
        else:
            tab[i + 8] = j + 2
        tab[i + 12] = j + 1
        i = i + 12
        j = j + 1

    i = 0
    j = 0
    while (i<12*dl):
        if (kn[j] == "."):
            tab[i + 10] = 0
        i = i + 12
        j = j + 1

    print("Konwersja do CT: ")
    i = 0
    print(tab[0])
    while (i < 12 * dl):
        print(tab[i + 2], tab[i + 4], tab[i + 6], tab[i + 8], tab[i + 10], tab[i + 12])
        i = i + 12


# =============Program ====================================================================

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

    print("Orginalny plik: ")
    print(tekst)

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
