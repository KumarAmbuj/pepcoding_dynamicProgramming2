def findbiotonic(arr):
    lis=[0 for i in range(len(arr))]
    lds=[0 for i in range(len(arr))]

    # for increasing
    for i in range(len(arr)):
        mx=0
        for j in range(i):
            if arr[j]<arr[i]:
                if mx<lis[j]:
                    mx=lis[j]

        lis[i]=mx+1

    # for decreasing
    for i in range(len(arr)-1,-1,-1):
        mx=0

        for j in range(len(arr)-1,i,-1):

            if arr[j]<arr[i]:
                if mx<lds[j]:
                    mx=lds[j]

        lds[i]=mx+1

    mx=0
    for i in range(len(arr)):
        mx=max(mx,lis[i]+lds[i])

    print(mx-1)

arr=[10,22,9,33,21,50,41,60,80,3]

findbiotonic(arr)