class Solution:
    def totalFruit(self, fruits: List[int]) -> int:

        from collections import defaultdict

        left = 0
        freq = defaultdict(int)
        max_len = 0

        for right in range(len(fruits)):
            freq[fruits[right]] += 1
            while len(freq) > 2 and left <= right:
                freq[fruits[left]] -= 1
                if freq[fruits[left]] == 0:
                    del freq[fruits[left]]
                left += 1

            max_len = max(max_len, right - left + 1)
        
        return max_len