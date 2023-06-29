class Bridge():
    def __init__(self,n,s):
        self.n=n
        self.s=s
def partition(arr,p,r):
    x=arr[r]
    i=p-1

    for j in range(p,r):
        if arr[j].n<x.n:
            i+=1
            arr[i],arr[j]=arr[j],arr[i]
    arr[i+1],arr[r]=arr[r],arr[i+1]
    return i+1
def Quicksort(arr,p,r):
    if p<r:
        q=partition(arr,p,r)
        Quicksort(arr,p,q-1)
        Quicksort(arr,q+1,r)

def findlis(arr):
    lis=[0 for i in range(len(arr))]

    for i in range(len(arr)):
        mx=0
        for j in range(i):
            if arr[j].s<arr[i].s:
                if mx<lis[j]:
                    mx=lis[j]

        lis[i]=mx+1
    mx=0
    for i in range(len(lis)):
        mx=max(mx,lis[i])

    return mx

def MaxNonOverlappingBridge(north,south):
    arr=[]
    for i in range(len(north)):
        arr.append(Bridge(north[i],south[i]))

    Quicksort(arr,0,len(arr)-1)

    ans=findlis(arr)

    print(ans)



north=[1,2,8,10,17,21,41,50,60,80]
south=[30,7,15,20,3,40,57,4,80,90]
MaxNonOverlappingBridge(north,south)