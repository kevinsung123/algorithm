from collections import defaultdict, Counter, OrderedDict
from typing import List

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
            nums_dic=OrderedDict(Counter(nums))
            for i,j in nums_dic.items():
                if j==1:
                    return i

if __name__ == '__main__':
    sol = Solution()
    ## ex1
    nums = [4, 1, 2, 1, 2]
    print(sol.singleNumber(nums))