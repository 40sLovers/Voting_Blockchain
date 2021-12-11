from hashlib import sha256
from datetime import datetime
def updatehash(*args):
    hashing = ""
    h = sha256()
    for arg in args:
        hashing += str(arg)
    h.update(hashing.encode('utf-8'))
    return h.hexdigest()
