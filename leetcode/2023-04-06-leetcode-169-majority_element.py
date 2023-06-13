from collections import defaultdict, Counter, OrderedDict
from typing import List


class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        w1 = "FizzBuzz"
        w2 = "Fizz"
        w3 = "Buzz"
        answer = []
        print(n)
        for i in range(n):
            idx = i + 1
            if idx % 3 == 0 and idx % 5 == 0:
                answer.append(w1)
            elif idx % 3 == 0:
                answer.append(w2)
            elif idx % 5 == 0:
                answer.append(w3)
            else:
                answer.append(str(idx))
        return answer


class Solution3:
    def fizzBuzz(self, n: int) -> List[str]:
        """
        :param n: int
        :return: List[str]
        """
        # ans list
        answer = []

        # dictionary to store all fizzbuzz mappings
        dict = defaultdict()
        dict[3] = "Fizz"
        dict[5] = "Buzz"
        print(dict)
        # iterate from 1 to n
        for i in range(1, n + 1):
            num_ans_str = ""

            for key in dict.keys():
                if i % key == 0:
                    num_ans_str += dict[key]

            if not num_ans_str:
                num_ans_str = str(i)
            answer.append(num_ans_str)

        return answer


if __name__ == '__main__':
    sol = Solution3()
    ## ex1
    nums = [3, 5, 15]
    for n in nums:
        print(sol.fizzBuzz(n))
