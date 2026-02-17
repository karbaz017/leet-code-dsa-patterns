class Solution:
    def longestKSubstr(self, s, k):
        # code here
        from collections import defaultdict
        
        longest_substring = ''

        if not s or k == 0:
            return -1

        freq = defaultdict(int)
        left = 0
        max_len = -1

        for right in range(len(s)):
            freq[s[right]] += 1
            while len(freq) > k and left <= right:
                freq[s[left]] -= 1
                if freq[s[left]] == 0:
                    del freq[s[left]]
                left += 1
        
            if len(freq) == k:
                max_len = max(max_len, right - left + 1)
        
        return max_len
