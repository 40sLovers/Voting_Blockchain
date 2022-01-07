from datetime import datetime
from ecpy.ecdsa import ECDSA
import uuid
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

class Blockchain:
    def __init__(self):
        self.chain = [self.createGenesisBlock(),]
        self.pendingTransactions = []
        self.difficulty=2
        self.miningReward=100
    def createGenesisBlock(self):
        bloc_geneza = Block("26/07/2002 00:00:00", [], None)
        return bloc_geneza

    def getLatestBlock(self):
        return self.chain[-1]

    def minePendingTransactions(self,minningRewardAdress):
        rewardTx = Transaction(None,minningRewardAdress.__str__(),self.miningReward)
        self.pendingTransactions.append(rewardTx)

        now = datetime.now()
        #strftime=string format time
        now = now.strftime("%d/%m/%Y %H:%M:%S")

        block_nou = Block(now, self.pendingTransactions , self.getLatestBlock().hash)
        block_nou.mineBlock(self.difficulty)

        self.chain.append(block_nou)

        self.pendingTransactions = []

    def getBallanceFromAdress(self, cheie_publica):
        sold = 0

        for blocuri in self.chain:
            for tx in blocuri.transactions:
                if tx.fromAdress!=None and tx.fromAdress == cheie_publica.__str__():
                    sold = sold - tx.amount
                if tx.toAdress == cheie_publica.__str__():
                    sold = sold + tx.amount

        return sold

    def addTransaction(self, transaction):
        if transaction.fromAdress == None:
            raise Exception("nu exista adresa de la care se face transferul")
        if transaction.toAdress == None:
            raise Exception("nu exista adresa la care se face transferul")
        if transaction.isValid() == False:
            raise Exception("Tranzactie Invalida")
        if transaction.amount <= 0:
            raise Exception("Suma invalida")
        if self.getBallanceFromAdress(transaction.fromAdress) < transaction.amount:
            raise Exception("Fonduri insuficiente")

        self.pendingTransactions.append(transaction)

    def getAllTransactionsForWallet(self, adress):
        lista_tranzactii = []
        for blocuri in self.chain:
            for transaction in blocuri.transactions:
                if transaction.toAdress == adress or transaction.fromAdress == adress:
                    lista_tranzactii.append(transaction)

        return lista_tranzactii

    def isChainValid(self):
        GenesisBlock = self.createGenesisBlock()

        if str(GenesisBlock) != str(self.chain[0]):
            return False
        
        for i in range(1,len(self.chain)):
            current_block = self.chain[i]
            previous_block = self.chain[i-1]
            if current_block.previousHash != previous_block.hash:
                return False
            if current_block.hasValidTransactions() == False:
                return False
            if current_block.hash != current_block.calculateHash():
                return False
            
        return True

    def __repr__(self) -> str:
        return f"Blockchain with chain= {self.chain};\n pendingTransactions= {self.pendingTransactions}"
    def ___str__(self):
        return f"Blockchain with chain= {self.chain};\n pendingTransactions= {self.pendingTransactions}"

class Block:
    def __init__(self, timestamp, transactions, previousHash,guid = str(uuid.uuid4()),PoolOptions=[]):
        # timestamp = cand a fost creat
        self.timestamp = timestamp
        self.transactions = transactions
        self.previousHash = previousHash
        self.guid= guid
        self.nonce = 0
        self.hash = self.calculateHash()
        self.PoolOptions=PoolOptions

    def calculateHash(self):
        return updatehash(self.timestamp, self.transactions, self.previousHash,self.nonce,self.guid)

    def mineBlock(self, difficulty=2):
        difficulty= int(difficulty)
        while self.hash[0: difficulty] != '0' * difficulty:
            self.nonce += 1
            self.hash = self.calculateHash()
            # print(str(self.hash[0: difficulty]),'0' * difficulty)

    def hasValidTransactions(self):
        for tx in self.transactions:
            if not tx.isValid():
                return False
        return True

    def __repr__(self) -> str:
        return f"\nBlock with guid: {self.guid}\n hash={self.hash}\n  \
previousHash={self.previousHash}\n timestamp={self.timestamp} \n transactions={self.transactions}"
    def ___str__(self):
        return f"\nBlock with guid: {self.guid}\n hash={self.hash}\n  \
previousHash={self.previousHash}\n timestamp={self.timestamp} \n transactions={self.transactions}"


class Transaction:
    def __init__(self, fromAdress, toAdress, amount):
        self.fromAdress = fromAdress
        self.toAdress = toAdress
        self.amount = amount
        self.timestamp = datetime.now().strftime("%d/%m/%Y, %H:%M:%S")

    def calculateHash(self):
        concatenatedString= str(self.fromAdress)+str(self.toAdress)+str(self.amount)+str(self.timestamp)
        return str.encode(updatehash(concatenatedString))

    def SignTransaction(self,signingKey):
        #signingKey e o cheie privata.
        if str(signingKey.get_public_key()) != str(self.fromAdress) :
            raise Exception("Nu poti semna tranzactii pentru alte portofele")
        hashTx= self.calculateHash()
        signer = ECDSA()
        sig = signer.sign(hashTx,signingKey)
        self.signature = sig

    def isValid(self):
        # If the transaction doesn't have a from address we assume it's a
        # mining reward and that it's valid. 
        if self.fromAdress == None:
             return True
        if not self.signature:
            raise Exception("Nici-o semnatura in aceasta tranzactie")
        signer = ECDSA()
        return signer.verify(self.calculateHash(), self.signature, self.fromAdress)
    def __repr__(self) -> str:
        return f"Transaction with fromAdress: {self.fromAdress}\n toAdress={self.toAdress}\n amount={self.amount} \
timestamp={self.timestamp}\n "
    def __str__(self) -> str:
        return f"Transaction with fromAdress: {self.fromAdress}\n toAdress={self.toAdress}\n amount={self.amount} \
timestamp={self.timestamp}\n "