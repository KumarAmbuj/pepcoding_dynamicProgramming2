def wordbreak(s,word):
    n=len(s)
    dp=[0 for i in range(n)]

    for i in range(n):
        for j in range(0,i+1):
            ch=s[j:i+1]
            if ch in word:
                if j>0:
                    dp[i]+=dp[j-1]
                else:
                    dp[i]+=1
    print(dp[n-1]>0)

s = "leetcode"
word = ["leet", "code"]
wordbreak(s,word)

s = "a"
word = ["a"]
wordbreak(s,word)