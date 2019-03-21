class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x<0:
            return bool(0)
        s = ""
        while x>0:
            s += chr((x%10) + 48)
            x=x//10
        return s==s[::-1]

def stringToInt(input):
    return int(input)

def main():
    import sys
    def readlines():
        for line in sys.stdin:
            yield line.strip('\n')
    lines = readlines()
    while True:
        try:
            line = lines.next()
            x = stringToInt(line)
            
            ret = Solution().isPalindrome(x)

            out = (ret)
            print out
        except StopIteration:
            break

if __name__ == '__main__':
    main()