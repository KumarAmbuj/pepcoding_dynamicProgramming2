def findmaxincreasingsum(arr):
    dp=[0 for i in range(len(arr))]

    for i in range(len(arr)):
        mx=0
        for j in range(i):

            if arr[j]<arr[i]:
                if mx<dp[j]:
                    mx=dp[j]

        dp[i]=mx+arr[i]

    print(dp)
arr=[10,22,9,33,21,50,41,60,80,3]
findmaxincreasingsum(arr)