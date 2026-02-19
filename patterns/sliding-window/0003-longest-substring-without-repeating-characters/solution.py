class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        from collections import defaultdict

        left = 0
        freq = defaultdict(int)
        max_len = 0

        for right in range(len(s)):
            freq[s[right]] += 1

            while freq[s[right]] > 1 and left <= right:
                freq[s[left]] -= 1
                if freq[s[left]] == 0:
                    del freq[s[left]]
                left += 1

            max_len = max(max_len, right - left + 1)
        
        return max_len
