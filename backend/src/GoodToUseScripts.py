from hashlib import sha256
from datetime import datetime
from ecpy.keys      import ECPublicKey, ECPrivateKey
from ecpy.curves     import  Curve,Point
import uuid
from Blockchain_ready_Gandolh import *;
from Classes import *






if __name__=='__main__':
    #CSVHelpers.createCSVFile("test1.csv", ["Nume", "Prenume", "Data"])
    #CSVHelpers.appendCSVFile("test1.csv", {"Nume": "Bradea", "Prenume": "Vlad", "Data": "Azi"})
    IAcoin=Blockchain()
    # BlockchainHelpers.initializareLantDeBlocuri(IAcoin)
    # print(IAcoin)


    poolId=uuid.uuid4().hex
    poolOptions={
        'a': GenerateHelper.getRandomPublicKey('a',poolId),
        'b':GenerateHelper.getRandomPublicKey('b',poolId),
        'c':GenerateHelper.getRandomPublicKey('c',poolId),
        'd':GenerateHelper.getRandomPublicKey('d',poolId),
        'e':GenerateHelper.getRandomPublicKey('e',poolId)
    }
    VotePool=Pool(poolId,poolOptions,IAcoin)
    VotePool.Vote(poolId,'','c')

    

    # l = []
    # for i in range(20):
    #     dict = {"optiune{}".format(i + 1): random.randint(1, 200)}
    #     l.append(dict)
    # print(sortOptions(l))

    # createCSVFile("whitelist.csv", ["public_key_x", "public_key_y"])
    # for i in range(20):
    #     createTestingUsers("whitelist.csv", i)

    # print(readAllUsers("whitelist.csv"))

