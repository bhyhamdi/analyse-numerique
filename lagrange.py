import numpy as np
import matplotlib.pyplot as plt
###########
def pq(p,q):
    pq=[]
    pq.append(p[0]*q[0])
    for i in range (1,len (p)):
        pq.append (p[i]*q[0]+p[i-1]*q[1])
    pq.append (p[-1]*q[-1]) 
    return (pq)
#faire produit de 2 poly et q de degree 1  


###########
y=[]
x=[]
n=int (input('les nb de pt: '))
for i in range (n):
    l1=[]
    xi=int(input ('donner x:'))
    fx = int (input ('donner f(x):'))
    y.append (fx)
    x.append(xi)

#input les pts 


###########
lp=[]
for i in range (len (x)):
    lp.append([-1*x[i],1])


lp2=[]
for i in range (len(x)):
    p=[1]
    for j in range (len (x)):
        if i!=j:
            p=pq(p,lp[j])
    lp2.append(p)
#les ploy li(x)
########
den=[]
for i in range (len(x)):
    o=1
    for j in range (len(x)):
        if i!=j:
            o=o*(x[j]-x[i])
    den.append(o)


    
#den de li(x)

 #############
lc=[]
for i in range (n):
    a=y[i]
    for j in range (n):
        if i!=j :
            a=a/(x[i] -x[j])
    lc.append(a)
#les cof de li(x)
########
v=np.linspace(min(y),max(y),500)
tou=[]
for i in range (len (lp2)):
    t=[]
    for j in range (len(v)):
        m=0
        for k in range (len(lp2[i])):
            m+=((int(lp2[i][k])*(v[j]**k))/den[i])*y[i]
        t.append (m)
        tr=np.asarray(t)
        if len(t)== len(v):
            plt.plot(v,tr,label="l"+str (i)+"[x]")
        
        
        



    
#tracer le li (x)
#####
p=[]
for i in range (len (lc)):
    h=0
    for j in range(len (lc)):
        h=h+(int(lc[j])*lp2[j][i])
    p.append(h)
#le poly final

 ######

ch=str(int(p[0]))
for i in range(1,len(p)):
    if p[i] !=0:
        xj=int(p[i])
        j=int(i)
        ch=ch+'+'+str(xj)+'x^'+str(j)

    
#afficher le poyl final 


w=[]
for j in range(len(v)):
    g=0
    for i in range (len(p)):
        g+=int(p[i])*(v[j]**i)
    w.append(g)
q=np.asarray(w)
plt.plot(v,q,label="p[x]")
plt.title("p[x]="+ch)##tittre de fig est le ploynome
plt.legend()

    


    
    

    
                

