class Solution:
    def isPalindromic(self, s: str) -> bool:
        b="".join(f"{ord(c):08b}" for c in s)
        return b==b[::-1]
        
                
        
        
        