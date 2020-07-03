import hashlib, uuid
salt = hashlib.md5('user_sigin_kard_ba_gmail_bezar_bere_to'.encode()).hexdigest()
print(salt[0:-5]+salt[5:-8])
