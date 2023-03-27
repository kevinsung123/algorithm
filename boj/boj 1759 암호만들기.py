import sys
from itertools import combinations

vowels = ['a', 'e', 'i', 'o', 'u']

if __name__ == '__main__':


    L, C = map(int, sys.stdin.readline().split())
    alpha = list(map(str, sys.stdin.readline().split()))

    for t in combinations(sorted(alpha), L):
        vowel_cnt = 0
        consonant_cnt = 0
        for chk in list(t):

            if chk in vowels:
                vowel_cnt += 1
            else:
                consonant_cnt += 1

        if vowel_cnt >= 1 and consonant_cnt >= 2:
            print(''.join(t))
