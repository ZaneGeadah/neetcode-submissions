class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        myList = dict() # hashmap of key = hashmaps, value = list

        for string in strs:
            
            occurrenceList = [0] * 26

            for char in string:
                index = ord(char) - ord('a')
                occurrenceList[index] += 1
            tupleList = tuple(occurrenceList)
            if tupleList in myList:
                myList[tupleList].append(string)
            else:
                myList[tupleList] = [string]

        return list(myList.values())