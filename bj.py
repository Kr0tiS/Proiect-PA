import random
import tkinter as tk
from tkinter import messagebox

# Valorile cărților
VALORI_CARTI = {
    '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10,
    'J': 10, 'Q': 10, 'K': 10, 'A': 11  # Asul începe ca 11
}

#Pachet de carti
class JocBlackjack:
    def __init__(self, radacina):
        self.radacina = radacina
        self.radacina.title("Joc de Blackjack")
        self.pachet = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A'] * 4
        random.shuffle(self.pachet)

        self.mana_jucator = []
        self.mana_dealer = []

        # Configurare GUI
        self.eticheta_jucator = tk.Label(radacina, text="Mâna ta: ", font=("Arial", 14))
        self.eticheta_jucator.pack()

        self.eticheta_dealer = tk.Label(radacina, text="Mâna dealerului: ", font=("Arial", 14))
        self.eticheta_dealer.pack()

        self.eticheta_rezultat = tk.Label(radacina, text="", font=("Arial", 16, "bold"))
        self.eticheta_rezultat.pack()

        self.buton_hit = tk.Button(radacina, text="Cere carte", command=self.jucator_cere_carte, font=("Arial", 12))
        self.buton_hit.pack(side=tk.LEFT, padx=20, pady=20)

        self.buton_stand = tk.Button(radacina, text="Stai", command=self.jucator_stai, font=("Arial", 12))
        self.buton_stand.pack(side=tk.RIGHT, padx=20, pady=20)

        self.porneste_jocul()

    def porneste_jocul(self):
        self.mana_jucator = [self.extrage_carte(), self.extrage_carte()]
        self.mana_dealer = [self.extrage_carte(), self.extrage_carte()]
        self.actualizeaza_etichete()

    def extrage_carte(self):
        return self.pachet.pop()

    def calculeaza_valoare_mana(self, mana):
        valoare = sum(VALORI_CARTI[carte] for carte in mana)
        asi = mana.count('A')
        while valoare > 21 and asi:
            valoare -= 10
            asi -= 1
        return valoare

    def actualizeaza_etichete(self):
        valoare_jucator = self.calculeaza_valoare_mana(self.mana_jucator)
        carte_dealer_vizibila = self.mana_dealer[0]

        self.eticheta_jucator.config(text=f"Mâna ta: {self.mana_jucator} (Valoare: {valoare_jucator})")
        self.eticheta_dealer.config(text=f"Mâna dealerului: [{carte_dealer_vizibila}, ?]")

    def jucator_cere_carte(self):
        self.mana_jucator.append(self.extrage_carte())
        valoare_jucator = self.calculeaza_valoare_mana(self.mana_jucator)
        self.actualizeaza_etichete()

        if valoare_jucator > 21:
            self.finalizeaza_jocul("Ai depășit 21! Dealerul câștigă.")

    def jucator_stai(self):
        valoare_dealer = self.calculeaza_valoare_mana(self.mana_dealer)
        while valoare_dealer < 17:
            self.mana_dealer.append(self.extrage_carte())
            valoare_dealer = self.calculeaza_valoare_mana(self.mana_dealer)

        self.verifica_castigator()

    def verifica_castigator(self):
        valoare_jucator = self.calculeaza_valoare_mana(self.mana_jucator)
        valoare_dealer = self.calculeaza_valoare_mana(self.mana_dealer)

        self.eticheta_dealer.config(text=f"Mâna dealerului: {self.mana_dealer} (Valoare: {valoare_dealer})")

        if valoare_dealer > 21:
            self.finalizeaza_jocul("Dealerul a depășit 21! Ai câștigat.")
        elif valoare_dealer > valoare_jucator:
            self.finalizeaza_jocul("Dealerul câștigă.")
        elif valoare_dealer < valoare_jucator:
            self.finalizeaza_jocul("Ai câștigat!")
        else:
            self.finalizeaza_jocul("Este egalitate!")

    def finalizeaza_jocul(self, rezultat):
        self.eticheta_rezultat.config(text=rezultat)
        self.buton_hit.config(state=tk.DISABLED)
        self.buton_stand.config(state=tk.DISABLED)
        messagebox.showinfo("Sfârșitul jocului", rezultat)

# Rulează GUI-ul
if __name__ == "__main__":
    radacina = tk.Tk()
    joc = JocBlackjack(radacina)
    radacina.mainloop()