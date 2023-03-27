from typing import List
import collections
from collections import deque


class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        '''
        # approach 1
        # previous to store the number being replaced
        # Time Complexity O(N*K)
        # Space Complexity O(1)
        '''
        for _ in range(k):
            previous = nums[-1]  # initiate a first previous
            for i in range(len(nums)):
                temp = nums[i]  # hodl nums[i]
                nums[i] = previous  # overwrite the current index
                previous = temp  # swap the value
    
    def rotate2(self, nums: List[int], k: int) -> None:
        '''
          approach 2
          list slicing

        '''
        k = k % len(nums)
        print(nums[-k:])
        print(nums[:-k])
        nums[:] = nums[-k:] + nums[:-k]
    
    def rotate3(self, nums: List[int], k: int) -> None:
        '''
        approch 3
        collections deque
        '''
        dq = collections.deque(nums)
        dq.rotate(k)
        nums = list(dq)
    
    def rotate4(self, nums: List[int], k: int) -> None:
        '''
        approch 3
        collections deque
        '''
        dq = collections.deque(nums)
        dq.rotate(k)
        nums = list(dq)
    
    def reverse(self, nums, start, end) -> None:
        while start < end:
            temp = nums[start]
            nums[start]= nums[end]
            nums[end]=temp
            start+=1
            end-=1
            
    
    def rotate5(self, nums: List[int], k: int) -> None:
        '''
        approch 3
        collections deque
        '''
        dq = collections.deque(nums)
        dq.rotate(k)
        nums = list(dq)


if __name__ == '__main__':
    nums = [1, 2, 3, 4, 5, 6, 7]
    k = 3
    s = Solution()
    
    print(s.rotate2(nums, k))
    
    nums = [-1, -100, 3, 99]
    k = 2
    print(s.rotate2(nums, k))
