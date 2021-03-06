import random,os,csv,json,sqlite3
if __name__== 'Classes':
    from Blockchain_main import *
elif __name__=='src.Classes':
    from .Blockchain_main import *

class Pool:
    def __init__(self,poolId,poolOptions,IAcoin,title='',poolCreator=None):
        self.poolId=poolId
        self.poolCreator=poolCreator
        self.title=title
        self.poolOptions=poolOptions
        self.opList = poolOptions.keys()
        self.IAcoin=IAcoin
        self.pendingTransactions=[]
        self.difficulty=2
        now = datetime.now()
        now = now.strftime("%d/%m/%Y %H:%M:%S")
        Block_comunist = Block(now,self.pendingTransactions,None,guid=poolId, poolOptions=poolOptions)
        self.block=Block_comunist
        self.IAcoin.openedPools.append(self)

    def Vote(self,privateKeyUser, option):
        #se realizeaza actiunea de votare
        #iau adresa publica a optiunii
        CurrentPool = self
        optionPublicKey=  [value for [key,value] in CurrentPool.poolOptions.items() if key== option]
        if len(optionPublicKey)==0:
            return False
        optionPublicKey=optionPublicKey[0]
        tx1 = Transaction(privateKeyUser.get_public_key(),optionPublicKey , 1)
        tx1.SignTransaction(privateKeyUser)
        self.addTransaction(tx1)
        # print(self.pendingTransactions)
        return True

    def endPool(self):
        # rewardAdress ---public Key
        self.minePendingTransactions()
        # print(self.IAcoin.chain)

    def getResults(self):
        dict = {}
        for x in self.poolOptions.values():
            dict[x] = 0

        for tx in self.block.transactions:
            dict[tx.toAdress] += int(tx.amount)

        results=[]
        for [poolOption, pub_key] in self.poolOptions.items():
            results.append({
                poolOption: dict[pub_key]
                })
        return results

    def addTransaction(self, transaction):
        if transaction.fromAdress == None:
            raise Exception("nu exista adresa de la care se face transferul")
        if transaction.toAdress == None:
            raise Exception("nu exista adresa la care se face transferul")
        if transaction.isValid() == False:
            raise Exception("Tranzactie Invalida")
        if transaction.amount <= 0:
            raise Exception("Suma invalida")
        if not self.isBallanceEnoughToVote(transaction.fromAdress) :
            raise Exception("Ai votat deja")

        self.pendingTransactions.append(transaction)

    def minePendingTransactions(self):
        self.block.previousHash=self.IAcoin.getLatestBlock().hash
        self.block.mineBlock(self.difficulty)
        self.IAcoin.chain.append(self.block)
        self.pendingTransactions = []

    def isBallanceEnoughToVote(self, cheie_publica):
        occurences= [ pub_key for pub_key in self.block.transactions if pub_key.fromAdress.__str__()==cheie_publica.__str__()]
        # print(len(occurences))
        if len(occurences):
            return False
        return True


class GenerateHelper:
    def __init__(self):
        pass

    @staticmethod
    def getRandomPublicKey(*args):
        hash=updatehash(*args, uuid.uuid4().hex)
        privateKey=keyFromHash(hash)
        return privateKey.get_public_key()

    @staticmethod
    def rand_str(str_size):
        return ''.join(random.choice('abcdefghijklmnopqrstuvwxyz') for x in range(str_size))

    @staticmethod
    def getRandomOptions(order_by):
        l = []
        for i in range(20):
            dict = {"optiune{}".format(i + 1): random.randint(1, 200)}
            l.append(dict)
        return json.dumps(AlgorithmsHelpers.sortOptions(l,order_by))
        
    def createTestingUsers(self,in_file, i):
        letter = chr(ord("a") + i) + "_user"
        letter_hash = updatehash(letter)
        private_key = keyFromHash(letter_hash)
        public_key = private_key.get_public_key()
        CSVHelpers.appendCSVFile(in_file, {"public_key_x": public_key.W.x, "public_key_y": public_key.W.y})


