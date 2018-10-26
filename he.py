import matplotlib.pyplot as plt
def sum(a,n):
    sum=0
    i=0
    while i<=n:
        sum+=a[i]
        i+=1
    return sum
x=int(input("enter the no. of gray lvls:"))

i=0
arr=[]
while i<x:
    arr.append(int(input("enter the value of "+str(i)+"level:")))
    i+=1
i=0
arr1=[]
arr[:]
while i<x:
    arr1.append(sum(arr,i))
    i+=1
en=(x-1)/arr1[x-1]
arr1[:]
i=0
arr2=[]
while i<x:
    arr2.append(round(en*arr1[i],0))
    i+=1
    arr2[:]
plt.bar(arr2,arr)
plt.xlabel('gray levels')
plt.ylabel('no. of pixels')
plt.title('Histogram equalization')
plt.axis([0, x, 0, 255])
plt.show()

    
    
              
         
