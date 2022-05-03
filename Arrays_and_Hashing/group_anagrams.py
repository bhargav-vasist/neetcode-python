List = list


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groupedMap = {}
        ordList = list(map(sorted, strs))
        for idx, item in enumerate(ordList):
            if item not in groupedMap:

        return [[""]]


Solution().groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"])
