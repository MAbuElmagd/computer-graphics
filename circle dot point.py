import matplotlib.pyplot as plt
x0=0
y0=int(input("enter r:"))
arrx=[]
arry=[]
deltad=[]
d=(5/4)-y0
i=0
arrx.append(x0)
arry.append(y0)
while arrx[i]<arry[i]:
    if d<=0:
        arrx.append(arrx[i]+1)
        arry.append(arry[i])
        deltad.append(2*arrx[i]+3)
        print("("+str(arrx[i])+","+str(arry[i])+")"+ "d="+str(d)+"_^d="+str(deltad[i]))
        d=d+deltad[i]
    else:
        arrx.append(arrx[i]+1)
        arry.append(arry[i]-1)
        deltad.append(2*(arrx[i]-arry[i])+5)
        print("("+str(arrx[i])+","+str(arry[i])+")"+ "d="+str(d)+"_^d="+str(deltad[i]))
        d=d+deltad[i]
    i+=1
plt.plot(arrx,arry)
plt.show()
        
