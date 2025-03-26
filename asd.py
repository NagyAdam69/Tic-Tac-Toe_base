felhasz = input("Felhasználónév: ")
jelszo = input("Jelszó: ")

fontos = []
with open("felhasznalok.txt", "r", encoding="utf-8") as forrasfajl:
    for sor in forrasfajl:
        adatok = sor.strip().split(";")
        felhasznalo = adatok[0]
        jelszo_file = adatok[1]
        pontszam = adatok[2]
        fontos.append((felhasznalo, jelszo_file, pontszam))

found = False
for felhasznalo, jelszo_file, pontszam in fontos:
    if felhasznalo == felhasz:
        found = True
        if jelszo == jelszo_file:
            print(f"Sikeres bejelentkezés! Pontszám: {pontszam}")
        else:
            print("Hibás jelszó!")
        break

if not found:
    print("A felhasználó nem létezik!")