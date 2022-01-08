import os

dict = {1: "andrei", 2: "carla", 3: "Levente", 4: "Levente"}

#"cheie1 valoare1, cheie2 valoare2, cheie3 valoare3, etc"
def transformare_dictionar_in_string (dict):
    s=""
    for i in dict.keys():
        s=s+str(i)+" "+str(dict[i])+", "
    s = s[0:len(s)-2:]
    return s

#print (transformare_dictionar_in_string(dict))
#si o functie care transforma o lista de liste de forma [[a1,b1],[a2,b2],[a3,b3]...[an,bn]]
# intr-un string de forma "a1 b1, a2 b2, a3 b3, ..., an bn"
v=[["Nana", "Floare"],["Cană","Deuntura"],["Mistar","Ardei"]]
def transformare_dictionar_de_matrice_lista_de_liste_in_string(v):
    s = ""
    for i in v:
        s=s+i[0]+" "+i[1]+", "
    s=s[0:len(s)-2:]
    return s
#print (transformare_dictionar_de_matrice_lista_de_liste_in_string(v))

#functie pentru citire csv
# citim linie cu linie

def readcsv(file):
    v=[]
    with open(file, 'r') as f:
        for line in f.readlines():
            line = line.strip('\n')
            v.append(line.split(','))
    return v

def writecsv(file,lista):
    with open(file,'w')as f:
        for sublista in lista:
            for i in range(len(sublista)):
                if i==len(sublista)-1:
                    f.write(sublista[i])
                else:
                    f.write(sublista[i] +',')
            f.write('\n')
    print(f)

def appendcsv(file,lista):
    with open(file,'a')as f:
        for sublista in lista:
            for i in range(len(sublista)):
                if i==len(sublista)-1:
                    f.write(sublista[i])
                else:
                    f.write(sublista[i] +',')
            f.write('\n')
    print(f)
#appendcsv("backend/database/whitelist1.csv",readcsv("backend/database/test1.csv"))
#writecsv("backend/database/whitelist1.csv",readcsv("backend/database/test1.csv"))