class CSVHelpers:
    # path_to_database = "../database/"
    def __init__(self):
        pass

    @staticmethod
    def readAllUsers(in_file):
        with open(in_file, "r") as f:
            reader = csv.reader(f)
            line = next(reader)
            # print(line)
            all_users = []
            for x in reader:
                x[0] = int(x[0])
                x[1] = int(x[1])
                all_users.append(x)
        return all_users

    @staticmethod
    def readAllEmails(in_file):
        with open(in_file, "r") as f:
            reader = csv.reader(f)
            line = next(reader)
            # print(line)
            all_users = []
            for x in reader:
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
        if os.path.isfile(new_file):
            raise "Fisierul se afla deja in baza de date!"
        else:
            with open(new_file, 'w', newline="") as f:
                writer = csv.writer(f)
                writer.writerow(list_of_header)

    @staticmethod
    def appendCSVFile(file, dict_values_forCSV):
        #primeste ca parametrii numele unui fisier si un dictionar cu care s-ar completa csv-ul
        #da append fisierului cu datele corespunzatoare.
        if not(os.path.isfile(file)):
            raise "Fisierul nu se afla in baza de  date!"
        else:
            with open(file, 'r', newline="") as f:
                reader = csv.reader(f)
                header = next(reader)
            with open(file, 'a', newline="") as f2:
                list_date = [0,] * len(header)
                for key in dict_values_forCSV.keys():
                    list_date[header.index(key)] = dict_values_forCSV[key]
                writer = csv.writer(f2)
                writer.writerow(list_date)

class VoteEntryStore:
    def __init__(self):
        self.TempStore = []
    
    def GetVoteEntryIndex(self, cod):
        i=0
        while i < len(self.TempStore):
            if self.TempStore[i].cod == cod:
                return i 
            i+=1
        return -1

    def AddVoteEntry(self, voteEntry):
        # print(voteEntry.cod)
        eIndex = self.GetVoteEntryIndex(voteEntry.cod)
        if eIndex != -1:
            return False
        self.TempStore.append(voteEntry)
        return True

    def GetVoteEntry(self, cod):
        i=0
        while i < len(self.TempStore):
            if str(self.TempStore[i].cod) == str(cod):
                return self.TempStore[i] 
            i+=1
        return None



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
    def sortOptions(l,order_by):
        if order_by=='nume':
            for i in range(len(l) - 1):
                for j in range(i + 1, len(l)):
                    x = list(l[i].keys())[0]
                    y = list(l[j].keys())[0]
                    # print(x,y)
                    if x < y:
                        l[i], l[j] = l[j], l[i]
        else:
            for i in range(len(l) - 1):
                for j in range(i + 1, len(l)):
                    x = list(l[i].keys())[0]
                    y = list(l[j].keys())[0]
                    if l[i][x] < l[j][y]:
                        l[i], l[j] = l[j], l[i]
        return l


class BlockchainHelpers():
    def __init__(self):
        pass

    @staticmethod
    def initializareLantDeBlocuri(blockChain,initialChainLength=20):
        #initializeaza [initialChainLength] de blocuri de start in blockchain. Acest lucru scade posibilitatea de a
        # recrea blockchainul de la 0 deoarece ar dura prea mult
        for i in range(0,initialChainLength):
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

class VoteEntry:
  def __init__(self, cod, name, opList):
    self.cod = cod
    self.name = name
    self.opList = opList
    self.bHasVoted = False
    self.votedOption = None
 

class SqlLiteConnectionHelper:
    abs_path_to_sqlite=os.path.join(os.path.abspath('..'),'database','SQLite.db')
    def __init__(self):
        con = sqlite3.connect(SqlLiteConnectionHelper.abs_path_to_sqlite)
        self.cur = con.cursor()
       
        pass
    
    def CreateTable(self,table_name, table_content):
        #table_content e de forma "(nume_coloana1 tip_coloana1,
        # nume_coloana2 tip_coloana2,nume_coloana3 tip_coloana3)"
        self.cur.execute('''CREATE TABLE {}
        ({})'''.format(table_name,table_content))

class HandMadeCsvHelpers:
    def __init__(self):
        pass
    @staticmethod
    def readcsv(file):
        v = []
        with open(file, 'r') as f:
            for line in f.readlines():
                line = line.strip('\n')
                v.append(line.split(','))
        return v

    @staticmethod
    def writecsv(file, lista):
        with open(file, 'w') as f:
            for sublista in lista:
                for i in range(len(sublista)):
                    if i == len(sublista) - 1:
                        f.write(sublista[i])
                    else:
                        f.write(sublista[i] + ',')
                f.write('\n')
        # print(f)

    @staticmethod
    def appendcsv(file, lista):
        with open(file, 'a') as f:
            for sublista in lista:
                for i in range(len(sublista)):
                    if i == len(sublista) - 1:
                        f.write(sublista[i])
                    else:
                        f.write(sublista[i] + ',')
                f.write('\n')
        # print(f)

class SaveHelper:
    def __init__(self):
        pass
    @staticmethod
    def saveEmailList(file,email):
        CSVHelpers.appendCSVFile(file,{'email':email})
        pass

    @staticmethod
    def saveWhitelist(file, public_key):
        CSVHelpers.appendCSVFile(file,{'public_key_x':public_key.W.x,'public_key_y':public_key.W.y})
        pass