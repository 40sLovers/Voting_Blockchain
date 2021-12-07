class Block:
    def __init__(self, timestamp, transactions, previousHash):
    #timestmap = cand a fost creat
        self.timestamp = timestamp
        self.transactions = transactions
        self.previousHash = previousHash
        self.hash = "calculeaza hash"
        
    def __repr__(self):
        return (self.timestamp + " " + str(self.transactions) + " " + str(self.previousHash))

    def calculateHash():
        #nu-i treaba mea, aveam nevoie de ea
        pass

    def hasValidTransactions():
        #nu-i treaba mea, aveam nevoie de ea
        pass

if __name__== "__main__":
    #cod pentru block.py
    pass