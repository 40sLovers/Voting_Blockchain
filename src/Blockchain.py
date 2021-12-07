from Block import Block
from Transaction import Transaction
from datetime import datetime

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


if __name__== "__main__":
    #cod pentru blockchain.py
    bloc = Blockchain()
    print(bloc.chain)

    print(bloc.getLatestBlock())
    bloc.chain.append(Block("26/07/2001 00:00:00", [], None))
    print(bloc.getLatestBlock())
    bloc.chain.append(Block("26/07/2000 00:00:00", [], None))
    print(bloc.getLatestBlock())

