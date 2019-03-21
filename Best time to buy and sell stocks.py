class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if not prices or len(prices)==1:
            return 0
        maxsum=0
        minimum = prices[0]
        for i in range(1,len(prices)):
            if prices[i]<minimum:
                minimum = prices[i]
            else:
                if (prices[i]-minimum)>maxsum:
                    maxsum = prices[i]-minimum
        return maxsum

def stringToIntegerList(input):
    return json.loads(input)

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
            prices = stringToIntegerList(line)
            
            ret = Solution().maxProfit(prices)

            out = intToString(ret)
            print out
        except StopIteration:
            break

if __name__ == '__main__':
    main()