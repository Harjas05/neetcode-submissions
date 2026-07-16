class Solution:
    def isPalindrome(self, s: str) -> bool:
        l = 0
        temp = ""
        for c in s:
            if c.isalnum():
                temp += c.lower()
        
        r = len(temp) - 1


        while (l < r):
            if temp[l] != temp[r]:
                return False
            l += 1
            r -= 1
        return True