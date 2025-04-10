current_user = None

def get_current_user():
    global current_user
    return current_user

def regisztracio():
    while True:
        felhasz = input("Felhasználó: ")

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
                print("A felhasználó létezik!\n")
                return

        if not found:
            jelszo = input("Jelszó: ")
            try:
                with open("felhasznalok.txt", "a", encoding="utf-8") as forrasfajl:
                    forrasfajl.write(f"{felhasz};{jelszo};0\n")
                    forrasfajl.flush()
                print("\nSikeres regisztráció! Az adatok elmentve.")
                
            except Exception as e:
                print(f"Hiba történt az írás során: {e}")
            return 

def bejelentkezes():
    global current_user
    while True:
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
        for felhasznalo, jelszo_file, pontszam in fontos:
            if felhasznalo == felhasz:
                found = True
                jelszo = input("Jelszó: ")
                if jelszo == jelszo_file:
                    current_user = felhasz
                    print(f"\nSikeres bejelentkezés! Pontszám: {pontszam}")
                    return True
                else:
                    print("\nHibás jelszó!\n")
                pass

        if not found:
            print("A felhasználó nem létezik!")
            pass

def sign_or_log():
    jo = True

    while jo:
        sign_or_log = input("1. Bejelentkezés\n2. Regisztráció\n(1 vagy 2): ")

        if sign_or_log == "1":
            bejelentkezes()
            jo = False

        elif sign_or_log == "2":
            regisztracio()
            jo = False

        else:
            print("Hibás választás!")

