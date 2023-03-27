import sys


class Solution:
    def reverseWords(self, string) -> str:
        # remove leading and trailing whitespace
        string.strip()

        # store strings splited by whitespace
        split_strings = string.split()
        # reverse each of string
        reversed_split_strings = list(reversed(split_strings))

        # join each of string by whitespace (1)
        answer = ' '.join(reversed_split_strings)
        return answer


if __name__ == '__main__':
    string = sys.stdin.readline()
    c = Solution()
    c.reverseWords(string)
