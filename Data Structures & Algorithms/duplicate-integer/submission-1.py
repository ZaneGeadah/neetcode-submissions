class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        myList = dict()
        for i in nums:
            if i in myList:
                return True
            myList[i] = 1
        return False

         
        