from Blockchain_ready_Gandolh import *
import random,os,csv,json

class Pool:
    def __init__(self,poolId,poolOptions,IAcoin):
        self.poolId=poolId
        self.poolOptions=poolOptions
        self.IAcoin=IAcoin
        now = datetime.now()
        now = now.strftime("%d/%m/%Y %H:%M:%S")
        Block_comunist = Block(now,[],IAcoin.getLatestBlock().hash,guid=poolId, poolOptions=poolOptions)
        self.block=Block_comunist
        self.IAcoin.openedPools.append(self)

    def Vote(self,poolId,privateKeyUser, option):
        #se realizeaza actiunea de votare
        #iau adresa publica a optiunii
        CurrentPool = [p for p in self.IAcoin.openedPools if p.poolId== poolId]
        if len(CurrentPool)==0:
            return 'imposibil'
        CurrentPool=CurrentPool[0]
        optionPublicKey=  [value for [key,value] in CurrentPool.poolOptions.items() if key== option]
        if len(optionPublicKey)==0:
            return 'imposibil'
        optionPublicKey=optionPublicKey[0]
        tx1 = Transaction(privateKeyUser.get_public_key(),optionPublicKey , 1)
        tx1.SignTransaction(privateKeyUser)
        self.IAcoin.addTransaction(tx1)
        print(self.IAcoin.pendingTransactions)

    def endPool(self,rewardAdress):
        # rewardAdress ---public Key
        self.IAcoin.minePendingTransactions(rewardA1dress)
        print(self.IAcoin.chain)


class GenerateHelper:
    def __init__(self):
        pass

    @staticmethod
    def getRandomPublicKey(*args):
        hash=updatehash(*args, uuid.uuid4().hex)
        privateKey=keyFromHash(hash)
        return privateKey.get_public_key()

    @staticmethod
    def rand_str(self, str_size):
        return ''.join(random.choice('abcdefghijklmnopqrstuvwxyz') for x in range(str_size))

    @staticmethod
    def getRandomOptions():
        l = []
        for i in range(20):
            dict = {"optiune{}".format(i + 1): random.randint(1, 200)}
            l.append(dict)
        return json.dumps(AlgorithmsHelpers.sortOptions(l))
        
    def createTestingUsers(self,in_file, i):
        letter = chr(ord("a") + i) + "_user"
        letter_hash = updatehash(letter)
        private_key = keyFromHash(letter_hash)
        public_key = private_key.get_public_key()
        CSVHelpers.appendCSVFile(in_file, {"public_key_x": public_key.W.x, "public_key_y": public_key.W.y})


class CSVHelpers:
    path_to_database = "../database/"
    def __init__(self):
        pass

    @staticmethod
    def readAllUsers(in_file):
        with open(CSVHelpers.path_to_database + in_file, "r") as f:
            reader = csv.reader(f)
            line = next(reader)
            print(line)
            all_users = []
            for x in reader:
                x[0] = int(x[0])
                x[1] = int(x[1])
                all_users.append(x)
        return all_users

    @staticmethod
    def isInCSVFile(file, value):
        #verifica daca textul value este prezent in csv
        if os.path.isfile(file):
            with open(file, 'r') as f:
                reader = csv.reader(f)
                for rows in reader:
                    for cell in rows:
                        if value in cell:
                            return True
                return False
        else: raise Exception("File not found")

    @staticmethod
    def createCSVFile(new_file, list_of_header):
        #creaza un csv file cu denumirea {new_file} si creaza header-ul din list_of_header
        if new_file in os.listdir(CSVHelpers.path_to_database):
            raise "Fisierul se afla deja in baza de date!"
        else:
            with open(CSVHelpers.path_to_database + new_file, 'w', newline="") as f:
                writer = csv.writer(f)
                writer.writerow(list_of_header)

    @staticmethod
    def appendCSVFile(file, dict_values_forCSV):
        #primeste ca parametrii numele unui fisier si un dictionar cu care s-ar completa csv-ul
        #da append fisierului cu datele corespunzatoare.
        if not(file in os.listdir(CSVHelpers.path_to_database)):
            raise "Fisierul nu se afla in baza de  date!"
        else:
            with open(CSVHelpers.path_to_database + file, 'r', newline="") as f:
                reader = csv.reader(f)
                header = next(reader)
            with open(CSVHelpers.path_to_database + file, 'a', newline="") as f2:
                list_date = [0,] * len(header)
                for key in dict_values_forCSV.keys():
                    list_date[header.index(key)] = dict_values_forCSV[key]
                writer = csv.writer(f2)
                writer.writerow(list_date)





class AlgorithmsHelpers:
    #merge doar pentru naturale
    @staticmethod
    def is_prim(x):
        if x==0 or x==1:
            return False
        if x==2:
            return True
        if x%2==0:
            return False
        for d in range(3,int(x**0.5)+1,2):
            if x%d==0:
                return False
        return True
    @staticmethod
    def cautbinar (x,v,s ,d ):
        x=int(x)
        while s<=d:
                mij=int((s+d)//2)
                if v[mij]==x:
                    return mij
                if v[mij]>x:
                    d=mij-1
                else:
                    s=mij+1
        if s==d and v[s]==x:
            return s
        return -1
    @staticmethod
    def sortOptions(l):
        for i in range(len(l) - 1):
            for j in range(i + 1, len(l)):
                x = list(l[i].keys())[0]
                y = list(l[j].keys())[0]
                if l[i][x] < l[j][y]:
                    var = l[i]
                    l[i] = l[j]
                    l[j] = var
        return l


class BlockchainHelpers():
    def __init__(self):
        pass

    @staticmethod
    def initializareLantDeBlocuri(blockChain):
        #initializeaza 20 de blocuri de start in blockchain. Acest lucru scade posibilitatea de a
        # recrea blockchainul de la 0 deoarece ar dura prea mult
        for i in range(0,20):
            now = datetime.now()
            # strftime=string format time
            now = now.strftime("%d/%m/%Y %H:%M:%S")

            block_nou = Block(now, [], blockChain.getLatestBlock().hash)
            block_nou.mineBlock(1)

            blockChain.chain.append(block_nou)


class KeyHelpers():
    def __init__(self):
        pass

    @staticmethod
    def getPrivateKey(*args):
        hash=updatehash(*args)
        privateKey=keyFromHash(hash)
        return privateKey

    @staticmethod
    def getPublicKey(*args):
        pv_key= KeyHelpers.getPrivateKey(*args)
        return pv_key.get_public_key()
