from uzivatel import Uzivatel


class Databaze:

    def __init__(self):
        self.seznam_uzivatelu = []

    def vstup_uzivatele(self):  # Získává vstup od uživatele
        jmeno = input("Zadejte jméno pojištěného: \n")
        prijmeni = input("Zadejte příjmení: \n")
        vek = input("Zadejte věk: \n")
        telefon = input("Zadejte telefonní číslo: \n")
        uzivatel = Uzivatel(jmeno, prijmeni, vek, telefon)
        self.pridej_uzivatele(uzivatel)

    def pridej_uzivatele(self, uzivatel):  # Přidá uživatele do seznamu
        self.seznam_uzivatelu.append(uzivatel)
        print("Data byla uložena. Pokračujte libovolnou klávesou...")
        input()

    def zobraz_uzivatele(self):  # Zobrazí všechny uložené uživatele v seznamu
        if not self.seznam_uzivatelu:  # Pokud je seznam prázdný vrátí "Seznam je prázdný"
            return "Seznam je prázdný"
        else:
            uzivatele_info = []
            for uzivatel in self.seznam_uzivatelu:
                uzivatele_info.append(str(uzivatel))
            return "\n".join(uzivatele_info)

    def vyhledat_uzivatele(self):  # Po zadání jména a příjmení vypíše hledanou osobu
        hledane_jmeno = input("Zadejte jméno pojištěného:\n")
        hledane_prijmeni = input("Zadejte příjmení:\n")

        nalezeni_uzivatele = []
        for uzivatel in self.seznam_uzivatelu:
            if uzivatel.jmeno == hledane_jmeno and uzivatel.prijmeni == hledane_prijmeni:
                nalezeni_uzivatele.append(uzivatel)

        if nalezeni_uzivatele:
            for uzivatel in nalezeni_uzivatele:
                print(uzivatel)
        else:
            print("Neevidujeme pojištěnce s tímto jménem")
