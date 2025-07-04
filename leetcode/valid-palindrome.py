class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower().strip()
        alphabet = "abcdefghijklmnopqrstuvwxyz1234567890"
        newstr = ""

        for c in s:
            if c in alphabet:
                newstr += c
        
        if len(newstr) <= 1:
            return True
        
        l = 0
        r = len(newstr) - 1

        while l <= r:
            if newstr[l] != newstr[r]:
                return False
            l += 1
            r -= 1
        
        return True