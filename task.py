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
# def three_sum(nums):
#     result = []

#     n = len(nums)

#     for i in range(n):
#         for j in range(i+1, n):
#             for k in range(j+1, n):

#                 if nums[i] + nums[j] + nums[k] == 0:
#                     triplet = sorted([nums[i], nums[j], nums[k]])

#                     if triplet not in result:
#                         result.append(triplet)

#     return result


# nums = [-1,0,1,2,-1,-4]
# print(three_sum(nums))
# def factorial(n):
#     fact=1
#     i=n
#     while i>0:
#         fact=fact*i
#         i=i-1
#     return fact
# print(factorial())    
# def max_passengers(n):
#     maxpassengers=0
#     passengers=10
#     a=input("give 2n inputs:").split()
#     for i in range(n):
#         x=int(a[2*i])
#         y=int(a[2*i + 1])
        
#         passengers=passengers+x
#         if y>passengers:
#             print("invalidoutput")
#             break
#         passengers=passengers-y
#         if passengers>maxpassengers:
#             maxpassengers=passengers
            
#     return maxpassengers
# print(max_passengers(2)
# hours=int(input("enter the hour: "))
# minutes=int(input("enter the minutes: "))
# print(hours ,minutes)
# hourhand=hours*30
# extra=(1/2)*minutes
# angleofhourhand=hourhand+extra
# minute_hand=minutes*6
# if minute_hand>angleofhourhand:
#     difference_of_angle=minute_hand-angleofhourhand
# if minute_hand<angleofhourhand:
#     difference_of_angle=angleofhourhand-minute_hand
# if difference_of_angle>=180:
#     print(360-difference_of_angle)
# expenses=[]
# def add_expense():
#     amount=float(input("Enter the expense: "))
#     category=input("Enter which category it belongs: ")
#     description=input("Enter the description: ")
#     expense={"amount":amount,
#              "category":category,
#              "description":description}
#     expenses.append(expense)
#     print("expense added succesfully")
# def view_expenses():
#     for expense in expenses:
#         print(expense)   
# def total_spending():

#     total = 0

#     for expense in expenses:
#         total += expense["amount"]

#     print(f"\nTotal Spending = {total}\n")

# def category_summary():
#     summary={}
#     for expense in expenses:
#         category=expense["category"]
#         if category not in summary:
#             summary[category]=0
#         summary[category]+=expense["amount"] 
#     for category in summary:


#         print(category,":",summary[category])    

# while True:
#     print("________EXPENSE TRACKER_______")
#     print("1.Add Expense")
#     print("2.View Expense")
#     print("3.Total Spending")
#     print("4.Category Summary")
#     print("5.Exit")
#     choice=input()
#     if choice == "1":
#         add_expense()

#     elif choice == "2":
#         view_expenses()

#     elif choice == "3":
#         total_spending()

#     elif choice == "4":
#         category_summary()

#     elif choice == "5":
#         print("Thank You!")
#         break

#     else:
#         print("Invalid Choice\n")
# nums=[2,4,6,7,8]
# newnums=[]
# for i in range(len(nums)):
#     product=1
#     for j in range(len(nums)):
#         if i!=j:
#             product=product*nums[j]
#     newnums.append(product)
# print(newnums)   
# def grouping(words):
#     group={}
#     for word in words:
#         key=sorted(word)
#         key=str(key)
#         if key not in group:
#             group[key]=[]
#         group[key].append(word)
#     return list(group.values())
# words = ["eat", "tea", "tan", "ate", "nat", "bat"]
# print(grouping(words))        

# nums = [4,6,7,8,9]
# newnums=[]
# maximum=0
# for num in nums:
#     maximum=max(maximum,num)
# for num in nums:
#     difference=maximum-num
#     if difference>0:
#         newnums.append(num)
# maximum2=0        
# for numbers in newnums:
#     maximum2=max(maximum2,numbers)
# print(maximum2)   
# nums = [1,2,4,5,8,9]

# for i in range(len(nums)-1):

#     current = nums[i]
#     next_num = nums[i+1]

#     for missing in range(current + 1, next_num):
#         print(missing)
s = input("Enter a string: ")

freq = {}

for ch in s:
    if ch in freq:
        freq[ch] += 1
    else:
        freq[ch] = 1

max_char = ""
max_freq = 0

for ch in freq:
    if freq[ch] > max_freq:
        max_freq = freq[ch]
        max_char = ch

print("Character with highest frequency:", max_char)
print("Frequency:", max_freq)






         
    
         


            











