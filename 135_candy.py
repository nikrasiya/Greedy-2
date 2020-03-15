from typing import List


class Solution:
    def candy(self, ratings: List[int]) -> int:
        if not ratings:
            return 0

        result = [1] * len(ratings)

        for i in range(1, len(ratings)):
            if ratings[i] > ratings[i - 1]:
                result[i] = result[i - 1] + 1

        for i in reversed(range(len(ratings) - 1)):
            if ratings[i] > ratings[i + 1] and result[i] <= result[i + 1]:
                result[i] = result[i + 1] + 1

        return sum(result)
