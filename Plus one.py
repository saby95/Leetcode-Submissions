class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        if not digits:
            return[]
        g = len(digits)-1
        carry = 1
        while(g>=0):
            digits[g]+=carry
            if digits[g]//10 == 1:
                digits[g]= digits[g]%10
                carry = 1
                g-=1
            else:
                carry = 0
                break
        if carry==1:
            digits.insert(0,1)
        return digits

def stringToIntegerList(input):
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
            digits = stringToIntegerList(line)
            
            ret = Solution().plusOne(digits)

            out = integerListToString(ret)
            print out
        except StopIteration:
            break

if __name__ == '__main__':
    main()