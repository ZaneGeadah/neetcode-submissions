class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        myList = dict() # hashmap of key = hashmaps, value = list

        for string in strs:
            s = sorted(string)
            sortedString = ''.join(s)
        
            if sortedString in myList:
                myList[sortedString].append(string)
            else:
                myList[sortedString] = [string]

        return list(myList.values())