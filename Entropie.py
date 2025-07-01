import math
from collections import Counter

def calculer_entropie(texte):
    n = len(texte)
    if n == 0:
        return 0
    freqs = Counter(texte)
    entropie = -sum((freq / n) * math.log2(freq / n) for freq in freqs.values())
    return entropie

def calculer_redondance(texte, alphabet_size=26):
    entropie = calculer_entropie(texte)
    if alphabet_size <= 1:
        return 0
    redondance = 1 - (entropie / math.log2(alphabet_size))
    return redondance

def indice_coincidence(texte):
    n = len(texte)
    if n <= 1:
        return 0
    freqs = Counter(texte)
    ic = sum(f * (f - 1) for f in freqs.values()) / (n * (n - 1))
    return ic

texte = "HELLO"

print("Entropie :", calculer_entropie(texte))
print("Redondance :", calculer_redondance(texte, alphabet_size=26))
print("Indice de coïncidence :", indice_coincidence(texte))
