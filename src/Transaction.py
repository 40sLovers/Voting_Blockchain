from datetime import datetime
import GoodToUseScripts
from ecpy.ecdsa import ECDSA
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
        if signingKey.get_public_key() != self.fromAdress:
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
