class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        ret = ""
        if not strs:
            return ret
        g = len(max(strs,key=len))
        try:
            for i in range(g):
                tmp = strs[0][i]
                fl=True;
                for j in range(len(strs)):
                    if strs[j][i] == tmp:
                        continue
                    else:
                        fl=False
                        break
                if fl:
                    ret+=strs[0][i]
                else:
                    break
            return ret
        except IndexError:
            return ret

def stringToStringArray(input):
    return json.loads(input)

def main():
    import sys
    def readlines():
        for line in sys.stdin:
            yield line.strip('\n')
    lines = readlines()
    while True:
        try:
            line = lines.next()
            strs = stringToStringArray(line)
            
            ret = Solution().longestCommonPrefix(strs)

            out = (ret)
            print out
        except StopIteration:
            break

if __name__ == '__main__':
    main()