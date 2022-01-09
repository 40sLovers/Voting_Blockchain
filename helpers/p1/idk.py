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





