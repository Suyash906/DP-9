class Solution:
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        if not envelopes:return 0
        
        envelopes.sort(key=lambda  key:key[0])
        
        max_num_envelopes = 1
        dp = [1 for _ in range(len(envelopes))]
        for i in range(1, len(envelopes)):
            for j in range(0,i):
                if envelopes[i][1] > envelopes[j][1] and envelopes[i][0] != envelopes[j][0]:
                    dp[i] = max(dp[i], dp[j]+1)
                    max_num_envelopes = max(max_num_envelopes, dp[i])
        
        return max_num_envelopes