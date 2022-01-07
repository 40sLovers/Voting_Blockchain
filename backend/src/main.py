from Blockchain_ready_Gandolh import *
from GoodToUseScripts import *
pv_key= keyFromHash(updatehash('my totally secret key'))
pu_key= pv_key.get_public_key()
pv_key2= keyFromHash(updatehash('just a random guy'))
pu_key2= pv_key.get_public_key()
# print(pv_key,pu_key)
IACoin = Blockchain()
# print(IACoin)
# IACoin.difficulty=3 # in caz ca vreti sa schimbati dificultatea de minare
# IACoin.miningReward=20 # in caz ca vreti sa schimbati reward-ul de minare
IACoin.minePendingTransactions(pu_key) #ca sa mineze genesisBlockul
print(f"Balance is {IACoin.getBallanceFromAdress(pu_key)}")


tx1 = Transaction(pu_key, pu_key2, 100)
tx1.SignTransaction(pv_key)
IACoin.addTransaction(tx1)
#Mine block
IACoin.minePendingTransactions(pu_key)

#Create second transaction
tx2 = Transaction(pu_key, pu_key2, 50)
tx2.SignTransaction(pv_key)
IACoin.addTransaction(tx2)

# Mine block
IACoin.minePendingTransactions(pu_key)


print(pu_key)
print(f"Balance is {IACoin.getBallanceFromAdress(pu_key)}")

# Uncomment this line if you want to test tampering with the chain
# IACoin.chain[1].transactions[0].amount = 10
# Check if the chain is valid
print('Blockchain valid?', IACoin.isChainValid())
