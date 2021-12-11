from datetime import datetime
import GoodToUseScripts
class Transaction:
    def __init__(self, fromAdress, toAdress, amount):
        self.fromAdress = fromAdress
        self.toAdress = toAdress
        self.amount = amount
        self.timestamp = datetime.now().strftime("%d/%m/%Y, %H:%M:%S")

    def calculateHash(self):
        concatenatedString= str(self.fromAdress)+str(self.toAdress)+str(self.amount)+str(self.timestamp)
        return GoodToUseScripts.updatehash(concatenatedString)

    def SignTransaction(self,signingKey):
        pass

    def isValid(self):
        # If the transaction doesn't have a from address we assume it's a
        # mining reward and that it's valid. 
        if self.fromAddress == None: return True
        if not self.signature or self.signature.length == 0:
            raise Exception("Nici-o semnatura in aceasta tranzactie")
    # publicKey = ec.keyFromPublic(this.fromAddress, 'hex');
    # return publicKey.verify(this.calculateHash(), this.signature);