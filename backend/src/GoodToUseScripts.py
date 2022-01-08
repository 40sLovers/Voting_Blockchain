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
    # print(GenerateHelper.getRandomOptions('nume'))
    my_pu_key=KeyHelpers.getPublicKey('gusi e pe whitelist')
    my_pv_key=KeyHelpers.getPrivateKey('gusi e pe whitelist')
    IAcoin=Blockchain()
    # BlockchainHelpers.initializareLantDeBlocuri(IAcoin)
    # IAcoin.minePendingTransactions(None) #ca sa mineze genesisBlockul
    # print(IAcoin)
    # print(IAcoin.isChainValid())

    poolId=uuid.uuid4().hex
    poolOptions={
        'a':GenerateHelper.getRandomPublicKey('a',poolId),
        'b':GenerateHelper.getRandomPublicKey('b',poolId),
        'c':GenerateHelper.getRandomPublicKey('c',poolId),
        'd':GenerateHelper.getRandomPublicKey('d',poolId),
        'e':GenerateHelper.getRandomPublicKey('e',poolId)
    }
    #se cauta in iacoin.openedPools dupa PoolId daca e nevoie de
    #o metoda din el
    VotePool=Pool(poolId,poolOptions,IAcoin)
    VotePool.Vote(poolId,KeyHelpers.getPrivateKey(GenerateHelper.rand_str(10)),'c')
    VotePool.Vote(poolId,KeyHelpers.getPrivateKey(GenerateHelper.rand_str(10)),'e')
    VotePool.Vote(poolId,KeyHelpers.getPrivateKey(GenerateHelper.rand_str(10)),'c')
    VotePool.Vote(poolId,KeyHelpers.getPrivateKey(GenerateHelper.rand_str(10)),'b')
    VotePool.Vote(poolId,KeyHelpers.getPrivateKey(GenerateHelper.rand_str(10)),'a')
    VotePool.Vote(poolId,KeyHelpers.getPrivateKey(GenerateHelper.rand_str(10)),'b')
    VotePool.Vote(poolId,KeyHelpers.getPrivateKey(GenerateHelper.rand_str(10)),'c')
    VotePool.Vote(poolId,KeyHelpers.getPrivateKey(GenerateHelper.rand_str(10)),'c')
    VotePool.Vote(poolId,KeyHelpers.getPrivateKey(GenerateHelper.rand_str(10)),'c')
    VotePool.Vote(poolId,KeyHelpers.getPrivateKey(GenerateHelper.rand_str(10)),'c')
    VotePool.Vote(poolId,KeyHelpers.getPrivateKey(GenerateHelper.rand_str(10)),'c')
    VotePool.endPool()
    print(VotePool.getResults())

    # CSVHelpers.createCSVFile('EmailList.csv',['email'])
    # CSVHelpers.appendCSVFile('EmailList.csv',{'email':'asd'})
    # print(IAcoin.isChainValid())
    # CSVHelpers.appendCSVFile('whitelist.csv',{'public_key_x':my_pu_key.W.x,'public_key_y':my_pu_key.W.y})
    # conHelper=SqlLiteConnectionHelper()
    # conHelper.CreateTable('Test1','public_key_x text, public_key_y text')
    #drop table
    #insert rows
    #select data
    pass