from Block import Block


class Blockchain:
    def __init__(self):
        self.chain = []
        self.pendingTransactions = []
    def createGenesisBlock(self):
        blocNou = Block()
        pass


bloc = Blockchain()
print(bloc.chain)
