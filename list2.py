#  Find the frequency of each element
# numbers = [10, 20, 10, 30, 20, 10]
# freq={}
# for num in numbers:
#     if num in freq:
#         freq[num] +=1
#     else:
#         freq[num]=1
# for key, value in freq.items():
#     print(f"{key} appears {value} times in the given list ")



# Find missing number from 1 to N
# nums=[1,2,3,5,6]
# n=6
# expected_sum=n*(n+1)//2
# actual_sum=sum(nums)
# missing=expected_sum - actual_sum
# print("missing number is:", missing)



# Find duplicates in array
numbers=[10, 20, 10, 30, 20,10]
duplicate={}
for num in numbers:
    if num in duplicate:
        duplicate[num]+=1
    else:
        duplicate[num]=1
for key, value in duplicate.items():
    if value>1:
     print(f"{key} is duplicate, (appears {value} times)")

# Count pairs with a given sum (Brute + Optimized using Hashing)
a=[1,5,7,-1,5]
k=6
count=0
for i in range(len(a)):
   for j in range(i+1, len(a)):
      if a[i]+a[j]==k:
         count+=1
print("total pairs with sum", k,":",count)


a=[1,5,7,-1,5]
k=6
count=0
freq={}
for num in a:
   complement = k-num
   if complement in freq:
      count += freq[complement]
   if num in freq:
         freq[num]+=1
   else:
         freq[num]=1
print("total pairs with sum",k,":",count)

# Move all 0s to the end
arr=[0,1,0,3,12]
result=[]
for num in arr:
    if num !=0:
        result.append(num)
zeros=len(arr)-len(result)    
result +=[0] * zeros    
print("after moving 0s:",result)


# Remove duplicates from array
# unsorted array
arr=[4,2,2,4,3]
unique=list(set(arr))
print("after removing duplicate :", unique)

# sorted array 
arr=[1,2,2,3,3,3,4]
result=[]
for i in range(len(arr)):
    if i==0 or arr[i] !=arr[i-1]:
        result.append(arr[i])
print("",result)

# left rotate
arr=[1,2,3,4]
arr=arr[1:] +arr[:1]
print("left rotate by 1: ",arr)