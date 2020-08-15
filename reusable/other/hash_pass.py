import hashlib, uuid
salt = hashlib.md5('3d6c1bd47f109e34c02f08773f8bd47f109e34c02f0877'.encode()).hexdigest()
print(salt[0:-5]+salt[5:-8])
