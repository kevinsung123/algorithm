from collections import Counter, OrderedDict, defaultdict


class Solution():
    def firstUniqChar(self, s: str) -> int:
        answer = -1
        s_dict = defaultdict(str)
        # 주어진 s를 dict에 저장 문자:횟수
        for chr in s:
            # 기존재
            if chr in s_dict:
                s_dict[chr] += 1
            else:
                s_dict[chr] = 1
        
        for idx, val in enumerate(s):
            # 나타난 횧수가 1이라면
            if s_dict[val] == 1:
                answer = idx
                return answer
        # 존재하지 않으면
        return answer

    def firstUniqChar2(self, s: str) -> int:

        #i : char j : cnt
        for i, j in OrderedDict(Counter(s)).items():
            print(i,j)
            # cnt가 1이라면
            if j == 1:
                return s.index(i)

     


if __name__ == '__main__':
    sol = Solution()
    ## ex1
    s = "leetcode"
    print(sol.firstUniqChar2(s))
    
    ## ex2
    s = "loveleetcode"
    print(sol.firstUniqChar2(s))
    
    ## ex3
    s = "aabb"
    print(sol.firstUniqChar2(s))
