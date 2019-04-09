from prettytable import PrettyTable
n=int(input("donner el nombre de points: "))
x=[]
y=[]
for i in range (n):
    xi=int(input("donner x"+ str(i) +":"))
    yi=int(input("donner f(x"+ str(i) +") :"))
    x.append(xi)
    y.append(yi)
#### donner les point
l=[]
l.append(x)
l.append(y)
j=n-1
while (j>0):
    f1=[]
    cor=x
    img=l[-1]
    for i in range (j):
        a=(img[i+1]-img[i])/(cor[i+n-j]-cor[i])
        f1.append(round(a,3))
    l.append (f1)
    j=j-1
######f[xi,xi+1],f[xi,...,xi+2],f[xi,...,xi+3],.....
c1=['Xi','F(Xi)','F[Xi,Xi+1]']
for i in range (2,n):
    ch='F[Xi,...,Xi+'+ str(i) +']'
    c1.append(ch)
####colone1 de tab 
for i in range (2):
    for k in range (1,2*len(l[i])-1,2):
        l[i].insert(k,' ')
                
####les ligne 1 et 2
for i in range (2,len(l)):
    o=i-1
    for j in range (o):
        l[i].insert(0,' ')
        l[i].append(' ')
for i in range (2,len(l)-1):
    for x in range (1,2*len(l[i][i-1:len(l[i])-(i-1)])-1,2):
        l[i].insert(x+i-1, ' ')
#### tout les ligne        
table=PrettyTable(c1)

for i in range (2*n-1):
    h=[]
    for j in range (len (l)):
        h.append(str(l[j][i]))
    table.add_row(h)
print(table)
###  tab 
    

    
    
