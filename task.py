# def longestconsecutive(nums):
#     S=set(nums)
#     longest=0
#     for num in set(nums):
#         if num-1 not in S:
#             lenght=1
#             current=num
#             while current+1 in S:
#                 lenght+=1
#                 current+=1
#             longest=max(longest,lenght)    
#     return longest
# nums=[3,4,9,5,8,2,7,1,6]
# print(longestconsecutive(nums))   
# def longestsubstring(s):
#     longest=0
#     for i in range(len(s)):
#         seen=set()
#         count=0
#         for j in range(i,len(s)):
#             if s[j] in seen:
#                 break
#             count+=1
#             seen.add(s[j])
#         longest=max(longest,count)
#     return longest
# s="abcabcbb"
# print(longestsubstring(s))
# def max_water(height):
#     max_area = 0

#     for i in range(len(height)):
#         for j in range(i + 1, len(height)):

#             width = j - i
#             h = min(height[i], height[j])

#             area = width * h

#             max_area = max(max_area, area)

#     return max_area


# height = [1,8,6,2,5,4,8,3,7]
# print(max_water(height))
def three_sum(nums):
    result = []

    n = len(nums)

    for i in range(n):
        for j in range(i+1, n):
            for k in range(j+1, n):

                if nums[i] + nums[j] + nums[k] == 0:
                    triplet = sorted([nums[i], nums[j], nums[k]])

                    if triplet not in result:
                        result.append(triplet)

    return result


nums = [-1,0,1,2,-1,-4]
print(three_sum(nums))

