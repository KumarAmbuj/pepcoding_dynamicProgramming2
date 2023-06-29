import sys
def palindromepartitioning(s):
    n=len(s)
    dp=[[False for j in range(n)] for i in range(n)]

    for g in range(n):
        i=0
        for j in range(g,n):
            if g==0:
                dp[i][j]=True
            elif g==1:
                if s[i]==s[j]:
                    dp[i][j]=True
                else:
                    dp[i][j]=False
            else:
                if s[i]==s[j] and dp[i+1][j-1]==True:
                    dp[i][j]=True
                else:
                    dp[i][j]=False

            i+=1
    dp1=[0 for i in range(n)]
    dp1[0]=0

    for j in range(1,n):
        if dp[0][j]==True:
            dp1[j]=0
        else:
            mn=sys.maxsize
            for i in range(j,0,-1):

                if dp[i][j]==True:
                    mn=min(mn,dp1[i-1])

            dp1[j]=mn+1

    print(dp1[n-1])

s='aab'
palindromepartitioning(s)

s='aba'
palindromepartitioning(s)
