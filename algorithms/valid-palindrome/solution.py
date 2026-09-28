class Solution:
    def isPalindrome(self, s: str) -> bool:
        m=""
        
        for i in s:
            if i.isalnum():
                m+=i.lower()
        return m==m[::-1]