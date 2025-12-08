# Sliding Window Algorithm - Fixed Length and Variable Length

# Variable Length Sliding Window Algorithm
# Finding the longest substring problem

A = "abcabccbb"

def longestSubstring(s):
    l = 0
    longest = 0
    n = len(s)
    myset = set()
    
    for r in range(n):
        while s[r] in myset:
            myset.remove(s[l])
            l += 1
        
        w = (r - l) + 1
        longest = max(longest, w)
        myset.add(s[r])
        
    return longest

longval = longestSubstring(A)
print(longval)

# Fixed Length Sliding Window Algorithm
# Maximum Average Subarray Problem

B = [1, 12, -5, -6, 50, 3]
k = 4

def maximumAvgSubArray(nums, k):
    n = len(nums)
    curr_sum = 0
    
    for i in range(k):
        curr_sum += nums[i]
        
    max_avg = curr_sum / k
    
    for i in range(k, n):
        curr_sum += nums[i]
        curr_sum -= nums[i - k]
        
        avg = curr_sum / k
        max_avg = max(max_avg, avg)
        
    return max_avg

finalVal = maximumAvgSubArray(B, k)
print(finalVal)