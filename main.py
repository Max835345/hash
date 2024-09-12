import hashlib
import uuid

hash = hashlib.md5()


s = input()
hash.update(s.encode('utf-8'))
password = hash.hexdigest()


h = hashlib.md5()
password_true = "password"
h.update(password_true.encode('utf-8'))
password_true = h.hexdigest()

if password == password_true:
    print("Open")
else:
    print("Close")
