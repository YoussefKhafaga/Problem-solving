def mergefunc(arr, left, right):
    i = j = k = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            arr[k] = left[i]
            i = i + 1
        else:
            arr[k] = right[j]
            j = j + 1
        k = k + 1
    while i < len(left):
        arr[k] = left[i]
        k = k + 1
        i = i + 1
    while j < len(right):
        arr[k] = right[j]
        k = k + 1
        j = j + 1
    return arr


def sort(arr):
    if len(arr) > 1:
        middle = len(arr) // 2
        left = arr[:middle]
        right = arr[middle:]
        sort(left)
        sort(right)
        arr = mergefunc(arr, left, right)
    return arr
class Solution(object):
    def sortArray(self, nums):
        return sort(nums)

    