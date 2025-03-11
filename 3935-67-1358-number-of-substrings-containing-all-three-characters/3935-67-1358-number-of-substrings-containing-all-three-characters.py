

class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        count = { 'a': 0, 'b': 0, 'c': 0 }  # Dictionary to track character frequencies
        left = 0
        result = 0
        
        for right in range(len(s)):
            count[s[right]] += 1  # Add the current character
            
            # Ensure all three characters exist in the window
            while all(count.values()):  # This checks if a, b, and c are at least 1
                result += len(s) - right  # Count substrings ending at 'right'
                count[s[left]] -= 1  # Shrink window from left
                left += 1
        
        return result

