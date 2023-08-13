from databaze import Databaze


class Menu:

    def __init__(self):
        self.databaze = Databaze()

    def vyber_akci(self):  # metoda umožní uživateli zvolit, co chce udělat
        while True:
            print("-----------------------\nEvidence pojištěných\n-----------------------")
            print("Vyberte si akci:")
            print("1 - přidat nového pojištěného")
            print("2 - vypsat všechny pojištěné")
            print("3 - vyhledat pojištěného")
            print("4 - konec")

            zvol = int(input())

            if zvol == 1:
                self.databaze.vstup_uzivatele()
            elif zvol == 2:
                print(self.databaze.zobraz_uzivatele())
            elif zvol == 3:
                self.databaze.vyhledat_uzivatele()
            elif zvol == 4:
                print("Děkujeme že používáte naši aplikaci")
                break  # Ukončí aplikaci
            else:
                print("Zvolil/a jste špatně, prosím zvolte ještě jednou")
