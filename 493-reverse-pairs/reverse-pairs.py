from typing import List

class Solution:
    def reversePairs(self, nums):

        # Merge two sorted halves
        def merge(arr, low, mid, high):
            temp = []
            left = low
            right = mid + 1

            while left <= mid and right <= high:
                if arr[left] <= arr[right]:
                    temp.append(arr[left])
                    left += 1
                else:
                    temp.append(arr[right])
                    right += 1

            while left <= mid:
                temp.append(arr[left])
                left += 1

            while right <= high:
                temp.append(arr[right])
                right += 1

            # Copy merged array back
            for i in range(low, high + 1):
                arr[i] = temp[i - low]

        # Count reverse pairs
        def countPairs(arr, low, mid, high):
            right = mid + 1
            cnt = 0

            for left in range(low, mid + 1):
                while right <= high and arr[left] > 2 * arr[right]:
                    right += 1

                cnt += (right - (mid + 1))

            return cnt

        # Merge Sort
        def mergeSort(arr, low, high):
            if low >= high:
                return 0

            mid = (low + high) // 2

            cnt = 0
            cnt += mergeSort(arr, low, mid)
            cnt += mergeSort(arr, mid + 1, high)

            # Count reverse pairs before merging
            cnt += countPairs(arr, low, mid, high)

            # Merge the sorted halves
            merge(arr, low, mid, high)

            return cnt

        return mergeSort(nums, 0, len(nums) - 1)