import hashlib
import json
from Cryptodome.PublicKey import RSA
from Cryptodome.Signature import *
from time import time
from datetime import datetime


class Blockchain(object):
    def __init__(self):
        self.chain = [self.addGenesisBlock()]
        self.pendingTransactions = []
        self.difficulty = 2
        self.blockSize = 200

    def minePendingTransactions(self):  # aici ar trebui sa avem un atribut de tip miner pentru fiecare node

        lenPT = len(self.pendingTransactions)
        if (lenPT < 1):
            print("Nu sunt destule Tranzacti (Must be > 1)")
            return False;
        else:
            for i in range(0, lenPT, self.blockSize):
                end = i + self.blockSize
                if i >= lenPT:
                    end = lenPT

                transactionSlice = self.pendingTransactions[i:end]
                newBlock = Block(transactionSlice, datetime.now().strftime("%d/%m/%Y, %H:%M:%S"), len(self.chain))
                hashVal = self.getLastBlock().hash
                newBlock.prev = hashVal
                newBlock.mineBlock(self.difficulty)
                self.chain.append(newBlock)
            print("Mining Success")
        return True

    def addTransaction(self, sender, reciever, amt, keyString, senderKey):
        keyByte = keyString.encode("ASCII")
        senderKeyByte = senderKey.encode("ASCII")
        key = RSA.import_key(keyByte)
        senderKey = RSA.import_key(senderKeyByte)

        if not sender or not reciever or not amt:
            print("A aparut o eroare (Wrong Input)")
            return False
        transaction = Transaction(sender, reciever, amt)
        transaction.signTransaction(key, senderKey)
        if not transaction.isValidTransaction():
            print("A aparut")
            return False
        self.pendingTransactions.append(transaction);
        return len(self.chain) + 1

    def getLastBlock(self):
        return self.chain[-1]

    def addGenesisBlock(self):
        tArr = []
        tArr.append(Transaction("DelaMine", "PentruTine", 1))
        genesis = Block(tArr, datetime.now().strftime("%m/%d/%Y, %H:%M:%S"), 0)
        genesis.prev = "0" * 64
        return genesis

    def isValidChain(self):
        for i in range(1, len(self.chain)):
            cmp = self.chain[i - 1]
            crp = self.chain[i]

            if not crp.hasValidTransactions():
                print("Eroare Tranzactii in block")
                return False

            if crp.hash != crp.calculateHash():
                print("Eroare Hash")
                return False

            if crp.prev != cmp.hash:
                console.log("Eroare Link intre Blocuri")
                return False
        return True

    def generateKeys(self):
        key = RSA.generate(2048)
        private_key = key.export_key()
        file_out = open("private.pem", "wb")
        file_out.write(private_key)

        public_key = key.publickey().export_key()
        file_out = open("receiver.pem", "wb")
        file_out.write(public_key)

        print(public_key.decode('ASCII'))
        return key.publickey().export_key().decode('ASCII')

    def getBalance(self, person):
        balance = 0
        for i in range(1, len(self.chain)):
            block = self.chain[i]
            try:
                for j in range(0, len(block.transactions)):
                    transaction = block.transactions[j]
                    if (transaction.sender == person):
                        balance -= transaction.amt
                    if (transaction.reciever == person):
                        balance += transaction.amt
            except AttributeError:
                print("Nicio Tranzactie pentru acest user")
        return balance + 100;  # Aici punem cata balanta vrem ca un user sa aiba la inceput


class Block(object):
    def __init__(self, transactions, time, index):
        self.index = index
        self.transactions = transactions
        self.time = time
        self.prev = ''
        self.nonse = 0
        self.hash = self.calculateHash()

    def calculateHash(self):

        hashTransactions = ""

        for transaction in self.transactions:
            hashTransactions += transaction.hash
        hashString = str(self.time) + hashTransactions + self.prev + str(self.nonse)
        hashEncoded = json.dumps(hashString, sort_keys=True).encode()
        return hashlib.sha256(hashEncoded).hexdigest()

    def mineBlock(self, difficulty):
        arr = [];
        for i in range(0, difficulty):
            arr.append(i)
        arrStr = map(str, arr)
        hashPuzzle = ''.join(arrStr)

        while self.hash[0:difficulty] != hashPuzzle:
            self.nonse += 1
            self.hash = self.calculateHash()
        print("Bloc Minat")
        return True

    def hasValidTransactions(self):
        for i in range(0, len(self.transactions)):
            transaction = self.transactions[i];
            if not transaction.isValidTransaction():
                return False;
            return True;

    def JSONencode(self):
        return json.encode(self);


class Transaction(object):
    def __init__(self, sender, reciever, amt):
        self.sender = sender
        self.reciever = reciever
        self.amt = amt
        self.time = datetime.now().strftime("%d/%m/%Y, %H:%M:%S")
        self.hash = self.calculateHash()

    def calculateHash(self):
        hashString = self.sender + self.reciever + str(self.amt) + str(self.time)
        hashEncoded = json.dumps(hashString, sort_keys=True).encode()
        return hashlib.sha256(hashEncoded).hexdigest()

    def isValidTransaction(self):
        if (self.hash != self.calculateHash()):
            return False
        if (self.sender == self.reciever):
            return False
        if not self.signature or len(self.signature) == 0:
            print("Nicio Semnatura!")
            return False
        return True
    # Mai e nevoie de munca pe partea asta

    def signTransaction(self, key, senderKey):
        if (self.hash != self.calculateHash()):
            print("Eroare tranzactie")
            return False
        if (str(key.publickey().export_key()) != str(senderKey.publickey().export_key())):
            print("Eroare semnatura ne-propietara")
            return False
        # Daca nu sunt erori putem sa semnam tranzactia
        pkcs1_15.new(key)
        self.signature = "Semnat"
        return True
