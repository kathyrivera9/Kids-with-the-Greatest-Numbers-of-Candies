import numpy
class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        result = []
        max = numpy.amax(candies)
        for i in range(len(candies)):
            if(candies[i] + extraCandies >= max):
                result.append(True)
            else:
                result.append(False)
        return result
