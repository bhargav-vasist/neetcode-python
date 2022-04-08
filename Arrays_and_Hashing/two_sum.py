List = list


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        myDict = {}
        targetIdxList = []
        for idx, num in enumerate(nums):
            targetNum = target - num
            targetIdx = myDict.get(targetNum)
            if targetIdx is not None:
                targetIdxList.append(targetIdx)
                targetIdxList.append(idx)
                return targetIdxList
            else:
                myDict[num] = idx
                continue

    def twoSumPerf(self, nums: List[int], target: int) -> List[int]:
        d = {}
        for index, num in enumerate(nums):
            second = target - num
            if second in d:
                return [d[second], index]
            else:
                d[num] = index
        return []
