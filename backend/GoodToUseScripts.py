from hashlib import sha256
from datetime import datetime
from ecpy.keys       import ECPublicKey, ECPrivateKey
from ecpy.curves     import Curve,Point
import os, sys
import csv
import random
import uuid
from Blockchain_ready_Gandolh import Blockchain,Block,Transaction,updatehash,keyFromHash;

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
poolPublicKeys=[]
def Vote(poolId,privateKeyUser, option):
    #se realizeaza actiunea de votare
    #iau adresa publica a optiunii
    hash=updatehash(option,poolId) #to combine em both
    publicKey=keyFromHash(hash).get_public_key()
    optionPicked = [p for p in poolPublicKeys if str(p)==str(publicKey)]
    if optionPicked.length!=0:
        optionPicked=optionPicked[0]
        #work in progress


if __name__=='__main__':
    #createCSVFile("test1.csv", ["Nume", "Prenume", "Data"])
    #appendCSVFile("test1.csv", {"Nume": "Bradea", "Prenume": "Vlad", "Data": "Azi"})
    IAcoin=Blockchain()
    # initializareLantDeBlocuri(IAcoin)
    # print(IAcoin)
    poolId=str(uuid.uuid4())
    poolPublicKeys=getWalletsForPoolOptions(['a','b','c','d','e'],poolId)
    print(poolPublicKeys)
    Vote(poolId,'','c')
