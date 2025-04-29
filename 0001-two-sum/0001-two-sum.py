class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
         # Create a map to store the numbers we've seen so far.
        prevMap = {}

        # Iterate over the list, getting both the number and its index
        for index, num in enumerate(nums):
            # Calculate the difference betwen the target and the current number
            difference = target - num

            # Check if this difference has already been seen in the map
            # If it has, it means we found a pair of nums that add up to target
            if difference in prevMap:
                # Return the indices of the two numbers
                return [prevMap[difference], index]

            # If not, store the curr num with its index in the map
            prevMap[num] = index

        # If no pair is found that adds up to the target, return an empty list
        # Note: depending on the problem, this line can be modified or removed
        return []