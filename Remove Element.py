class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        if not nums:
            return 0
        i = 0
        for j in range(len(nums)):
            if nums[j]==val:
                i += 1
            else:
                nums[j-i] = nums[j]
        return len(nums)-i

def stringToIntegerList(input):
    return json.loads(input)

def stringToInt(input):
    return int(input)

def intToString(input):
    if input is None:
        input = 0
    return str(input)

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
            nums = stringToIntegerList(line)
            line = lines.next()
            val = stringToInt(line)
            
            ret = Solution().removeElement(nums, val)

            out = integerListToString(nums, len_of_list=ret)
            print out
        except StopIteration:
            break

if __name__ == '__main__':
    main()