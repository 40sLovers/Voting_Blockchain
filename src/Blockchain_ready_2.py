from datetime import datetime
from ecpy.ecdsa import ECDSA
import GoodToUseScripts
import uuid
class Blockchain:
    def __init__(self):
        self.chain = [self.createGenesisBlock(),]
        self.pendingTransactions = []

    def createGenesisBlock(self):
        bloc_geneza = Block("26/07/2002 00:00:00", [], None)
        return bloc_geneza

    def getLatestBlock(self):
        return self.chain[-1]

    def minePendingTransactions(self):
        now = datetime.now()
        #strftime=string format time
        now = now.strftime("%d/%m/%Y %H:%M:%S")

        block_nou = Block(now, self.pendingTransactions , self.getLatestBlock().hash)
        #block_nou.mineBlock()

        self.chain.append(block_nou)

        self.pendingTransactions = []

    def getBallanceFromAdress(self, cheie_publica):
        sold = 0
        for blocuri in self.chain:
            for tx in blocuri.transactions:
                if tx.fromAdress == cheie_publica:
                    sold = sold - tx.amount
                if tx.ToAdress == cheie_publica:
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
        if self.getBallanceFromAdress(transaction.fromAdress) <= transaction.amount:
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


class Block:
    def __init__(self, timestamp, transactions, previousHash,guid = str(uuid.uuid4())):
        # timestmap = cand a fost creat
        self.timestamp = timestamp
        self.transactions = transactions
        self.previousHash = previousHash
        self.guid= guid
        self.hash = self.calculateHash()
        self.nonce = 0

    def calculateHash(self):
        return GoodToUseScripts.updatehash(self.timestamp, self.transactions, self.previousHash)

    def mineBlock(self, difficulty=2):
        while self.hash[0, difficulty] != [0] * difficulty:
            self.nonce += 1
            self.hash = self.calculateHash()

    def hasValidTransactions(self):
        for tx in self.transactions:
            if not tx.isValid():
                return False
        return True

    def __repr__(self):
        return (self.timestamp + " " + str(self.transactions) + " " + str(self.previousHash))


class Transaction:
    def __init__(self, fromAdress, toAdress, amount):
        self.fromAdress = fromAdress
        self.toAdress = toAdress
        self.amount = amount
        self.timestamp = datetime.now().strftime("%d/%m/%Y, %H:%M:%S")

    def calculateHash(self):
        concatenatedString= str(self.fromAdress)+str(self.toAdress)+str(self.amount)+str(self.timestamp)
        return str.encode(GoodToUseScripts.updatehash(concatenatedString))

    def SignTransaction(self,signingKey):
        #signingKey e o cheie privata.
        if signingKey.get_public_key().x != self.fromAdress.x or \
        signingKey.get_public_key().y != self.fromAdress.y:
            raise Exception("Nu poti semna tranzactii pentru alte portofele")
        hashTx= self.calculateHash()
        signer = ECDSA()
        sig = signer.sign(hashTx,signingKey)
        self.signature = sig

    def isValid(self):
        # If the transaction doesn't have a from address we assume it's a
        # mining reward and that it's valid. 
        if self.fromAddress == None: return True
        if not self.signature:
            raise Exception("Nici-o semnatura in aceasta tranzactie")
        signer = ECDSA()
        return signer.verify(self.calculateHash(), self.sig, self.fromAdress)
