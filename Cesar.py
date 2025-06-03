# Fonction de chiffrement
def chiffrer_cesar(texte_clair, decalage):
    resultat = ""
    for char in texte_clair:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            resultat += chr((ord(char) - base + decalage) % 26 + base)
        else:
            resultat += char
    return resultat

# Fonction de déchiffrement
def dechiffrer_cesar(texte_chiffre, decalage):
    return chiffrer_cesar(texte_chiffre, -decalage)

# ---------------------------
# Partie interactive

# Saisie du texte clair et du décalage
texte_clair = input("Entrez le texte à chiffrer : ")
while True:
    try:
        decalage = int(input("Entrez le décalage (nombre entier) : "))
        break
    except ValueError:
        print("Erreur : veuillez entrer un nombre entier.")

# Chiffrement
texte_chiffre = chiffrer_cesar(texte_clair, decalage)
print("\nTexte chiffré :", texte_chiffre)

# Saisie du texte chiffré pour déchiffrement
texte_a_dechiffrer = input("\nEntrez un texte chiffré à déchiffrer : ")
texte_dechiffre = dechiffrer_cesar(texte_a_dechiffrer, decalage)
print("Texte déchiffré :", texte_dechiffre)
