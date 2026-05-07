class Gestionnaire_alcool:
    def __init__(self, soda, bière, liqueurs, prix = 0):
        self.soda = soda
        self.bière = bière 
        self.liqueurs = liqueurs
        self.prix = 0

    @property
    def prix(self):
        return self._prix

    @prix.setter
    def prix(self, valeur):
        if valeur < 0:
            raise ValueError (f"le prix ne peut etre négatif")
        self._prix = valeur

    def quantité_alcool(self, volume):
        if volume <= 4.5:
            return f'la quantité voulu de {self.volume}vol à été atteinte'
        else:
            return f" ce n'est pas la bonne quantité d'alcool"
        
    def choisir_boisson(self, boisson):
        if boisson == "soda": 
            return f"envoi un {self.soda}"
        elif boisson == "bière":
                       return f"envoi une {self.bière}"
        elif boisson == "liqueurs":
            return f"c'est un boisson forte, envoi une {self.liqueurs}"
        else:
            print("cette boisson n'est pas disponible")

if __name__ == "__main__":
    # Initialisation
    gestionnaire = Gestionnaire_alcool("Coca", "Heineken", "Whisky")
    
    # Test du choix
    print(gestionnaire.choisir_boisson("biere"))
    print("-" * 30)

    # Gestion des prix
    try:
        gestionnaire.prix = 750
        print(f"Le prix mis à jour est de : {gestionnaire.prix} FCFA")
        
        # Test de l'erreur de prix
        # gestionnaire.prix = -100 
    except ValueError as e:
        print(e) 