import matplotlib.pyplot as plt
x0=int(input("enter x0:"))
y0=int(input("enter y0:"))
x1=int(input("enter x1:"))
y1=int(input("enter y1:"))
m=(y1-y0)/(x1-x0)
arrx=[]
arry=[]
d=0
i=0
arrx.append(x0)
arry.append(y0)
if m > 1 and m<-1:
    d=x0
    while i<(y1-y0+1):
        arry.append(arry[i]+1)
        d+=(1/m)
        arrx.append(round(d,0))
        print(str(arrx[i])+","+str(arry[i]))
        i+=1
else:
    d=y0
    while i<(x1-x0+1):
        d=d+m
        arrx.append(arrx[i]+1)
        arry.append(round(d,0))
        print(str(arrx[i])+","+str(arry[i]))
        i+=1
arrx.append(x1)
arry.append(y1)
plt.plot(arrx,arry)
plt.show()
