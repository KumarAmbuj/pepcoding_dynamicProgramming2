def findDistinctSequence(s):
    dp=[0 for i in range(len(s)+1)]

    hash={}
    dp[0]=1
    for i in range(1,len(dp)):

        ch=s[i-1]
        dp[i]=2*dp[i-1]
        if ch in hash:
            dp[i]=dp[i]-dp[hash[ch]-1]

        hash[ch]=i

    print(dp[len(s)]-1)
s='abcbac'
findDistinctSequence(s)
s='abcabc'
findDistinctSequence(s)
