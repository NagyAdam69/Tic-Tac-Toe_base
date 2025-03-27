def bejelentkezes():
    while True:
        while True:
            felhasz = ""
            felhasz = input("Felhasználónév: ")

            fontos = []
            with open("felhasznalok.txt", "r", encoding="utf-8") as forrasfajl:
                for sor in forrasfajl:
                    adatok = sor.strip().split(";")
                    felhasznalo = adatok[0]
                    jelszo_file = adatok[1]
                    pontszam = adatok[2]
                    fontos.append((felhasznalo, jelszo_file, pontszam))

            found = False
            for felhasznalo, jelszo_fasdile, pontszam in fontos:
                if felhasznalo == felhasz:
                    found = True
                    jelszo = input("Jelszó: ")
                    if jelszo == jelszo_file:
                        print(f"Sikeres bejelentkezés! Pontszám: {pontszam}")
                        exit()
                    else:
                        print("Hibás jelszó!")
                        break
                    break

            if not found:
                print("A felhasználó nem létezik!")
                break
while True:
    while True:
        sign_or_log = input("1. Bejelentkezés\n2. Regisztráció\n(1 vagy 2): ")

        if sign_or_log == "1":
            bejelentkezes() 
            exit()

        elif sign_or_log == "2":
            regisztracio()
            exit()
        else:
            print("Hibás bejelentkezés!")
            break
