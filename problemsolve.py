#  1.  reverse a list
# list=[1,2,3,4,5]
# ln=len(list)
# for i in range(ln, 0 ,-1):
#     print(i , end="    ")

# 2. reverse a list with the help of while 
# def reverse(list,s, e):
#     while s<e:
#         list[s], list[e]=list[e], list[s]
#         s+=1
#         e-=1
# list=[1,2,3,4,5]
# print(list)
# print("after reverse list")
# reverse(list,0,4)
# print(list)

#3.  count the number in the list
# num=int(input("enter the number "))
# count=0
# while(num>0):
#     count=count+1
#     num=num//10
    
# # print("the number is ",count )
# print("the number is ",num )

# 4. check if number is palindrome or not
# num=int(input(" please enter the number  "))
# temp=num
# rev=0
# while(num>0):
#     dig=num%10
#     rev=rev*10+dig
#     num=num//10
# if (temp==rev):
#     print("number is palindrome ", temp)
# else:
#     print("number is  not palindrome ", temp)

# 5. Reverse a Number 
# num=int(input(" please janu enter the number  "))
# temp=num
# rev=0
# while(num>0):
#     dig=num%10
#     rev=rev*10+dig
#     num=num//10
# print("your number is ", temp , "reverse number is ", rev)

# 6. print an identify matrix
# num=int(input(" sona enter number of rows  "))
# for i in range(0,num):
#     for j in range(0, num):
#         if (i==j):
#             print("1" , end="  ")
#         else:
#             print('0' , end="  ")
#     print()

# 7. convert celsius into farenhiet
# cel= int(input("enter the celcius "))
# f= (cel*1.8)+32
# print("celcius is ",cel , "farenhiet is ", f)

# 8. generate all the divisors of an integer
# num=int(input("lali enter number lali  "))
# for i in range(1, num):
#     if (num%i == 0):
#         print("number is ", i, end=" ")

# 9, find the sum of N natural numbers 
# n=int(input("enter the numbers ")) 
# temp=n
# sum1=0
# while(n>0):
#     sum1=sum1+n
#     n=n-1
# print("the sum of number is ", sum1 , "in ", temp)

# 10. find the second largest number in list
# list=[]
# n=int(input("enter the numbers  "))
# for i in range(0,n):
#     num=input("enter the numbers "+ str(i+1) + ":")
#     list.append(num)
# list.sort()
# print("the second largest number in list is", list[n-2])
#  with the help of function
# def second(list):
#     n=len(list)
#     list.sort() 
#     print("the second largest number is ", list[n-2] , "in ", list , end=" ")
# list1=[11,22,33,23]
# second(list1)

# 11. find the largest number in list
# def second(list):
#     n=len(list)
#     list.sort() 
#     print("the  largest number is ", list[n-1] , "in ", list)
# list1=[11,22,33,23, 25, 44,55]
# second(list1)

# 12. put even and odd element in list
# def search(list):
#     even=[]
#     odd=[]
#     n=len(list)
#     for i in range(0,n):
#         if i%2==0:
#             even.append(i) 
#         else:
#             odd.append(i)
#     print("the even list is ", even)
#     print("the odd list is ", odd)
    
# list1=[1,3,4,5,6,7,8,9,11,12,14,15,22,34,55,65,23,43,64]
# search(list1)

# 13. Merge two list and sort it
# def Merge(list1,list2):
#     list3=list1+list2
#     list3.sort()
#     print("the first list is ",list1)
#     print("the second list is ",list2)
#     print("after merging")
#     print("the sorted  list is ",list3)
# list1=[1,2,34,5,3,5,6,4]
# list2=[11,12,134,42,33,22,112]
# Merge(list1,list2)

# 14. sort the list according to the second element in a sublist
# def sort(list):
#     n=len(list)    
#     list.sort()
#     for i in range(0,n-1):
#         temp=list[i]
#         list[i]=list[i+1]
#         list[i+1]=temp
#     print("the list is ", list)

# ls=[2,3,4,5,1]
# print(len(ls))
# print(ls)
# print("after swapping ")
# sort(ls)

# 15. sort a list according to the length of the list
# def sort(list):
#     list.sort(key=len)
#     # n=len(list)
#     print("the sorted list is ", list)

# list=[1,2,322,23,4,5,6]
# print(list)
# print("after changing")
# sort(list)

# 16. find the union of two list
# def union(list,list1):
#     list.sort()
#     list1.sort()
#     list2=list+list1
#     list3=set(list2)
#     print("the sorted list is ", list3)
# list=[1,2,3,4,5]
# list1=[1,2,6,3,7]
# print(list)
# print(list1)
# print("after adding union is ")
# union(list,list1)

# next method

# def interse(a,b):
#     return list(set(a) | set(b))
# a=[1,2,4,5,6]
# b=[1,2,6,7,8,9]
# print(a, b , end=" ")
# print("intersection of two list")
# print(interse(a,b))


# 17. find the intersection of two list
# def interse(a,b):
#     return list(set(a) & set(b))
     
# a=[1,2,4,5,6]
# b=[1,2,6,7,8,9]
# print(a, b , end=" ")
# print("intersection of two list")
# print(interse(a,b))

#18. generate random number 
# import random
# print(random.randint(1,10)) 

# 19. sort a list of tuple in increasing order by the last element in each tuple
# def sort(tuple):
#     return sorted(tuple, )










    

    


    




