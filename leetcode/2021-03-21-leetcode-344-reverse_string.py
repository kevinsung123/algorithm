from typing import List
class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """

        ## solve 1)
        # s[:] is editing the actual memory bytes s porint, to s= porint the variable name s to other bytes in the memory
        s[:]=s[::-1]
        
        ## solve 2)
        s.reverse()
        
        ## solve3) implementation by mirror image
        size =len(s)
        # reverse string by mirror image
        for i in range(size//2):
            s[i] , s[-i-1] =s[-i-1],s[i]
        
    
        
        


if __name__ == '__main__':
    s = ["h", "e", "l", "l", "o"]
    sol=Solution()
    sol.reverseString(s)
    
