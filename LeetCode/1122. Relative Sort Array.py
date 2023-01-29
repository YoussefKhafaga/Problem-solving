class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        i = 0
        for element in arr2:
            for j in range(0, len(arr1)):
                if arr1[j] == element and arr1[i] ==element:
                    i += 1
                elif arr1[j] == element and arr1[i] != element:
                    arr1[i], arr1[j] = arr1[j], arr1[i]     
                    i += 1
        for j in range(i, len(arr1)):
            for k in range(j+1, len(arr1)):
                if arr1[j] > arr1[k]:
                    arr1[j], arr1[k] = arr1[k], arr1[j]
            
        return arr1