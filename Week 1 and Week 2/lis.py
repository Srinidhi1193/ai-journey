""" Accept a list of numbers.
Use a for loop.
Calculate the total without using sum().
Return the total.
Take the list from the user. You can directly define a sample list for now if you prefer.
Print the returned result. """

def sum_list(nums):
    tot = 0
    for num in nums:
        tot += num
    return tot
""" 
l = int(input("Enter the length of the list: "))
nums = []
for i in range(l):
    e = int(input("Enter the num to add: "))
    nums.append(e) """

nums = [10,20,30,40,50]
print(sum_list(nums))


""" Accept a list of numbers.
Use a for loop.
Do not use max().
Return the largest number.
Take the list from the user.
Print the returned result. """

def max_list(nums):
    lar = nums[0]
    for num in nums:
        if num > lar:
            lar = num
    return lar
nums = [10,20,30,40,50]
print(max_list(nums))

""" Accept a list of numbers.
Use a for loop.
Count how many numbers are even.
Return the count.
Do not use filter() or other built-in shortcuts. """

def even_count(nums):
    even = 0
    for num in nums:
        if num % 2 == 0:
            even += 1
    return even
nums = [10,20,30,41,50]
print(even_count(nums))

""" Accept a list of numbers.
Return a new list containing only unique values.
Maintain the original order.
Use a for loop.
Do not use set(). """

def rem_dup(nums):
    new = []
    for num in nums:
        if num not in new:
            new.append(num)
    return new
nums = [10,10,30,41,41,50]
print(rem_dup(nums))

""" Accept a list of numbers.
Return the second largest unique number.
Use a for loop.
Do not use sort(), sorted(), or max(). """

def sec_lar(nums):
    lar = float("-inf")
    sec = float("-inf")
    for num in nums:
        if num > lar:
            sec = lar
            lar = num
        elif num > sec and num < lar:
            sec = num
    return sec 
nums = [-10,-10,-30,-41,-41,-50]
print(sec_lar(nums))

""" numbers = [10, 20, 30, 40]
Insert 25 between 20 and 30 using insert(). """

numbers = [10, 20, 30, 40]
numbers.insert(2,25)
print(numbers)

def non_dup(nums):
    new = []
    for num in nums:
        if nums.count(num) == 1:
            new.append(num)
    return new
nums = [10,10,30,41,10,41,50]
print(non_dup(nums))

""" matrix = [
    [10, 20, 30],
    [40, 50, 60],
    [70, 80, 90]
]
find sum """

def find_sum(matrix):
    total = 0
    for row in matrix:
        for num in row:
            total += num
    return total
matrix = [
    [10, 20, 30],
    [40, 50, 60],
    [70, 80, 90]
]
print(find_sum(matrix))

""" matrix = [
    [10, 20, 30],
    [40, 50, 60],
    [70, 80, 90]
]. find row sums. """

def row_sum(matrix):
    tot = []
    for row in matrix:
        s=0
        for num in row:
            s += num
        tot.append(s)
    return tot
matrix = [
    [10, 20, 30],
    [40, 50, 60],
    [70, 80, 90]
]
print(row_sum(matrix))

""" a = [10, 20, 30, 40, 50]
b = [20, 40, 60, 80]
Find common elements """

def com_ele(nums1, nums2):
    cmn = []
    for i in nums1:
        for j in nums2:
            if i == j:
                cmn.append(i)
    return cmn
a = [10, 20, 30, 40, 50]
b = [20, 40, 60, 80]
print(com_ele(a, b))

""" numbers = [2, 4, 3, 5, 7, 8]
target = 10 """

def targ_check(nums, tar):
    pairs =[]
    for i in range(len(nums)):
        for j in range(i+1,len(nums)):
            if nums[i] + nums[j] == tar:
                pairs.append((nums[i],nums[j]))
    return pairs
nums = [2, 4, 3, 5, 7, 8]
target = 10
print(targ_check(nums, target))

""" Given:

numbers = [10, 15, 20, 25, 30, 35, 40]
Create:
process_numbers(numbers)
Requirements:
Loop through the list.
If the number is even, check whether it is greater than 25.
If greater than 25, add it to an even_large list.
Otherwise, add it to an even_small list.
Ignore odd numbers.
Return both lists. """

def process_numbers(numbers):
    even_large = []
    even_small = []
    for num in numbers:
        if num % 2 == 0:
            if num > 25:
                even_large.append(num)
            else:
                even_small.append(num)
    return even_large,even_small

numbers = [10, 15, 20, 25, 30, 35, 40]
print(process_numbers(numbers))










