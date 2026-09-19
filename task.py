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

# nums = [3,5,7,8,9,10]
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
# s = input("Enter a string: ")

# freq = {}

# for ch in s:
#     if ch in freq:
#         freq[ch] += 1
#     else:
#         freq[ch] = 1

# max_char = ""
# max_freq = 0

# for ch in freq:
#     if freq[ch] > max_freq:
#         max_freq = freq[ch]
#         max_char = ch

# print("Character with highest frequency:", max_char)
# print("Frequency:", max_freq)

# a=int(input("enter the number a: "))
# b=int(input("enter the number b: "))
# i=1
# maximum=1
# if a>b:
#     smallest=b
# else:
#     smallest=a
# while i<=smallest:
#     if a%i==0 and b%i==0:
#         maximum=max(maximum,i)
#     i=i+1
# print(maximum) 
# a=int(input("Enter the digit: "))
# i=1
# sum=0
# while i<a:
#     if a%i==0:
#         sum=sum+i
#     i=i+1
# if sum==a:
#     print(" it is a perfect number")
# else:
#     print(" it is not a perfect number")     


        
# def max_product(nums):
#     maxproduct=1
#     for i in range(0,len(nums)):
#       for j in range(i+1,len(nums)):
#         product=nums[i]*nums[j]
#         maxproduct=max(maxproduct,product)
#     print(maxproduct)   
# nums=[2,3,10,5,9,20]
# print(max_product(nums))
# a=0
# b=1
# n=int(input("How many digits you want: "))
# i=1
# fibonaci=[0,1]
# while i<=n:
#     newnumber=a+b
#     fibonaci.append(newnumber)
#     a=b
#     b=newnumber
#     i=i+1

# print(fibonaci)


# nums = [16,17,4,3,5,2]

# max_so_far = nums[-1]
# leaders = [max_so_far]

# for i in range(len(nums)-2, -1, -1):

#     if nums[i] > max_so_far:

#         leaders.append(nums[i])
#         max_so_far = nums[i]

# leaders.reverse()

# print(leaders)
# n=int(input("enter the number: "))
# temp=n
# digit=0
# max_num = 0
# while temp>0:
#     digit+=1
#     temp=temp//10

# for i in range(digit):
    

#     left = n // (10 ** (digit - i))
#     right = n % (10 ** (digit - i-1))

#     new_num = left * (10 ** (digit - i - 1)) + right

#     if new_num > max_num:
#         max_num = new_num

# print(max_num)

# num = input("Enter number: ")

# max_num = 0

# for i in range(len(num)):

#     new_num = num[:i] + num[i+1:]

#     if int(new_num) > max_num:
#         max_num = int(new_num)

# print(max_num)
# sentence=input("enter the sentence: ")
# words=sentence.split()
# for word in words:
#     rev=""
#     for ch in word:
#         rev=ch+rev
#     print(rev,end=" ")    
# n=int(input("enter the number: "))
# adddigit=int(input("enter the digit you want to add to get maximum: "))
# temp=n
# count=0
# max_num=0
# while temp>0:
#     temp=temp//10
#     count=count+1
# for i in range(0,count):
#     left=n//(10**(count-i))
#     right=n%(10**(count-i))
#     new_num=left*(10**(count+1-i))+adddigit*(10**(count-i))+right
#     if new_num>max_num:
#         max_num=new_num
# print(max_num)
# def is_prime(n):

#     if n < 2:
#         return False

#     for i in range(2, int(n ** 0.5) + 1):

#         if n % i == 0:
#             return False

#     return True


# def nearest_prime(num):

#     distance = 0

#     while True:

#         distance += 1

#         left = num - distance
#         right = num + distance

#         if is_prime(left):
#             return left

#         if is_prime(right):
#             return right


# num = int(input("Enter a number: "))

# print("Nearest prime =", nearest_prime(num))
# num = input("Enter number: ")
# max_num = 0
# for digit in num:
#     if int(digit) % 2 == 0:

