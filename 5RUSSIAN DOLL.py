class Envelope:
    def __init__(self,w,h):
        self.w=w
        self.h=h
def partition(arr,p,r):
    x=arr[r]
    i=p-1

    for j in range(p,r):
        if arr[j].w<x.w:
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
            if arr[j].h<arr[i].h:
                if mx<lis[j]:
                    mx=lis[j]
        lis[i]=mx+1
    mx=0
    for i in range(len(lis)):
        mx=max(mx,lis[i])
    return mx
def MaxNonOverlappingEnvelope(width,height):
    arr=[]

    for i in range(len(width)):
        arr.append(Envelope(width[i],height[i]))

    Quicksort(arr,0,len(arr)-1)

    ans=findlis(arr)

    print(ans)

width=[17,26,25,48,63,42,9,4,21,68,58]
height=[5,18,34,84,72,86,55,70,45,76,51]
MaxNonOverlappingEnvelope(width,height)
