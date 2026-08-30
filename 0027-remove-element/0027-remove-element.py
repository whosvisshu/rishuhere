class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        # 'k' acts as the pointer for the next valid position
        k = 0
        
        # Iterate through the array with a reading pointer 'i'
        for i in range(len(nums)):
            # If the current element is not the value to remove
            if nums[i] != val:
                # Place it at the 'k'th index
                nums[k] = nums[i]
                # Increment 'k' to move to the next valid position
                k += 1
                
        # 'k' now represents the number of elements not equal to 'val'
        return k