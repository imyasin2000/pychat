import hashlib, uuid
salt = hashlib.md5('pwd'.encode()).hexdigest()
print(salt[0:-5]+salt[5:-8])
