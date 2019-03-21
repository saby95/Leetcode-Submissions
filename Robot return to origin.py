class Solution(object):
    def judgeCircle(self, moves):
        """
        :type moves: str
        :rtype: bool
        """
        if not moves:
            return True
        u = moves.count('U')
        d = moves.count('D')
        l = moves.count('L')
        r = moves.count('R')
        return u==d and l==r

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
            moves = stringToString(line)
            
            ret = Solution().judgeCircle(moves)

            out = (ret)
            print out
        except StopIteration:
            break

if __name__ == '__main__':
    main()