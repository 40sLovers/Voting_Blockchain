from hashlib import sha256
from datetime import datetime
from ecpy.keys       import ECPublicKey, ECPrivateKey
from ecpy.curves     import Curve,Point
import os, sys
import csv
from Blockchain_ready_Gandolh import Blockchain,Block,Transaction

path_to_database = "backend/database/"

def createCSVFile(new_file, list_of_header):
    if new_file in os.listdir(path_to_database):
        raise "Fisierul se afla deja in baza de date!"
    else:
        with open(path_to_database + new_file, 'w', newline="") as f:
            writer = csv.writer(f)
            writer.writerow(list_of_header)

def appendCSVFile(file, dict_values_forCSV):
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
    for i in range(0,20):
        now = datetime.now()
        # strftime=string format time
        now = now.strftime("%d/%m/%Y %H:%M:%S")

        block_nou = Block(now, [], blockChain.getLatestBlock().hash)
        block_nou.mineBlock(3)

        blockChain.chain.append(block_nou)
        #print(len(blockChain.chain))

#createCSVFile("test1.csv", ["Nume", "Prenume", "Data"])
#appendCSVFile("test1.csv", {"Nume": "Bradea", "Prenume": "Vlad", "Data": "Azi"})
#IAcoin=Blockchain()
#initializareLantDeBlocuri(IAcoin)
#print(IAcoin)
