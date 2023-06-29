def burstballoon(arr):
    n = len(arr)
    dp = [[0 for i in range(n)] for j in range(n)]

    for g in range(n):
        i = 0
        for j in range(g, n):
            mx = 0
            for k in range(i, j + 1):
                left = (dp[i][k - 1] if k > i else 0)
                right = (dp[k + 1][j] if k < j else 0)
                val = (arr[i - 1] if i > 0 else 1) * arr[k] * (arr[j + 1] if j < n - 1 else 1)
                total = left + right + val
                if total > mx:
                    mx = total
            dp[i][j] = mx
            i += 1

    print(dp[0][n - 1])


arr = [3, 1, 5, 8]
burstballoon(arr)

