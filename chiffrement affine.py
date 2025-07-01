import math

def chiffrement_affine(texte_clair, a, b, m=26):
    if math.gcd(a, m) != 1:
        raise ValueError(f"Le coefficient 'a' doit être premier avec {m} (gcd = 1)")

    texte_clair = texte_clair.upper()
    texte_chiffre = ""

    for char in texte_clair:
        if char.isalpha():
            x = ord(char) - ord('A')
            y = (a * x + b) % m
            texte_chiffre += chr(y + ord('A'))
        else:
            texte_chiffre += char

    return texte_chiffre


texte = "HELLO WORLD"


resultat = chiffrement_affine(texte, a=5, b=8)

print("Texte chiffré :", resultat)
