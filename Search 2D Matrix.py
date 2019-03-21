class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if not matrix:
            return False
        a = len(matrix)
        b = len(matrix[0])
        for i in range(a):
            if target in matrix[i]:
                return True
        return False

def stringToInt2dArray(input):
    return json.loads(input)

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
            matrix = stringToInt2dArray(line)
            line = lines.next()
            target = stringToInt(line)
            
            ret = Solution().searchMatrix(matrix, target)

            out = (ret)
            print out
        except StopIteration:
            break

if __name__ == '__main__':
    main()