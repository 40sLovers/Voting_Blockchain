
from hashlib import sha256
from datetime import datetime
from ecpy.keys       import ECPublicKey, ECPrivateKey
from ecpy.curves     import Curve,Point
import os, sys
import csv
import random
import uuid
from src.Blockchain_ready_Gandolh import *
from src.GoodToUseScripts import *

#
# it doesnt work but it could pls paul,thomas watch this
#https://ec-python.readthedocs.io/en/latest/#ecpy.curves.Point

def getWalletsForPoolOptions(options,poolId):
    # Functia primeste variantele ca string-uri si creaza wallet-uri
    #am folosit cheia publica pentru a nu permite sa se faca tranzactii de la optiuni catre
    #alte walleturi
    publicKeys=[]
    hashPoolId=updatehash(poolId)
    hashpoolIdInteger=hashPoolId.encode('utf-8').hex()
    cv= Curve.get_curve('secp256k1')
    for option in options:
        hash=updatehash(option,poolId) #to combine em both
        hashOption=updatehash(option)
        hashOptionInteger=hashOption.encode('utf-8').hex()
        publicKeys.append(ECPublicKey(Point(hashpoolIdInteger,hashOptionInteger,cv)))
    return publicKeys
