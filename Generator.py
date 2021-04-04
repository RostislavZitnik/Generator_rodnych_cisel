pohlavi = input("Pohlavi (m/ž): ")
if pohlavi.lower() not in ("m", "ž"):  #pohlavi pouze "m" a nebo "ž"
    print("Neplatny vstup")
    print("Ukončuji")
    quit()

den = input("Den narozeni (01 - 31): ")
if not 0 < int(den) < 32 or not den.isnumeric():  #den narozeni od 1 do 31
    print("Neplatny vstup")
    print("Ukončuji")
    quit()

delka = {1: "31", 2: "29", 3: "31", 4: "30", 5: "31", 6: "30", 7: "31", 8: "31", 9: "30", 10: "31", 11: "30", 12: "31"}
mesic = input("Mesic narozeni (1 - 12): ")
if not 0 < int(mesic) < 13 or not mesic.isnumeric():  #mesic od 1 do 12, muze byt zadano pouze cislo
    print("Neplatny vstup")
    print("Ukončuji")
    quit()
elif int(den) > int(delka.get(int(mesic))):  #kontrola dne narozeni vs. pocet dni v mesici
    print("Tento mesic nema tolik dni")
    print("Ukončuji")
    quit()

rok = input("Rok narozeni (19xx - 20xx): ")
if not len(rok) == 4 or not rok.isnumeric() or rok[0:2] not in ("19", "20"):  #pocet znaku, vlozeno cislo, zacina 19,20
    print("Neplatny vstup")
    print("Ukončuji")
    quit()
elif int(mesic) == 2 and int(den) == 29 and not int(rok) % 4 == 0:  #kontrola prestupneho roku
    print("Toto neni prestupny rok")
    quit()

if len(mesic) == 1: #kontrola formatu mesice
    mesic = ("0" + mesic)

if pohlavi.lower() == "m":
    print("Narodil jsi se", den + "." + mesic + "." + rok)
    rodnecislo = rok[-2:] + mesic + den + "/XXXX"
    print("Tvoje rodne cislo je:", rodnecislo)

if pohlavi.lower() == "ž":
    print("Narodila jsi se", den + "." + mesic + "." + rok)
    mesic = int(mesic) + 50
    rodnecislo = rok[-2:] + str(mesic) + den + "/XXXX"
    print("Tvoje rodne cislo je:", rodnecislo)
