import matplotlib.pyplot as plt
x0=int(input("enter x0:"))
y0=int(input("enter y0:"))
x1=int(input("enter x1:"))
y1=int(input("enter y1:"))
m=(y1-y0)/(x1-x0)
arrx=[]
arry=[]
deltad=[]
d=(y1-y0)-((x1-x0)/2)
i=0
arrx.append(x0)
arry.append(y0)
while arrx[len(arrx)-1]<x1:
    if d<=0:
        arrx.append(arrx[i]+1)
        arry.append(arry[i])
        deltad.append(y1-y0)
        print("("+str(arrx[i])+","+str(arry[i])+")"+ "d="+str(d)+"_^d="+str(deltad[i]))
        d=d+deltad[i]
    else:
        arrx.append(arrx[i]+1)
        arry.append(arry[i]+1)
        deltad.append(y1-y0-x1+x0)
        print("("+str(arrx[i])+","+str(arry[i])+")"+ "d="+str(d)+"_^d="+str(deltad[i]))
        d=d+deltad[i]
    i+=1
arrx.append(x1)
arry.append(y1)
plt.plot(arrx,arry)
plt.show()
        
