import GoodToUseScripts


class Block:
    def __init__(self, timestamp, transactions, previousHash):
        # timestmap = cand a fost creat
        self.timestamp = timestamp
        self.transactions = transactions
        self.previousHash = previousHash
        self.hash = self.calculateHash()
        self.nonce = 0

    def calculateHash(self):
        return GoodToUseScripts.updatehash(self.timestamp, self.transactions, self.previousHash)

    def mineBlock(self, difficulty):
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


if __name__ == "__main__":
    # cod pentru block.py
    pass