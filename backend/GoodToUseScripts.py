from hashlib import sha256
from datetime import datetime
from ecpy.keys      import ECPublicKey, ECPrivateKey
from ecpy.curves     import Curve,Point
import os, sys
import csv
import random
import uuid
from Blockchain_ready_Gandolh import Blockchain,Block,Transaction,updatehash,keyFromHash;
import math
import json

path_to_database = "backend/database/"

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


def createCSVFile(new_file, list_of_header):
    #creaza un csv file cu denumirea {new_file} si creaza header-ul din list_of_header
    if new_file in os.listdir(path_to_database):
        raise "Fisierul se afla deja in baza de date!"
    else:
        with open(path_to_database + new_file, 'w', newline="") as f:
            writer = csv.writer(f)
            writer.writerow(list_of_header)


def appendCSVFile(file, dict_values_forCSV):
    #primeste ca parametrii numele unui fisier si un dictionar cu care s-ar completa csv-ul
    #da append fisierului cu datele corespunzatoare.
    if not(file in os.listdir(path_to_database)):
        raise "Fisierul nu se afla in baza de  date!"
    else:
        with open(path_to_database + file, 'r', newline="") as f:
            reader = csv.reader(f)
            header = next(reader)
        with open(path_to_database + file, 'a', newline="") as f2:
            list_date = [0,] * len(header)
            for key in dict_values_forCSV.keys():
                list_date[header.index(key)] = dict_values_forCSV[key]
            writer = csv.writer(f2)
            writer.writerow(list_date)


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


def getWalletsForPoolOptions(options,poolId):
    # Functia primeste variantele ca string-uri si creaza wallet-uri
    #am folosit cheia publica pentru a nu permite sa se faca tranzactii de la optiuni catre
    #alte walleturi
    publicKeys=[]
    for option in options:
        hash=updatehash(option,poolId) #to combine em both
        privateKey=keyFromHash(hash)
        publicKeys.append(privateKey.get_public_key())
    return publicKeys



def Vote(poolId,privateKeyUser, option):
    #se realizeaza actiunea de votare
    #iau adresa publica a optiunii
    hash=updatehash(option,poolId) #to combine em both
    publicKey=keyFromHash(hash).get_public_key()
    optionPicked = [p for p in poolPublicKeys if str(p)==str(publicKey)]
    if len(optionPicked)!=0:
        optionPicked=optionPicked[0]
        


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


def createTestingUsers(in_file, i):
    letter = chr(ord("a") + i) + "_user"
    letter_hash = updatehash(letter)
    private_key = keyFromHash(letter_hash)
    public_key = private_key.get_public_key()
    appendCSVFile(in_file, {"public_key_x": public_key.W.x, "public_key_y": public_key.W.y})


def readAllUsers(in_file):
    with open(path_to_database + in_file, "r") as f:
        reader = csv.reader(f)
        line = next(reader)
        print(line)
        all_users = []
        for x in reader:
            x[0] = int(x[0])
            x[1] = int(x[1])
            all_users.append(x)
    return all_users

#merge doar pentru naturale
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


def rand_str( str_size):
    return ''.join(random.choice('abcdefghijklmnopqrstuvwxyz') for x in range(str_size))


def getRandomOptions():
    l = []
    for i in range(20):
        dict = {"optiune{}".format(i + 1): random.randint(1, 200)}
        l.append(dict)
    return json.dumps(sortOptions(l))

def InitializePoolVote(poolId):
    #createBlock with poolId and predefined list of options
    poolPublicKeys=[]
    poolPublicKeys=getWalletsForPoolOptions(['a','b','c','d','e'],poolId)
    print(poolPublicKeys)
    pass



if __name__=='__main__':
    #createCSVFile("test1.csv", ["Nume", "Prenume", "Data"])
    #appendCSVFile("test1.csv", {"Nume": "Bradea", "Prenume": "Vlad", "Data": "Azi"})
    IAcoin=Blockchain()
    # initializareLantDeBlocuri(IAcoin)
    # print(IAcoin)


    poolId=str(uuid.uuid4())
    InitializePoolVote(poolId)
    Vote(poolId,'','c')

    # l = []
    # for i in range(20):
    #     dict = {"optiune{}".format(i + 1): random.randint(1, 200)}
    #     l.append(dict)
    # print(sortOptions(l))

    # createCSVFile("whitelist.csv", ["public_key_x", "public_key_y"])
    # for i in range(20):
    #     createTestingUsers("whitelist.csv", i)

    # print(readAllUsers("whitelist.csv"))

