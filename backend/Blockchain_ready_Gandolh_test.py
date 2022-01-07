from Blockchain_ready_Gandolh import *
from GoodToUseScripts import *
import unittest
import random

class TestBlockchain(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print('Initialising...')
        global IACoin,keylen,seed1,seed2,key,key2,key_copy
        keylen = 10
        seed1 = cls.rand_str(cls,keylen)
        seed2 = cls.rand_str(cls,keylen)
        #make seed1!=seed2
        while seed1==seed2:
            seed2 = cls.rand_str(cls,keylen)
        #generate keys
        key=keyFromHash(updatehash(seed1))
        key2 = keyFromHash(updatehash(cls.rand_str(cls,10)))
        key_copy=keyFromHash(updatehash(seed1))

        IACoin = Blockchain()

    def rand_str(self, str_size):
        return ''.join(random.choice('abcdefghijklmnopqrstuvwxyz') for x in range(str_size))

    def test_keygeneration(self):
        print('Testing key generation...')
        # Check if same input results in the same hash
        self.assertEqual(key.d,key_copy.d)

        # Check if the get public key works
        self.assertEqual(key.get_public_key().W,key_copy.get_public_key().W)

    def test_mineGenesisBlock(self):
        print('Testing genesis block...')
        len_before = len(IACoin.chain)
        IACoin.minePendingTransactions(key.get_public_key())
        #todo add more tests
        self.assertGreater(len(IACoin.chain),len_before)

    def test_transactions(self):
        print('Testing transactions...')
        print(IACoin.getBallanceFromAdress(key.get_public_key()))
        tx = Transaction(key.get_public_key(),key2.get_public_key(),100)
        tx.SignTransaction(key)
        IACoin.addTransaction(tx)
        # Mine block
        print(IACoin)

if __name__ == '__main__':
    unittest.main()