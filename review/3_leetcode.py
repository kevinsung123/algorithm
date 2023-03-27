from collections import defaultdict, Counter


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        answer = 0
        # two pointer 를 활용하고 dict를 lookup테이블 이용
        lookup = dict()
        start = 0
        end = 0
        for end, val in enumerate(s):
            # 문자가 lookup에 있는지 체크
            # start 갱신
            # 반복문자 발견 그리고  start보다 크거나 같은경우
            if s[end] in lookup and lookup[s[end]] >= start:
                start = lookup[s[end]] + 1
            # 문자가 없을 경우 최대길이 갱신
            else:
                answer = max(answer, end - start + 1)
            # lookup 처음 참조
            lookup[s[end]] = end
            print(lookup,answer)
        print(answer)
        return answer


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
