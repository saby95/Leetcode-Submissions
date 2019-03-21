class Solution(object):
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        sign=1
        if dividend<0:
            sign = -1 * sign
            dividend = -dividend
        if divisor<0:
            sign = -1 * sign
            divisor = -divisor
        ans =  sign*(dividend//divisor)
        if ans<= -2147483648:
            return -2147483648
        if ans>=2147483648:
            return 2147483647
        return ans

def stringToInt(input):
    return int(input)

def intToString(input):
    if input is None:
        input = 0
    return str(input)

def main():
    import sys
    def readlines():
        for line in sys.stdin:
            yield line.strip('\n')
    lines = readlines()
    while True:
        try:
            line = lines.next()
            dividend = stringToInt(line)
            line = lines.next()
            divisor = stringToInt(line)
            
            ret = Solution().divide(dividend, divisor)

            out = intToString(ret)
            print out
        except StopIteration:
            break

if __name__ == '__main__':
    main()