class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # s = HARJAS
        # K = 3
        if k >= len(s):
            return len(s)
        
        freq = [0] * 26
        start = 0
        max_l = 0
        max_freq  = 0
        #AAABABB
        #K = 1


        for i in range(len(s)):
            curr_length = i - start + 1
            index = ord(s[i]) - ord('A')
            print(index)
            freq[index] += 1
            for io in range(26):
                max_freq = max(max_freq, freq[io])    
            print("curr")
            print(max_freq)
            max_l = max(max_l, curr_length)
            if (curr_length - max_freq > k):
                max_l -= 1
            while curr_length - max_freq > k:
                index2 = ord(s[start]) - ord('A')
                freq[index2] -= 1
                start += 1
                curr_length = i - start + 1
        return max_l
        




        