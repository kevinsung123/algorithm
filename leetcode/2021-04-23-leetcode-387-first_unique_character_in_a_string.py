from collections import defaultdict, Counter, OrderedDict


class Solution:
    def firstUniqChar(self, s: str) -> int:
        # order dict
        st = defaultdict(list)
        for idx, val in enumerate(s):
            st[val].append(idx)
        st = OrderedDict(sorted(st.items(), key=lambda x: x[0]))
        
        # get first uniq character
        for i in s:
            if len(st[i]) == 1:
                return st[i][0]
        return -1

    
    def firstUniqChar2(self, s: str) -> int:
        # Explaination: Ordered Dict will save the characters it encounters in
        # same sequence as the original string. Hence it becomes easy to catch hold of the first
        # unique character. Then according to the counter variable, whenever the first 1 is encountered
        # the corresponding dict.key's index is returned from the original String.
        dic = OrderedDict(Counter(s))
        for i, j in dic.items():
            if j == 1:
                return s.index(i)
        return -1


if __name__ == '__main__':
    sol = Solution()
    ## ex1
    s = "leetcode"
    print(sol.firstUniqChar(s))
    
    ## ex2
    s = "loveleetcode"
    print(sol.firstUniqChar(s))
    
    ## ex3
    s = "aabb"
    print(sol.firstUniqChar(s))
