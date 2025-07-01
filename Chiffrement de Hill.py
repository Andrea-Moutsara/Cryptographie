import numpy as np

def hill_chiffrement(texte_clair, matrice_cle, modulo=26):
    texte_clair = texte_clair.upper().replace(" ", "")
    n = matrice_cle.shape[0]

    while len(texte_clair) % n != 0:
        texte_clair += 'X'  

    # Convertir le texte en blocs numériques
    blocs = [
        [ord(c) - ord('A') for c in texte_clair[i:i+n]]
        for i in range(0, len(texte_clair), n)
    ]

    texte_chiffre = ""

    for bloc in blocs:
        vecteur = np.array(bloc).reshape(n, 1)
        chiffré = np.dot(matrice_cle, vecteur) % modulo
        texte_chiffre += ''.join(chr(int(num) + ord('A')) for num in chiffré)

    return texte_chiffre

cle = np.array([[3, 3],
               [2, 5]])

texte = "HELLO"
resultat = hill_chiffrement(texte, cle)
print("Texte chiffré :", resultat)
