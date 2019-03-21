class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        if not matrix:
            return []
        end_row = len(matrix)
        if end_row == 1:
            return matrix[0]
        end_row = end_row-1
        end_col = len(matrix[0])-1
        res = []
        start_row = 0
        start_col = 0
        fl = 1
        while(fl):
            if (start_row>end_row) or (start_col>end_col):
                fl=0
                break
            if (not (start_row-end_row)) and (not (start_col-end_col)):
                fl=0
                res = res+[matrix[start_row][start_col]]
                break
            if(not (start_col-end_col)):
                for i in range(start_row,end_row+1):
                    res = res+[matrix[i][start_col]]
                fl=0
                break
            
            if (not (start_row-end_row)):
                res = res+matrix[start_row][start_col:end_col+1]
                fl=0
                break
            
            res = res+matrix[start_row][start_col:end_col+1]
            for i in range(start_row+1,end_row):
                res = res+[matrix[i][end_col]]
            res = res+(matrix[end_row][start_col:end_col+1][::-1])
            for i in range(end_row-1,start_row,-1):
                res = res+[matrix[i][start_col]]
            start_row+=1
            start_col+=1
            end_row-=1
            end_col-=1
        return res

def stringToInt2dArray(input):
    return json.loads(input)

def integerListToString(nums, len_of_list=None):
    if not len_of_list:
        len_of_list = len(nums)
    return json.dumps(nums[:len_of_list])

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
            
            ret = Solution().spiralOrder(matrix)

            out = integerListToString(ret)
            print out
        except StopIteration:
            break

if __name__ == '__main__':
    main()