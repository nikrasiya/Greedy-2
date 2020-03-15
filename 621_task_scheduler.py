from typing import List
from collections import Counter


class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        """
            https://leetcode.com/problems/task-scheduler/
            Time Complexity - O(n)
            Space Complexity - O(1)
            'n' is the number of tasks.
        """
        if not tasks:
            return 0

        task_count = list(Counter(tasks).values())
        # the most occur element
        max_freq = max(task_count)
        # max count is max of max_freq
        max_count = task_count.count(max_freq)
        # partitions after placing max freq element
        partitions = max_freq - 1
        # empty slots after placing max_freq elements
        empty_slots = (n - (max_count - 1)) * partitions
        # slots required for pending slots
        pending_tasks = len(tasks) - (max_freq * max_count)
        # idle slots after placing all elements
        idle = max(0, empty_slots - pending_tasks)
        return len(tasks) + idle


if __name__ == '__main__':
    print(Solution().leastInterval(["A", "A", "A", "B", "B", "B"], 2))
