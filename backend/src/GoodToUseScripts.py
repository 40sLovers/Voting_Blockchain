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
    # my_pu_key=KeyHelpers.getPublicKey('gusi e pe whitelist')
    # my_pv_key=KeyHelpers.getPrivateKey('gusi e pe whitelist')
    # IAcoin=Blockchain()
    # IAcoin.minePendingTransactions(my_pu_key) #ca sa mineze genesisBlockul
    # BlockchainHelpers.initializareLantDeBlocuri(IAcoin)
    # print(IAcoin)
 

    # poolId=uuid.uuid4().hex
    # poolOptions={
    #     'a': GenerateHelper.getRandomPublicKey('a',poolId),
    #     'b':GenerateHelper.getRandomPublicKey('b',poolId),
    #     'c':GenerateHelper.getRandomPublicKey('c',poolId),
    #     'd':GenerateHelper.getRandomPublicKey('d',poolId),
    #     'e':GenerateHelper.getRandomPublicKey('e',poolId)
    # }

    # VotePool=Pool(poolId,poolOptions,IAcoin)
    # VotePool.Vote(poolId,my_pv_key,'c')
    # VotePool.endPool(None)
    # CSVHelpers.appendCSVFile('whitelist.csv',{'public_key_x':my_pu_key.W.x,'public_key_y':my_pu_key.W.y})
    



