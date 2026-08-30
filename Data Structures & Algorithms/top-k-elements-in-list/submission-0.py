class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        myList = dict()
        maxHeap = []

        for number in nums:
            if number in myList:
                myList[number] += 1

            else:
                myList[number] = 1 # key is number, value is occurrence

        for number in myList.keys():
            heapq.heappush(maxHeap, [-myList[number], number])

        i = 0
        kthList = list()
        largest = list()
        while i < k:
            largest = heapq.heappop(maxHeap) # [2, 7]
            kthList.append(largest[1])
            i += 1

        return kthList