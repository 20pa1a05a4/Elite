class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_length = 0
        start = 0
        end = 0
        while(start < len(s) and end < len(s) and start <= end):
            while(end < len(s)-1 and s[end+1] not in s[start:end+1]):
                end += 1
            
            length = (end - start + 1)
            max_length = max(max_length,length)
            print(start,end)
            while(end < len(s) - 1 and s[start] != s[end+1]):
                start += 1 
            start += 1
            end += 1
            
        return max_length
