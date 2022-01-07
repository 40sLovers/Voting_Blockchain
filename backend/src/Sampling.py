# https://ec-python.readthedocs.io/en/latest/


from ecpy.curves     import Curve,Point
from ecpy.keys       import ECPublicKey, ECPrivateKey
from ecpy.ecdsa      import ECDSA
from Blockchain_ready_Gandolh import *
from GoodToUseScripts import *
cv     = Curve.get_curve('secp256k1')
# pu_key = ECPublicKey(Point(0x65d5b8bf9ab1801c9f168d4815994ad35f1dcb6ae6c7a1a303966b677b813b00,

#                            0xe6b865e529b8ecbf71cf966e900477d49ced5846d7662dd2dd11ccd55c0aff7f,
#                            cv))
# pv_key = ECPrivateKey(0xfb26a4e75eec75544c0f44e937dcf5ee6355c7176600b9688c667e5c283b43c5,
#                       cv)
# pv_key2 = ECPrivateKey(0xfb26a4e75eec75544c0f44e937dcf5ee6355c7176600b9688c667e5c283b43c5,
# cv)
# print(pv_key2)
# print(pv_key2.get_public_key())
# signer = ECDSA()
# sig    = signer.sign(str.encode("asd"),pv_key)
# assert(signer.verify(str.encode("asd"),sig,pu_key))



userPvKey= GoodToUseScripts.keyFromHash("asd")
print(userPvKey)