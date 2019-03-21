class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        sign = 1
        if x<0:
            x = -x
            if x>0x80000000:
                return 0
            sign=-1
        elif x>=0x80000000:
            return 0
        ret=0
        while(x>0):
            ret = (ret*10) + (x%10)
            x=x//10
        if(ret*sign)>=0x80000000 or (ret*sign)<-0x80000000:
            return 0
        return sign*ret

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
            x = stringToInt(line)
            
            ret = Solution().reverse(x)

            out = intToString(ret)
            print out
        except StopIteration:
            break

if __name__ == '__main__':
    main()