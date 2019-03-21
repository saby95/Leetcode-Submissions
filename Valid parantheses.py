class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if not s:
            return True
        j=-1
        l=[]
        comp = {')':'(',']':'[','}':'{'}
        try:
            for i in range(len(s)):
                if s[i] in [')',']','}']:
                    if (l[j]==comp[s[i]]):
                        del l[j]
                        j -= 1
                    else:
                        return False
                elif s[i] in ['[','(','{']:
                    j+=1
                    l.append(s[i])
            return not(l)
        except IndexError:
            return False

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
            s = stringToString(line)
            
            ret = Solution().isValid(s)

            out = (ret)
            print out
        except StopIteration:
            break

if __name__ == '__main__':
    main()