#         remaining = list(num)
#         remaining.remove(digit)

#         remaining.sort(reverse=True)

#         new_num = ""

#         for d in remaining:
#             new_num += d

#         new_num += digit

#         if int(new_num) > max_num:
#             max_num = int(new_num)

# print(max_num)
# n=int(input("enter the number: "))
# temp=n
# digits=0
# sum=0
# while temp>0:
#     temp=temp//10
#     digits+=1
# i=1   
# while n>0:
#     d=n%10
#     n=n//10
#     sum=sum+d*10**(digits-i)
#     i=i+1
# print(sum)
# n=int(input("enter the number u want:") )
# i=1
# while i<=n:
#     j=1
#     while j<=i:
#         print(j,end="")
#         j=j+1
#     print()    
#     i=i+1



# L1 = [4,3,3,5,6,7,3]
# L2 = [2,3,4,6,7,9,11,3]
# L3 = [3,9,11,13,2,3,4,6,5]

# result = []

# for num in L1:

#     if num in L2 and num in L3:

#         result.append(num)

#         L2.remove(num)
#         L3.remove(num)

# print(result)

# numbers = [4,3,3,3,5,7,6]
# newlist = []
# while len(numbers)>0:

#     minimum = numbers[0]

#     for num in numbers:
#         if num < minimum:
#             minimum = num

#     newlist.append(minimum)
#     numbers.remove(minimum)

# print(newlist)
# num = int(input("Enter a number: "))

# for start in range(1, num):

#     total = 0
#     expression = ""

#     for current in range(start, num):

#         total += current

#         if expression == "":
#             expression = str(current)
#         else:
#             expression = expression + "+" + str(current)

#         if total == num:
#             print(expression)
#             break

#         if total > num:
#             break


# n=int(input("enter the number: "))
# c=int(input("closest multiple of: "))
# difference=0
# while True:
    
#     left=n-difference

#     right=n+difference

#     if left%c==0:
#         print(left)
#         break
#     elif right%c==0:
#         print(right) 
#         break
#     else:
#         difference=difference+1
# n=int(input("enter number of lines: "))


# for i in range(1,n+1):
#     j=1
#     while j<=i:

#         print(j,end="")

#         j=j+1
#     print()

# n=int(input("enter the number: "))
# sum1=0
# sum2=0
# count=0
# temp=n
# i=1
# while n>0:

#     d=n%10
#     n=n//10
#     if i%2==1:
#         sum1=sum1+d
        
#     elif i%2==0:
#         sum2=sum2+d
#     i=i+1    
# if sum1==sum2:
        
#         print("it is divisible by 11") 
# else:
#      print("not divisible by 11")
# n=int(input("enter the value of n: "))
# i=1
# maximum=0
# c=0
# sum=0
# while i<=n:
#     sum=sum+i
#     c=c+1
#     if sum%2==0:
#         if c>maximum:
#             maximum=c
#     i=i+1        
# print(maximum)

# n=int(input("enter the value of n: "))
# i=1
# while i<=n:
#     j=1
#     while j<=i:
#         print("*",end="")
#         j+=1
#     print()    
#     i=i+1
# y=n-1    
# while y>0:
#     j=1
#     while j<=y:
#         print("*",end="")
#         j=j+1
#     print()
#     y=y-1

# a=int(input("enter the number of digit number u want: "))
# for n in range(10**(a-1),10**(a)):
#     temp=n
#     if temp%3==0:
#         if temp%9!=0:
#             print(n)
#             break

# n=int(input("enter the number: "))
# temp=n
# count=0
# sum=0
# e=0
# while n>0:
#     n=n//10
#     count=count+1
# n=temp    
# while temp>0:
#     d=temp%10
#     temp=temp//10
#     sum=sum+d**(count-e)
#     e=e+1
# if sum==n:
#     print("discarium")
# else:
#     print("not discarium")       

n=int(input())
print(n&"s")

    



 


     




