class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        j=0
        res =[]
        for i in range(m,m+n):
            nums1[i]=nums2[j]
            j+=1
        nums1.sort()

def stringToIntegerList(input):
    return json.loads(input)

def stringToInt(input):
    return int(input)

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
            nums1 = stringToIntegerList(line)
            line = lines.next()
            m = stringToInt(line)
            line = lines.next()
            nums2 = stringToIntegerList(line)
            line = lines.next()
            n = stringToInt(line)
            
            ret = Solution().merge(nums1, m, nums2, n)

            out = integerListToString(nums1)
            if ret is not None:
                print "Do not return anything, modify nums1 in-place instead."
            else:
                print out
        except StopIteration:
            break

if __name__ == '__main__':
    main()