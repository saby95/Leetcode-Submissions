class Solution(object):
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        n1=0
        n2=0
        i=0
        l1=len(num1)
        l2=len(num2)
        for i in range(max(l1,l2)):
            if i>=l1:
                pass
            else:
                n1 = n1*10 + (ord(num1[i])-48)
            if i>=l2:
                pass
            else:
                n2 = n2*10 + (ord(num2[i])-48)
        res = n1*n2
        ret = ""
        if not res:
            return "0"
        while(res!=0):
            ret += chr((res%10)+48)
            res = res//10
        return ret[::-1]

def stringToString(input):
    return input[1:-1].decode('string_escape')

def main():
    import sys
    def readlines():
        for line in sys.stdin:
            yield line.strip('\n')
    lines = readlines()
    while True:
        try:
            line = lines.next()
            num1 = stringToString(line)
            line = lines.next()
            num2 = stringToString(line)
            
            ret = Solution().multiply(num1, num2)

            out = (ret)
            print out
        except StopIteration:
            break

if __name__ == '__main__':
    main()