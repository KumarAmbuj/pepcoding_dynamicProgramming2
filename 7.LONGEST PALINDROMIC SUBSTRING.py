def findLongestPalindromicSubstring(s):
    dp=[[False for j in range(len(s))] for i in range(len(s))]

    l=0

    for g in range(len(s)):
        i=0
        j=g
        while(j<len(s)):

            if g==0:
                dp[i][j]=True
            elif g==1:
                if s[i]==s[j]:
                    dp[i][j]=True
            elif g>1:
                if s[i]==s[j] and dp[i+1][j-1]==True:
                    dp[i][j]=True
                else:
                    dp[i][j]=False
            if dp[i][j]==True:
                l=g+1
            i+=1
            j+=1
    print(l)
s='abccbc'
findLongestPalindromicSubstring(s)