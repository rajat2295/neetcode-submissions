class Solution:
    def isPalindrome(self, s: str) -> bool:
        result =[]
        for char in s:
            if char.isalnum():
                result.append(char)
        print(''.join(result),''.join(result[::-1]))
        return ''.join(result).lower() ==''.join(result[::-1]).lower()
