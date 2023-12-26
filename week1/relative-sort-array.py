class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        already = {}
        lengthOfArr1 = len(arr1)

        for i in range(len(arr2)):
            already[arr2[i]] = i

        def relativeSort(x):
            if x in already:
                return already[x]
            return x + lengthOfArr1

        arr1.sort(key = relativeSort)
        return arr1