from hashlib import sha256
from datetime import datetime
def updatehash(*args):
    hashing = ""
    h = sha256()
    for arg in args:
        hashing += str(arg)
    h.update(hashing.encode('utf-8'))
    return h.hexdigest()


class Block(object):

    def __init__(self, data=None, index=0, previous_hash = "0" * 64,nonse = 0 ):
        self.data = data
        self.index = index
        self.previous_hash = previous_hash
        self.nonse = nonse
        self.time = datetime.now().strftime("%d/%m/%Y, %H:%M:%S");
    def hash(self):
        return updatehash(self.previous_hash, self.index, self.data, self.nonse,self.time)

    def __str__(self):
        return str("Block#: %s\nHash: %s\nPrevious: %s\nData: %s\nNonse: %s\nTime: %s\n" % (
            self.index, self.hash(), self.previous_hash, self.data, self.nonse, self.time))


class Blockchain(object):
    difficulty = 4

    def __init__(self):
        self.chain = []

    def add(self, block):
        self.chain.append(block)

    def remove(self, block):
        self.chain.remove(block)

    def mine(self, block):
        try:
            block.previous_hash = self.chain[-1].hash()
        except IndexError:
            pass
        while True:
            if block.hash()[:self.difficulty] == "0" * self.difficulty:
                self.add(block);
                break
            else:
                block.nonse += 1

    def isValid(self):
        for i in range(1,len(self.chain)):
            _current = self.chain[i].previous_hash
            _previous = self.chain[i-1].hash()
            if _current != _previous or _previous[:self.difficulty] != "0"*self.difficulty:
                return False

        return True




class Transaction(object):
    pass


def main():
    blockchain = Blockchain()
    database = ["hello world", "ciao", "aurevoir", "bye"]
    num = 0
    for data in database:
        num += 1
        blockchain.mine(Block(data, num))
    for block in blockchain.chain:
        print(block)
    print(blockchain.isValid())

if __name__ == '__main__':
    main()
