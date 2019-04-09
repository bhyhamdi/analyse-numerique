import numpy as np
import matplotlib.pyplot as plt
n=int (input ('donne le degree max de polynome '))
n+=1
y =[]
l=[]
for i in range (n):
    l1=[]
    x=int(input ('donner x:'))
    fx = int (input ('donner f(x):'))
    y.append (fx)
    for j in range(n):
        l1.append (x**j)
    l.append (l1)
a= np.asarray(l)
b=np.asarray(y)
x = np.linalg.solve(a,b)
x.tolist()
ch=str(int(x[0]))
for i in range(1,len(x)):
    if x[i] !=0:
        xj=int(x[i])
        j=int(i)
        ch=ch+'+'+str(xj)+'x^'+str(j)
#####ch le ploy en chaine
v=np.linspace(-10,10,3)
w=[]
for j in range(len(v)):
    g=0
    for i in range (len(x)):
        g+=int(x[i])*(v[j]**i)
    w.append(g)
q=np.asarray(w)
plt.plot(v,q,label="p[x]")
plt.title(ch)##tittre de fig est le ploynome
plt.legend()

    

    
    
    
        
        

