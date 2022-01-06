from numpy import *;
import numpy as np;
import math;
import copy;
x5=np.arange(32)
x5=x5.tolist()
x4=[]
x3=[]
x2=[]
x1=[]
def lagrangian(alpha,beta,R):
    n=len(alpha)
    max=0
    for i in range(0,n):
        max=max+alpha[i]*alpha[i]/beta[i]
    max=R*sqrt(max)
    return max
alpha=[1,2,3,4,5]
n=1000 #The maximum of s.t.(can change)
R=sqrt(n)
beta=[5,4,3,2,1]
low_bound=176 #lower bound(can change)
up_bound=192 #upper bound(can change)
m=0
for j in range(0,32):
    alpha=[1,2,3,4]
    R=sqrt(n-j*j)
    beta=[5,4,3,2]
    ext=lagrangian(alpha,beta,R)+5*j
    if ext<=low_bound:
        x5.remove(j)
for i in x5:
    k=int(sqrt((n-i*i)/2))
    for j in range(0,k+1):
        alpha=[1,2,3]
        beta=[5,4,3]
        R=sqrt(n-i*i-2*j*j)
        ext=lagrangian(alpha,beta,R)+5*i+4*j
        if ext>low_bound:
            x4.append([i,j])
for i in x4:
    k=int(sqrt((n-i[0]*i[0]-2*i[1]*i[1])/3))
    for j in range(0,k+1):
        alpha=[1,2]
        beta=[5,4]
        R=sqrt(n-i[0]*i[0]-2*i[1]*i[1]-3*j*j)
        ext=lagrangian(alpha,beta,R)+5*i[0]+4*i[1]+3*j
        if ext>low_bound:
            x3.append([i[0],i[1],j])
for i in x3:
    k=int(sqrt((n-i[0]*i[0]-2*i[1]*i[1]-3*i[2]*i[2])/4))
    for j in range(0,k+1):
        alpha=[1]
        beta=[5]
        R=sqrt(n-i[0]*i[0]-2*i[1]*i[1]-3*i[2]*i[2]-4*j*j)
        ext=lagrangian(alpha,beta,R)+5*i[0]+4*i[1]+3*i[2]+2*j
        if ext>low_bound:
            x2.append([i[0],i[1],i[2],j])
print(len(x2))
for i in x2:
    k=int(sqrt((n-i[0]*i[0]-2*i[1]*i[1]-3*i[2]*i[2]-4*i[3]*i[3])/5))
    x1.append([i[0],i[1],i[2],i[3],k])
res=0
for i in x1:
    fin=5*i[0]+4*i[1]+3*i[2]+2*i[3]+i[4]
    if fin>=res:
        res=fin
print(res)
for i in x1:
    fin=5*i[0]+4*i[1]+3*i[2]+2*i[3]+i[4]
    if fin==res:
        print(i)
