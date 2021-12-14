from hashlib import sha256
from datetime import datetime
from ecpy.keys       import ECPublicKey, ECPrivateKey
from ecpy.curves     import Curve,Point

def updatehash(*args):
    hashing = ""
    h = sha256()
    for arg in args:
        hashing += str(arg)
    h.update(hashing.encode('utf-8'))
    return h.hexdigest()


def keyFromHash(hash):
    cv= Curve.get_curve('secp256k1')
    hashInteger=hash.encode('utf-8').hex()
    userPvKey= ECPrivateKey(hashInteger,
                      cv)
    return userPvKey