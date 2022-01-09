import re
def abs_diff(a, b):
    s=a-b
    if s<0:
        s=-s
    return s


x = int(input())
y = int(input())
d= abs_diff(x, y)
print(d)

def search(x,ln):
    for i in ln:
        if i==x:
            return True
    return False

def find_last(x,ln):
    index=-1
    for i in range(len(ln)):
        if x==ln[i]:
            index=i
    if index==-1:
        return False
    return index

def remove_duplicates(ln):
    ln2= list(set(ln))
    for i in range(len(ln2)):
        ln[i]=ln2[i]
    while len(ln)>len(ln2):ln.pop()

def check_subsequence(l1,l2):
    return str(l1).replace("[","").replace("]","") in str(l2)
    
def factorial(n):
    if n==0:return 1
    return n*factorial(n-1)

import math
def fact(n):
    p=1
    for i in range(1,n+1):
        p*=i
    return p


def fin_sum(x, n):
    minusOnePower= -1
    XPower= x
    s=0
    for i in range(1,n+1):
        s= s + (minusOnePower * (XPower * XPower)/fact(2*i))
        minusOnePower*=-1
        XPower*=x
    return s



import math
def fact(n):
    p=1
    for i in range(1,n+1):
        p*=i
    return p

def infin_sum(x, eps):
    minusOnePower= -1
    XPower= x
    s=0
    s_prev=1.0
    i=1
    while(math.fabs(s-s_prev)>eps):
        s_prev=s
        s= s + (minusOnePower * (XPower * XPower)/fact(2*i))
        minusOnePower*=-1
        XPower*=x
        i+=1
    return s

def gen_fibo(n):
    #your code here
    a=1;b=1
    yield 1;yield 1
    for i in range(3,n+1):
        c=a+b;
        a=b;
        b=c;
        yield c
        
print(f"There are {next(g)} numbers!")
for i in g:
    print(i)



import re

s= input()
ls= s.split(" ")
l1=[]
rexp="[aeiou]{2,}";
pattern2 = re.compile(rexp)
for ch in ls:
    if pattern2.findall(ch)!=[]:
        l1.append(ch)

print(l1)
s=input()
pattern="[0-9]{3,}";
print(re.findall(pattern,s))


s=input()
pattern="07[0-9]{8}";
print(re.findall(pattern,s))

s=input()
pattern="[a-z]+\.[a-z]+[0-9]?[0-9]?@e-uvt.ro"
print(re.findall(pattern,s))

s=input()
print(re.sub(" +"," ",s))


def replaceUnderAvg(matchobj):
    elt=matchobj.group(0);
    if elt[-1]==",":
        return ","
    return " "
    


s=input()
d={}
words=re.findall("[a-zA-z]+",s)
sum=0
for word in words:
    pattern="[^[a-zA-Z]]?"+word+"[^[a-zA-Z]]?";
    countApp= len(re.findall(pattern,' '+s + ' '))
    sum=sum+ countApp
    d[word]=countApp;

avg=sum/len(words)

for [key,value] in d.items():
    if value>avg:
        s=re.sub("[^[a-zA-Z]]?"+key+"[^[a-zA-Z]]?",replaceUnderAvg,s)
seps="-()'"
for sep in seps:
    s=s.replace(sep," ")
s=s.replace("  "," ")
print(s)

s= input()
print(" ".join([i for i in s.split(" ") if len(i)%2==1]))

# put your python code here

s= input()
print(" ".join([i for i in s.split(" ") if len(i)%2==1]))

s=input()
ls= s.split(" ")
print("ID: {} BP={} BC={}".format(ls[0],ls[1],ls[2]))


s= input()

ls= s.split(" ")
ls = [int(i) for i in ls]
ls= sorted(ls,key=lambda x:-x)
s = "{:" + str(len(str(ls[0]))) + "d}"
for x in ls:
    print(s.format(x))

s= input()
result=""
for i in range(len(s)):
    if s[i]>='a' and s[i]<='z':
       result+= chr(ord(s[i])- 32)
    else: result+=s[i]
    
print(result)

n=int(input())
toDelete= [",",".","'"]
dict={}
for i in range(n):
    s=input()
    for td in toDelete:
        s=s.replace(td,"")
    ls=s.split(" ")
    for word in ls:
        if word not in dict.keys():
            dict[word]=0
        dict[word]+=1

for i in dict.keys():
    if dict[i]>1:
        print(i,dict[i])
a=input()
b=input()
print ( str(sorted(a.lower()))==str(sorted(b.lower())))


for i in range(3):
    for j in range(3):
        x=input()
        if i==j:print(x)

n = int(input())
result_matrix=[[0 for i in range(n)] for j in range(n)]
for k in range(2):
    for i in range(n):
        for j in range(n):
            x= int(input())
            result_matrix[i][j]+=x


for row in result_matrix:
    print(row)

n = int(input())
matrix1=[[0 for i in range(n)] for j in range(n)]
matrix2=[[0 for i in range(n)] for j in range(n)]
result_matrix=[[0 for i in range(n)] for j in range(n)]


for i in range(n):
    for j in range(n):
        matrix1[i][j]+=int(input())
for i in range(n):
    for j in range(n):
        matrix2[i][j]=int(input())



for i in range(n):
    for j in range(n):
        for k in range(n):
            result_matrix[i][j]+= (matrix1[i][k] * matrix2[k][j])
for row in result_matrix:
    print(row)

sum1=0
sum2=0
sum3=0
for row in lt:
    sum3+= row[1]
    sum1 = sum1+ row[1] * row[2]
    sum2+= row[2]
print(sum3//len(lt))
print(sum1/sum2)

n=int(input())

d=2
prime_divs=[]
while n>1:
    p=0
    while n%d==0:
        p+=1
        n/=d
    if p>0:
        prime_divs.append((d,p))
    d+=1

print(prime_divs)

dict={}
for word in ls:
    if len(word) not in dict.keys():
        dict[len(word)]=[word]
    else: 
        if word not in dict[len(word)]:
           dict[len(word)].append(word)

for [key,value] in dict.items():
    print(str(key) + ' = '+str(value))



n= int(input())
dict={}


for word in range(n):
    x=int(input())
    dict[x]=[]
    for d in range(2,x):
        if x%d==0:
            dict[x].append(d)
    if str(dict[x])==str([]):
        dict[x]=None

for [key,value] in sorted(dict.items()):
    if value!=None:
        print(str(key) + ': '+str(value))