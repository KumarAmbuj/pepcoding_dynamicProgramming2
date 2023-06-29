def findDiffSubsequence(s):
    hash={}

    dp=[0 for i in range(len(s)+1)]

    dp[0]=1

    for i in range(1,len(s)+1):
        ch=s[i-1]
        if ch in hash:
            dp[i]=(2*dp[i-1])-dp[hash[ch]-1]
        else:
            dp[i]=2*dp[i-1]

        hash[ch]=i
    print(dp)
    print(dp[len(s)])
s='abcabc'
findDiffSubsequence(s)

s='abcbac'
findDiffSubsequence(s)
