from collections import Counter
import heapq


class Solution(object):
    def leastInterval(self, tasks, n):

        task_counts = Counter(tasks)
        max_heap = [-count for count in task_counts.values()]
        heapq.heapify(max_heap)

        time = 0

        while max_heap:
            temp = []
            for _ in range(n + 1):
                if max_heap:
                    count = heapq.heappop(max_heap)
                    if count + 1 < 0:
                        temp.append(count + 1)

                time += 1

                if not max_heap and not temp:
                    break

            for item in temp:
                heapq.heappush(max_heap, item)

        return time
