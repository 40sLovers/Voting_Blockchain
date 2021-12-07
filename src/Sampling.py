import sys, os
sys.path.append(os.path.abspath(os.path.join('..','libraries','elliptic-py','src')))
from ellipticpy import SigningKey, SECP256k1
sk = SigningKey.generate(curve = SECP256k1)
sk_string = sk.to_string()
