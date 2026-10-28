class Solution(object):
    def fizzBuzz(self, n):
        Answer = []
        for n in range(n):
            if (n+1)%3 == 0 and (n+1)%5 == 0:
                Answer.append("FizzBuzz")
            elif (n+1)%3==0:
                Answer.append("Fizz")
            elif (n+1)%5 == 0:
                Answer.append("Buzz")
            else:
                Answer.append(str(n+1))
        return Answer
