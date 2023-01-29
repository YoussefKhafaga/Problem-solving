class Solution(object):
    def getNoZeroIntegers(self, n):
        for i in range(1, n):
            num = n-i
            number1 = str(num)
            number2 = str(i)
            no = 0
            for char in number1:
                if char == "0":
                    no = 1
            for char in number2:
                if char == "0":
                    no = 1
            if no == 0:
                return [i, n-i]