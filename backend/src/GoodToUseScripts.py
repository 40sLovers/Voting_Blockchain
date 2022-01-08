from hashlib import sha256
from datetime import datetime
from ecpy.keys      import ECPublicKey, ECPrivateKey
from ecpy.curves     import  Curve,Point
import uuid
from Blockchain_main import *;
from Classes import *



if __name__=='__main__':
    #CSVHelpers.createCSVFile("test1.csv", ["Nume", "Prenume", "Data"])
    #CSVHelpers.appendCSVFile("test1.csv", {"Nume": "Bradea", "Prenume": "Vlad", "Data": "Azi"})
    my_pu_key=KeyHelpers.getPublicKey('gusi e pe whitelist')
    my_pv_key=KeyHelpers.getPrivateKey('gusi e pe whitelist')
    IAcoin=Blockchain()
    # BlockchainHelpers.initializareLantDeBlocuri(IAcoin)
    # IAcoin.minePendingTransactions(None) #ca sa mineze genesisBlockul
    # print(IAcoin)
    print(IAcoin.isChainValid())

    poolId=uuid.uuid4().hex
    poolOptions={
        'a': GenerateHelper.getRandomPublicKey('a',poolId),
        'b':GenerateHelper.getRandomPublicKey('b',poolId),
        'c':GenerateHelper.getRandomPublicKey('c',poolId),
        'd':GenerateHelper.getRandomPublicKey('d',poolId),
        'e':GenerateHelper.getRandomPublicKey('e',poolId)
    }
    #se cauta in iacoin.openedPools dupa PoolId daca e nevoie de
    #o metoda din el
    VotePool=Pool(poolId,poolOptions,IAcoin)
    VotePool.Vote(poolId,my_pv_key,'c')
    # VotePool.Vote(poolId,my_pv_key,'e')
    # VotePool.Vote(poolId,my_pv_key,'c')
    # VotePool.Vote(poolId,my_pv_key,'b')
    # VotePool.Vote(poolId,my_pv_key,'a')
    # VotePool.Vote(poolId,my_pv_key,'b')
    # VotePool.Vote(poolId,my_pv_key,'c')
    # VotePool.Vote(poolId,my_pv_key,'c')
    # VotePool.Vote(poolId,my_pv_key,'c')
    # VotePool.Vote(poolId,my_pv_key,'c')
    # VotePool.Vote(poolId,my_pv_key,'c')
    VotePool.endPool()
    print(VotePool.getResults())
    print(IAcoin.isChainValid())
    # CSVHelpers.appendCSVFile('whitelist.csv',{'public_key_x':my_pu_key.W.x,'public_key_y':my_pu_key.W.y})
    
    
    
    pass