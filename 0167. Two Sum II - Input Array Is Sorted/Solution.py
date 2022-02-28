class Solution:
    def twoSum_1(self, numbers, target):
        """
        type numbers: List[int]
        type target: int
        rtype: List[int]
        """
        l, r = 0, len(numbers) - 1
        while l < r:
            total = numbers[l] + numbers[r]
            if total == target:
                return [l + 1, r + 1]
            elif total > target:
                r -= 1
            else:
                l += 1

    def twoSum_2(self, numbers, target):
        """
        type numbers: List[int]
        type target: int
        rtype: List[int]
        """
        for x in range(len(numbers)):
            low, high = 0, len(numbers) - 1
            while (low <= high):
                mid = int(low + (high - low) / 2)
                if target - numbers[x] == numbers[mid]:
                    if x == mid:
                        low = mid + 1
                    else:
                        return [x + 1, mid + 1]
                elif target - numbers[x] < numbers[mid]:
                    high = mid - 1
                else:
                    low = mid + 1
    
    def twoSum_3(self, numbers, target):
        """
        type numbers: List[int]
        type target: int
        rtype: List[int]
        """
        map = {}
        for i, num in enumerate(numbers):
            if target - num in map:
                return [map[target - num] + 1, i + 1]
            else:
                map[num] = i