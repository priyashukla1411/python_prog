#3. Write a Python program to display the current date and time.
# import datetime
# x = datetime.datetime.now()
# print ("Current date and time : ")
# print (x.strftime("%Y-%m-%d %H:%M:%S"))  # strftime(formating)


#4. Write a Python program which accepts the radius of a circle from the user and compute the area. 
# a = float(input ("enter the the radius =  "))
# p = 3.14*(a*a)
# print("area of circle = ", p)

#  Write a Python program which accepts a sequence of comma-separated numbers from user and generate a list and a tuple with those numbers
# number = input("user input numbers : ")
# list = number.split(",")
# tuple = tuple(list)
# print('List : ',list)
# print('Tuple : ',tuple)

#  7. Write a Python program to accept a filename from the user and print the extension of that
# filename= input("Enter Filename: ")
# f = filename.split(".")
# print ("Extension of the file is : ", f[-1])
 
 
 
# 8. Write a Python program to display the first and last colors from the following list.
# colour = input ("Enetr colors name= ")
# f = colour.split(",")
# c= (f[0], f[-1])
# print(c)
 

# 9. Write a Python program to display the examination schedule. (extract the date from exam_st_date).
# schedule = input("enter student schedule : ")
# f = "/".join(schedule)
# print(schedule)
# print(f)
 
 
 # 10. Write a Python program that accepts an integer (n) and computes the value of n+nn+nnn
# a = int(input("Input an integer : "))
# n1 = int( "%d" % a )
# n2 = int( "%d%d" % (a,a) )
# n3 = int( "%d%d%d" % (a,a,a) )
# print (n1+n2+n3)

#  12. Write a Python program to print the calendar of a given month and year.
# import calendar 
# y = int(input ("enter year = "))
# m = int(input("enter month = "))
# print(calendar.month(y,m))


# 14. Write a Python program to calculate number of days between two dates.
# from datetime import datetime
# first_year= str(input('Enter date(yyyy-mm-dd): '))
# my_date1 = datetime.strptime(first_year, "%Y-%m-%d")
# print(my_date1)
# last_year = str(input('Enter date(yyyy-mm-dd): '))
# my_date2 = datetime.strptime(last_year, "%Y-%m-%d")
# print(my_date2)

# delta = my_date2 - my_date1
# print(delta.days)

# 15. Write a Python program to get the volume of a sphere with radius 6.

# num= int(input("enter the radius = "))
# V=4/3*(3.14*num*3)
# print(V)

#  16. Write a Python program to get the difference between a given number and 17, if the number is greater than 17 return double the absolute difference
# def difference(n):
#     if n <= 17:
#         return 17 - n
#     else:
#         return (n - 17) * 2 

# print(difference(18))

# 18. calculate the sum of three given numbers, if the values are equal then return thrice of their sum.
# def num(x, y, z):
    
#      sum = x + y + z
  
#      if x == y == z:
#       sum = sum * 3
#      return sum

# print(num(2, 2, 2))    #  three numbers are equal
# print(num(1, 2, 3))    # three numers are not equal

#21. Write a Python program to find whether a given number (accept from the user) is even or odd, print out an appropriate message to the user. 
# num = int(input("Enter a number: "))
# mod = num % 2
# if mod > 0:
#     print("This is an odd number.")
# else:
#     print("This is an even number.")#

# 22. Write a Python program to count the number 4 in a given list.   
# def count(lst, x):
#     count = 0
#     for num in lst:
#         if (num == x):
#             count = count + 1
#     return count
# lst = [4,7,7,4,9,4,7,4]
# x = 4
# print('{} has occurred {} times'.format(x, count(lst, x)))


# 24. Write a Python program to test whether a passed letter is a vowel or not.
# def is_vowel(char):
#     all_vowels = 'aeiou'
#     return char in all_vowels
# print(is_vowel('p'))
# print(is_vowel('e'))


#25. Write a Python program to check whether a specified value is contained in a group of values.
# def is_group_member(group_data, n):
#         for value in group_data:
#             if n == value:
#                 return True
#         return False
# print(is_group_member([1, 5, 8, 3], 3))
# print(is_group_member([5, 8, 3], -1))

#27. Write a Python program to concatenate all elements in a list into a string and return i
# list = ['1','2','3','4'] 
# newlist = ""
# a = newlist.join(list) 
# print(a) 


# 28. Write a Python program to print all even numbers from a given numbers list in the same order and stop the printing if any numbers that come after 237 in the sequence. Go to the editor
# Sample numbers list :

# numbers = [    
#     386, 462, 47, 418, 907, 344, 236, 375, 823, 566, 597, 978, 328, 615, 953, 345, 
#     399, 162, 758, 219, 918, 237, 412, 566, 826, 248, 866, 950, 626, 949, 687, 217, 
#     815, 67, 104, 58, 512, 24, 892, 894, 767, 553, 81, 379, 843, 831, 445, 742, 717, 
#     958,743, 527
#     ]
# num = [    
#     386, 462, 47, 418, 907, 344, 236, 375, 823, 566, 597, 978, 328, 615, 953, 345, 
#     399, 162, 758, 219, 918, 237, 412, 566, 826, 248, 866, 950, 626, 949, 687, 217, 
#     815, 67, 104, 58, 512, 24, 892, 894, 767, 553, 81, 379, 843, 831, 445, 742, 717, 
#     958,743, 527
#     ]
# for x in num:
#     if x == 237:
#         print(x)
#         break;
#     elif x % 2 == 0:
#         print(x)


