class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        if not matrix:
            return
        a = len(matrix)
        if len(matrix[0])==1:
            if 0 in matrix:
                matrix[i] = [0 for i in range(a)]
        b = len(matrix[0])
        rows = []
        cols = []
        for i in range(a):
            for j in range(b):
                if matrix[i][j]==0:
                    if not(i in rows):
                        rows.append(i)
                    if not (j in cols):
                        cols.append(j)
        for row in rows:
            for j in range(b):
                matrix[row][j]=0
                
        for col in cols:
            for i in range(a):
                matrix[i][col]=0
        return

def stringToInt2dArray(input):
    return json.loads(input)

def int2dArrayToString(input):
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
            matrix = stringToInt2dArray(line)
            
            ret = Solution().setZeroes(matrix)

            out = int2dArrayToString(matrix)
            if ret is not None:
                print "Do not return anything, modify matrix in-place instead."
            else:
                print out
        except StopIteration:
            break

if __name__ == '__main__':
    main()