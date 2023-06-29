import sys
def palindromePartitioning(s):
    n=len(s)
    dp1 = [[False for j in range(n)] for i in range(n)]

    for g in range(n):
        i=0
        for j in range(g,n):
            if g==0:
                dp1[i][j]=True

            elif g==1:
                if s[i]==s[j]:
                    dp1[i][j]=True
                else:
                    dp1[i][j]=False

            else:
                if s[i]==s[j] and dp1[i+1][j-1]==True:
                    dp1[i][j]=True
                else:
                    dp1[i][j]=False
            i+=1


    dp=[[0 for j in range(n)] for i in range(n)]

    for g in range(n):
        i=0

        for j in range(g,n):
            if g==0:
                dp[i][j]=0

            elif g==1:
                if s[i]==s[j]:
                    dp[i][j]=0
                else:
                    dp[i][j]=1

            else:
                if dp1[i][j]==True:
                    dp[i][j]=0
                else:
                    mn = sys.maxsize
                    for k in range(i, j):
                        mn = min(mn, dp[i][k] + dp[k + 1][j])
                    dp[i][j] = mn + 1


            i+=1

    print(dp[0][n-1])
s='aab'
palindromePartitioning(s)

s='efe'
palindromePartitioning(s)


