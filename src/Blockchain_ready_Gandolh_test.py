from Blockchain_ready_Gandolh import Blockchain,Block,Transaction
from GoodToUseScripts import keyFromHash,updatehash
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

if __name__ == '__main__':
    unittest.main()