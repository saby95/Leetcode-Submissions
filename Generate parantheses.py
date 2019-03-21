class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        if n == 0:
            return [""]
        
        def dfs(t):
            path, l, r = t
            if l + r == 2 * n:
                return [path]
            else:
                res = []
                if l < n:
                    res += dfs((path + '(', l + 1, r))
                if l > r:
                    res += dfs((path + ')', l, r + 1))
                return res
                
        return dfs(("", 0, 0))

def stringToInt(input):
    return int(input)

def stringArrayToString(input):
    return json.dumps(input)

def main():
    import sys
    def readlines():
        for line in sys.stdin:
            yield line.strip('\n')
    lines = readlines()
    while True:
        try:
            line = lines.next()
            n = stringToInt(line)
            
            ret = Solution().generateParenthesis(n)

            out = stringArrayToString(ret)
            print out
        except StopIteration:
            break

if __name__ == '__main__':
    main()