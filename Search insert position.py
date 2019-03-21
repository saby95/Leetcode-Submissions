class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if not len(nums):
            return 0
        i = 0
        j = len(nums)-1
        while(True):
            if(target<=nums[i]):
                return i
            elif(target>=nums[j]):
                if target==nums[j]:
                    return j
                return j+1
            i+=1
            j-=1

def stringToIntegerList(input):
    return json.loads(input)

def stringToInt(input):
    return int(input)

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
            nums = stringToIntegerList(line)
            line = lines.next()
            target = stringToInt(line)
            
            ret = Solution().searchInsert(nums, target)

            out = intToString(ret)
            print out
        except StopIteration:
            break

if __name__ == '__main__':
    main()