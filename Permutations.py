class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        
        def permutations(num):
            if not len(num):
                return []
            if len(num) == 1:
                return [num]
            res = []
            cur = num[0]
            perms = permutations(num[1:])
            for perm in perms:
                for i in range(len(perm)+1):
                    res.append(perm[:i]+[cur]+perm[i:])
            return res
        if not nums:
            return[]
        if len(nums)==1:
            return [nums]
        result = permutations(nums)
        return result

def stringToIntegerList(input):
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
            nums = stringToIntegerList(line)
            
            ret = Solution().permute(nums)

            out = int2dArrayToString(ret)
            print out
        except StopIteration:
            break

if __name__ == '__main__':
    main()