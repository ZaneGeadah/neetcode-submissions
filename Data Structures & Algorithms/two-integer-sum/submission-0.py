class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        myList = dict()
        index = 0
        for number in nums:
            if number in myList.keys():
                return [myList[number],index]
            else:
                myList[target - number] = index
                index += 1