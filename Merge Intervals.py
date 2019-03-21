# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        intervals.sort(key = lambda x : x.start)
        i = 0
        while i < len(intervals) - 1:
            if intervals[i+1].start <= intervals[i].end:
                intervals[i] = Interval(intervals[i].start,max(intervals[i].end,intervals[i+1].end))
                intervals.pop(i+1)
            else:
                i += 1
        return intervals

def stringToInterval(input):
    tokens = json.loads(input)
    return Interval(tokens[0], tokens[1])

def stringToIntervalArray(input):
    intervalArrays = json.loads(input)
    nodes = []
    for intervalArray in intervalArrays:
        nodes.append(stringToInterval(json.dumps(intervalArray)))
    return nodes

def intervalToString(interval):
    return "[{}, {}]".format(interval.start, interval.end)

def intervalArrayToString(intervalArray):
    serializedIntervals = []
    for interval in intervalArray:
        serializedInterval = intervalToString(interval)
        serializedIntervals.append(serializedInterval)
    return "[{}]".format(', '.join(serializedIntervals))

def main():
    import sys
    def readlines():
        for line in sys.stdin:
            yield line.strip('\n')
    lines = readlines()
    while True:
        try:
            line = lines.next()
            intervals = stringToIntervalArray(line)
            
            ret = Solution().merge(intervals)

            out = intervalArrayToString(ret)
            print out
        except StopIteration:
            break

if __name__ == '__main__':
    main()