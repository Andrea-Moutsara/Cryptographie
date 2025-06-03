# Fonction de chiffrement Vigenère
def chiffrer_vigenere(texte_clair, cle):
    resultat = ""
    cle = cle.lower()
    index_cle = 0

    for char in texte_clair:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            decalage = ord(cle[index_cle % len(cle)]) - ord('a')
            nouveau_char = chr((ord(char) - base + decalage) % 26 + base)
            resultat += nouveau_char
            index_cle += 1
        else:
            resultat += char
    return resultat

# Fonction de déchiffrement Vigenère
def dechiffrer_vigenere(texte_chiffre, cle):
    resultat = ""
    cle = cle.lower()
    index_cle = 0

    for char in texte_chiffre:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            decalage = ord(cle[index_cle % len(cle)]) - ord('a')
            nouveau_char = chr((ord(char) - base - decalage) % 26 + base)
            resultat += nouveau_char
            index_cle += 1
        else:
            resultat += char
    return resultat

# ----------------------------
# Partie interactive

# Chiffrement
texte_clair = input("Entrez le texte à chiffrer : ")
cle_chiffrement = input("Entrez la clé de chiffrement : ")

texte_chiffre = chiffrer_vigenere(texte_clair, cle_chiffrement)
print("\nTexte chiffré :", texte_chiffre)

# Déchiffrement
texte_chiffre_a_dechiffrer = input("\nEntrez le texte chiffré à déchiffrer : ")
cle_dechiffrement = input("Entrez la clé de déchiffrement : ")

texte_dechiffre = dechiffrer_vigenere(texte_chiffre_a_dechiffrer, cle_dechiffrement)
print("Texte déchiffré :", texte_dechiffre)
