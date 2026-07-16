class Solution:
    def minWindow(self, s: str, t: str) -> str:
       

        # make sure that every char is t is in s
        # length
        t_dic = {}
        window = {}
        start = 0
        
        res = [-1,-1]
        reslen = float("infinity")
        have  = 0

        
        for i in range(len(t)):
            t_dic[t[i]] = t_dic.get(t[i], 0) + 1
        need = len(t_dic)
        for end in range(len(s)):
            window[s[end]] = window.get(s[end], 0) + 1
            if s[end] in t_dic and window[s[end]] == t_dic[s[end]]:
                have += 1
            while have == need:
                if (end - start + 1) < reslen:
                    reslen = end - start + 1
                    res = [start, end]
                window[s[start]] -= 1
                if s[start] in t_dic and window[s[start]] < t_dic[s[start]]:
                    have -= 1
                start += 1
        start, end = res
        return s[start : end + 1] if reslen != float("infinity") else ""

        
            

            
        #     if s[start] not in t_dic:
        #         start += 1
        #     if s[end] not in t_dic:
        #         end += 1
        #     else:
        #         res += s[i]
        #         s_dic[t[i]] = s_dic.get(s[i], 0) + 1
        #     if end > len(s):
        #         break
        # return res
            

            


            # tempchar = to_lower(s[q])
            # index = ord(s[q]) - ord('a')
            # freqs[index] += 1
        #     freqt.add(t[q])
        # if (len(freqt) <= len(freqs)) and len(s) >= len(t):
        #     curr_length = end - start + 1
        #     num_chars = 0
        #     while(num_chars < len(t)):
        #         if s[start] not in freqt:
        #             start += 1
        #         else if s[start] in freqt:
        #             num_chars
        #         if s[end] not in freqt:
        #             end -= 1
        #         else if s[end] in freqt:
        #             end += 1
                
                






        

            