# 29. Write a Python program to print out a set containing all the colors from color_list_1 which are not present in color_list_2. Go to the editor
# Test Data :
# color_list_1 = set(["White", "Black", "Red"])
# color_list_2 = set(["Red", "Green"])
# color_list_1 = set(["White", "Black", "Red"])
# color_list_2 = set(["Red", "Green"])
# print("Original set elements:")
# print(color_list_1)
# print(color_list_2)
# print("Differenct of color_list_1 and color_list_2:")
# print(color_list_1 - color_list_2)

#30. Write a Python program that will accept the base and height of a triangle and compute the area.
# b = int(input("Input the base : "))
# h = int(input("Input the height : "))
# area = b*h/2
# print("Area of Triangle= ", area)

# 31. Write a Python program to compute the greatest common divisor (GCD) of two positive integers. 
# import math
# a= int(input("Enter first number = "))
# b= int(input("Enter second number = "))
# print("The gcd of 336 and 360 is : ", end="")
# print(math.gcd(a,b))

# 32. Write a Python program to get the least common multiple (LCM) of two positive integers.
# a=int(input("enter first"))
# b=int(input("enter second"))
# maxnum=max(a,b)
# while(True):
#     if (maxnum % a == 0 and maxnum % b ==0):
#         break
#     maxnum+=1
# print(maxnum)

# 33. Write a Python program to sum of three given integers. However, if two values are equal sum will be zero.
# def sum_three(x, y, z):
#     if x == y or y == z or x==z:
#         sum = 0
#     else:
#         sum = x + y + z
#     return sum
# print(sum_three(2, 1, 2))
# print(sum_three(3, 2,5 ))


# 34. Write a Python program to sum of two given integers. However, if the sum is between 15 to 20 it will return 20.
# def sum(x, y):
#     sum = x + y
#     if sum in range(15, 20):
#         return 20
#     else:
#         return sum

# print(sum(10, 6))
# print(sum(10, 2))
# print(sum(10, 12))


# 35. Write a Python program that will return true if the two given integer values are equal or their sum or difference is 5
# def test_number5(x, y):
#        if x == y or abs(x-y) == 5 or (x+y) == 5:
#        return True
#    else:
#        return False
# print(test_number5(7, 2))
# print(test_number5(2, 2))
# print(test_number5(7, 3))


#36. Write a Python program to add two objects if both objects are an integer type
# def add_numbers(a, b):
#          if not (isinstance(a, int) and isinstance(b, int)):
#             return "Inputs must be integers!"
#         return a + b
# print(add_numbers(10, 20))
# print(add_numbers(10, 20.23))
# print(add_numbers('5', 6))
# print(add_numbers('5', '6'))


#37. Write a Python program to display your details like name, age, address in three different lines.
# name= input("user input name= ")
# address = input("user input address= ")
# age= int(input("user input address= "))
# print("Name: {}\nAge: {}\nAddress: {}".format(name, age, address))

# 38. Write a Python program to solve (x + y) * (x + y).
# x= int(input("USER INPUT VALUE1: "))
# y= int(input("USER INPUT VALUE2: "))
# result = x * x + 2 * x * y + y * y
# print(result)


# 39. Write a Python program to compute the future value of a specified principal amount, rate of interest, and a number of years.  
# p= 1200   # principle amount
# t= 2      # time
# r= 5.4    # rate
# # calculates the compound interest
# a=p*(1+(r/100))**t  # formula for calculating amount
# ci=a-p  # compound interest = amount - principal amount
# print(ci)

# 40. Write a Python program to compute the distance between the points (x1, y1) and (x2, y2).

# x1=int(input("enter x1 : "))
# x2=int(input("enter x2 : "))
# y1=int(input("enter y1 : "))
# y2=int(input("enter y2 : "))
# result= ((((x2 - x1 )**2) + ((y2-y1)**2) )**0.5)
# print("distance between",(x1,x2),"and",(y1,y2),"is : ",result)

# 48. Write a Python program to parse a string to Float or Integer
# n = "246.2458"
# print(float(n))
# print(int(float(n)))

# 50. Write a Python program to print without newline or space.
# for i in range(0, 10):
#     print('*', end="")
# print("\n")

# 54. Write a Python program to get the current username
# getlogin() method of OS library is used to get the current username.
# # importing os module
# import os
# # using getlogin() returning username
# p=os.getlogin()
# print(p)

# 58. Write a Python program to sum of the first n positive integers

# n = int(input("Input a number: "))
# sum_num = (n * (n + 1)) / 2
# print("Sum of the first", n ,"positive integers:", sum_num)

# 59. Write a Python program to convert height (in feet and inches) to centimeters.
# print("Input your height: ")
# h_ft = int(input("Feet: "))
# h_inch = int(input("Inches: "))

# h_inch += h_ft * 12
# h_cm = round(h_inch * 2.54, 1)

# print("Your height is : %d cm." % h_cm)


# 60. Write a Python program to calculate the hypotenuse of a right angled triangle.
# from math import sqrt
# print("Input lengths of shorter triangle sides:")
# a = float(input("a: "))
# b = float(input("b: "))
# c = sqrt(a**2 + b**2)
# print("The length of the hypotenuse is:", c )

# 61. Write a Python program to convert the distance (in feet) to inches, yards, and miles. 
# feet = int(input("Input distance in feet: "))
# d_inches = d_ft * 12
# d_yards = d_ft / 3.0
# d_miles = d_ft / 5280.0
# print( d_inches)
# print(d_yards)
# print( d_miles)


# 62. Write a Python program to convert all units of time into seconds. 
# days = int(input("Input days: ")) * 3600 * 24
# hours = int(input("Input hours: ")) * 3600
# minutes = int(input("Input minutes: ")) * 60
# seconds = int(input("Input seconds: "))

# time = days + hours + minutes + seconds

# print("The  amounts of seconds", time)









