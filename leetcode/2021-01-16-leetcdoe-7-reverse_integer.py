import functools
from typing import List


class Solution:
    def reverse(self, x: int) -> int:
        '''
         Runtime : 36ms
         Memory Usage : 14.3MB
         sol :  %연산으로 일의자리수 부터 구하여 reverse 숫자를 구함
        :param x:
        :return:
        '''
        # set variable
        sign = 1
        ans = 0
        
        #  check whether positive and negative
        if x < 0:
            sign = -1
            x = -x
        
        # algorithm for reverse integer
        while x > 0:
            ans = ans * 10 + x % 10
            x = int(x / 10)
        # overflow check
        if ans > 2 ** 31 - 1:
            return 0
        else:
            return sign * ans
    
    def reverse2(self, x: int) -> int:
        '''
          string으로  reverse str구하고 sign를 구함
        :param x: x 
        :return: 
        '''
        sign = 1
        if x < 0:
            sign = -1
            x = -x
        # reverse str
        ans = str(x)[::-1]
        ans = int(ans)
        # overflow check
        if ans < -(2 ** 31) or ans > 2 ** 31 - 1:
            return 0
        else:
            return -ans if sign == -1 else ans


if __name__ == '__main__':
    '''
    example1
    Input : x=123
    Output : 321
    example2
    Input : x=-123
    Output : -321
    example3
    Input : x=120
    Output : 21
    example4
    Input : x=0
    Output : 0
    '''
    
    sol = Solution()
    input = [123, -123, 120, 0]
    for i in input:
        print(sol.reverse(i))
