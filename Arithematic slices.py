def findslices(arr):
    n=len(arr)
    dp=[0 for i in range(n)]

    ans=0

    for i in range(2,n):
        if arr[i]-arr[i-1]==arr[i-1]-arr[i-2]:
            dp[i]=dp[i-1]+1
        ans+=dp[i]

    print(ans)

arr=[1,2,3,4]
findslices(arr)