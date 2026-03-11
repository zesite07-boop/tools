#!/usr/bin/env python3
"""
Génère un fichier .htpasswd pour la protection par mot de passe.
Usage : python3 gen_htpasswd.py
"""
import hashlib, base64, getpass, os

def md5_crypt(password):
    """Format MD5 Apache ($apr1$)"""
    import crypt
    return crypt.crypt(password, crypt.mksalt(crypt.METHOD_MD5))

def sha1_htpasswd(user, password):
    """Format SHA1 (plus compatible partagé)"""
    sha1 = hashlib.sha1(password.encode('utf-8')).digest()
    b64 = base64.b64encode(sha1).decode('utf-8')
    return f"{user}:{{SHA}}{b64}"

user = input("Nom d'utilisateur [ra-btp] : ").strip() or "ra-btp"
pwd = getpass.getpass("Mot de passe : ")
pwd2 = getpass.getpass("Confirmer : ")

if pwd != pwd2:
    print("❌ Les mots de passe ne correspondent pas.")
    exit(1)

line = sha1_htpasswd(user, pwd)
fname = ".htpasswd"
with open(fname, 'w') as f:
    f.write(line + "\n")

print(f"\n✓ Fichier {fname} créé.")
print(f"  Ligne : {line}")
print(f"\nÀ uploader sur o2switch dans :")
print(f"  /home/clients/z3site/.htpasswd")
print(f"  (dossier PARENT du dossier tools/ — jamais dans le dossier public)")
