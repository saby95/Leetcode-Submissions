class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not(s):
            return 0
        l = 0
        r = 0
        fl=0
        try:
            while(s[r]):
                if s[r] == ' ':
                    fl+=1
                    r += 1
                    continue
                if fl:
                    l = r
                    fl=0
                r+=1
        except IndexError:
            if fl:
                return r-l-fl
            return r-l

def stringToString(input):
    return input[1:-1].decode('string_escape')

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
            s = stringToString(line)
            
            ret = Solution().lengthOfLastWord(s)

            out = intToString(ret)
            print out
        except StopIteration:
            break

if __name__ == '__main__':
    main()