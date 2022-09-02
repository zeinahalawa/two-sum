def twoSum(self, nums, target):
        for counter in range(len(nums)):
            for counters in range(counter+1, len(nums)):
                if nums[counter] + nums[counters] == target:
                    return [counter, counters]
