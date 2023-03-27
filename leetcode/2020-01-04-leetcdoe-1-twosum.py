import functools
from typing import List


class Solution:
    # approach1. brute force
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        answer = []
        for idx, val in enumerate(nums):
            tmp = val
            for idx2, val2 in enumerate(nums):
                if target == tmp + val2 and idx != idx2:
                    answer.append(idx)
                    answer.append(idx2)
                    return answer
    
    # aprpoch2 .hash-table(with dict)
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # empty dict
        answer = dict()
        
        # loop nums
        for idx, val in enumerate(nums):
            # complement + val = target
            complement = target - val
            # find answer set
            if complement in answer:
                return [answer[complement], idx]
            else:
                answer[val] = idx


if __name__ == '__main__':
    '''
    example1
    Input : nums=[2,7,11,15] target=9
    Output : [0,1]
    '''
    nums = [2, 7, 11, 15]
    target = 9
    sol = Solution()
    assert sol.twoSum(nums=nums, target=target) == [0, 3]
    
    '''
    example2
    Input : nums=[3,2,4] target=6
    Output : [1.2]
    '''
    nums = [3, 2, 4]
    target = 6
    assert sol.twoSum(nums=nums, target=target) == [0, 3]
