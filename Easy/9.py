x = 121

class Solution:
    def isPalindrome(x: int) -> bool:
        x = str(x)
        for i in range(len(x)):
            if x[i] == x[-1-i]:
                pass
            else:
                return False
        return True

Solution.isPalindrome(x)