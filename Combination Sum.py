class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        res=[]
        candidates.sort()
        self.dfs(candidates, target, 0, [], res)
        return res
        
        
    def dfs(self,nums, target, index, path, res):
        if target<0:
            return
        if target==0:
            res.append(path)
            return
        for i in range(index, len(nums)):
            self.dfs(nums, target-nums[i], i, path+[nums[i]], res)

def stringToIntegerList(input):
    return json.loads(input)

def stringToInt(input):
    return int(input)

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
            candidates = stringToIntegerList(line)
            line = lines.next()
            target = stringToInt(line)
            
            ret = Solution().combinationSum(candidates, target)

            out = int2dArrayToString(ret)
            print out
        except StopIteration:
            break

if __name__ == '__main__':
    main()