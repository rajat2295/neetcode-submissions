class Solution:
    def isPalindrome(self, s: str) -> bool:
        result =[]
        pointer1, pointer2 = 0, len(s)-1
        while  pointer1 <= pointer2:
            if not (s[pointer1].isalnum()):
                pointer1 =1 + pointer1
                continue
            if not (s[pointer2].isalnum()):
                pointer2 = pointer2 -1
                continue
            
            if s[pointer1].lower() != s[pointer2].lower():
                print(s[pointer1],s[pointer2],pointer1,pointer2)
                return False
            pointer1 =1 + pointer1 
            pointer2 = pointer2 -1
        return True

       
