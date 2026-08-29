class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        myList = dict()
        for char in s:
            if char in myList:
                myList[char] += 1
            else:
                myList[char] = 1
        for char in t:
            if char in myList:
                myList[char] -= 1
            else:
                return False
        print(myList)
        for value in myList.values():
            if value != 0:
                return False
        return True
        