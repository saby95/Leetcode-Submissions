class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        step=(numRows-1)*2
        ret = ""
        size=len(s)
        if numRows>size or numRows==1:
            return s
        for i in range(numRows):
            inner_step = step
            if i!=0 or i!=size-1:
                inner_step=i*2
            offset = i
            while(offset<size):
                ret=ret+s[offset]
                if(inner_step!=step):
                    inner_step=step-inner_step
                offset=offset+inner_step
            
        return ret

def stringToString(input):
    return input[1:-1].decode('string_escape')

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
            s = stringToString(line)
            line = lines.next()
            numRows = stringToInt(line)
            
            ret = Solution().convert(s, numRows)

            out = (ret)
            print out
        except StopIteration:
            break

if __name__ == '__main__':
    main()