class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_l = 0;
        start = 0
        # dict<int,int> subs
        subs = dict()

        for end in range(len(s)):
            curr_length = end - start + 1
            char = s[end]
            if char in subs:
                subs[char] += 1
            else:
                subs[char] = 1
            
            while (len(subs) < curr_length):
                x = s[start]
                if subs[x] <= 1:
                    # subs.delete(x)
                    del subs[x]
                else:
                    subs[x] -= 1
                start += 1
                curr_length = end - start + 1
            
            max_l = max(max_l, curr_length)
        return max_l
        