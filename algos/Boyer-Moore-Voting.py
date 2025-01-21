# Boyer-Moore Voting Algorithm

def majorityElement(nums):
    candidate = None
    count = 0
    
    # First pass: find a candidate
    for num in nums:
        if count == 0:
            candidate = num
        count += 1 if num == candidate else -1
    
    # Optional: Verify candidate is majority if not guaranteed
    # if nums.count(candidate) > len(nums) // 2:
    #     return candidate
    # else:
    #     return None

    return candidate

# Example usage:
nums = [2,2,1,1,1,2,2]
print(majorityElement(nums))  # Output: 2
