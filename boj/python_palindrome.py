import sys


def palindrome(str):
    flag = True
    for i in range(len(str) // 2):
        if str[i] != str[-1 - i]:
            flag = False
            break
    return flag


def palindrome2(str):
    return str == str[::-1]


def palind3(str):
    return list(str) == list(reversed(str))


def palin4(str):
    return str == ''.join(reversed(str))


def ngram(s):
    ans = []
    for i in range(len(s) - 2):
        ans.append((str(s[i] + s[i + 1]+s[i+2])))
    return ans

def gram(text):
    return list(map(''.join,list(zip(text,text[1:],text[2:]))))


if __name__ == '__main__':
    test = list(map(str, sys.stdin.readline().split()))
    print(test)
    for case in test:
        print(case, " palindrome=", palindrome2(case))
        print(case, " 2gram=>", ngram(case))
        print(case, " 3gram=>",gram(case))

    text = 'hello'
    print(list(zip(*[text[i:] for i in range(3)])))