from collections import defaultdict, Counter


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        used_char = defaultdict(int)
        left = 0
        ans = 0
    
        for idx,chr in enumerate(s):
            # first chr
            if s[idx] in used_char and used_char[s[idx]] >= left:
                left = used_char[s[idx]] + 1
            else:
                ans = max(ans, idx - left + 1)
            used_char[s[idx]] = idx
        return ans
    
    def lengthOfLongestSubstring2(self, s: str) -> int:
        
        ans = 0
        start = 0
        end = 0
        lookupDict = {}
        while end < len(s):
            # if exists charater then update index
            if s[end] in lookupDict and lookupDict[s[end]] >= start:
                start = lookupDict[s[end]] + 1
            ans = max(ans, end - start + 1)
            
            # first character
            lookupDict[s[end]] = end
            end += 1
        print(ans)
        return ans


if __name__ == '__main__':
    sol = Solution()
    ## ex1
    s = "abcabcbb"
    sol.lengthOfLongestSubstring(s)
    
    ## ex2
    s = "bbbbb"
    sol.lengthOfLongestSubstring(s)
    
    ## ex3
    s = "pwwkew"
    sol.lengthOfLongestSubstring(s)
