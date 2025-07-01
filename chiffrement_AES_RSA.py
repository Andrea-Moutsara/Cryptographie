from Crypto.PublicKey import RSA
from Crypto.Cipher import AES, PKCS1_OAEP
from Crypto.Random import get_random_bytes
import base64

# Génération des clés RSA
def generer_cles_rsa():
    cle_rsa = RSA.generate(2048)
    cle_privee = cle_rsa.export_key()
    cle_publique = cle_rsa.publickey().export_key()
    return cle_privee, cle_publique

# Chiffrement hybride
def chiffrer(message, cle_publique_bytes):
    cle_aes = get_random_bytes(16)

    # AES
    cipher_aes = AES.new(cle_aes, AES.MODE_EAX)
    ciphertext, tag = cipher_aes.encrypt_and_digest(message.encode())

    # RSA
    cle_publique = RSA.import_key(cle_publique_bytes)
    cipher_rsa = PKCS1_OAEP.new(cle_publique)
    cle_aes_chiffree = cipher_rsa.encrypt(cle_aes)

    return {
        'cle_aes_chiffree': base64.b64encode(cle_aes_chiffree).decode(),
        'nonce': base64.b64encode(cipher_aes.nonce).decode(),
        'tag': base64.b64encode(tag).decode(),
        'ciphertext': base64.b64encode(ciphertext).decode()
    }

# Déchiffrement hybride
def dechiffrer(data, cle_privee_bytes):
    cle_privee = RSA.import_key(cle_privee_bytes)
    cipher_rsa = PKCS1_OAEP.new(cle_privee)
    cle_aes = cipher_rsa.decrypt(base64.b64decode(data['cle_aes_chiffree']))

    cipher_aes = AES.new(cle_aes, AES.MODE_EAX, nonce=base64.b64decode(data['nonce']))
    message = cipher_aes.decrypt_and_verify(
        base64.b64decode(data['ciphertext']),
        base64.b64decode(data['tag'])
    )

    return message.decode()

# Exécution
if __name__ == "__main__":
    message = input(" Entrez votre message confidentiel : ")

    cle_privee, cle_publique = generer_cles_rsa()

    # Chiffrement
    donnees_chiffrees = chiffrer(message, cle_publique)
    print("\n Message chiffré avec succès !")
    print("Données chiffrées :", donnees_chiffrees)

    # Déchiffrement
    message_dechiffre = dechiffrer(donnees_chiffrees, cle_privee)
    print("\n Message déchiffré :", message_dechiffre)
