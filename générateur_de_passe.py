import random
from time import sleep

print("-------------c'est ici -------le début de mon test---------")
def mot_passe():
    mot = [
        "a", "b", "c", "@", "K","!"
        "A", ";", ":", "Q", "r", "j",
        "#", ".", "9", "1", "+", "°"
    ]
    
    resultat = " "
    for i in range(12):
        x = random.choice(mot)
        
        resultat += x
        
    return resultat

if __name__ == "__main__":
    
    print("-------------le résultat de mon scripte--------------!")
    password = mot_passe()
    print(f"the password is: {password}")