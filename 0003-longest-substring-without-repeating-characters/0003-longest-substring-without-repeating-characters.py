class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_map = {}
        left = 0
        max_length = 0
        
        for right in range(len(s)):
            if s[right] in char_map:
                # Move the left pointer just past the previous occurrence of the character
                # We use max() to ensure the left pointer doesn't move backward
                left = max(left, char_map[s[right]] + 1)
                
            # Update the latest index of the character
            char_map[s[right]] = right
            
            # Update the maximum length found so far
            max_length = max(max_length, right - left + 1)
            
        return max_length