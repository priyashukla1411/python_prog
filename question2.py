
# 2
# import sys
# print("User Current Version:-", sys.version)

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




# 66.Write a Python program to calculate body mass index.
# height = float(input("Input your height in Feet: "))
# weight = float(input("Input your weight in Kilogram: "))
# print("Your body mass index is: ", weight / (height/100)**2  )

# 69.Write a Python program to sort three integers without using conditional statements and loops.
# x = int(input("Input first number: "))
# y = int(input("Input second number: "))
# z = int(input("Input third number: "))
# a1 = min(x, y, z)
# a3 = max(x, y, z)
# a2 = (x + y + z) - a1 - a3     #(condition)
# print("Numbers in sorted order: ", a1, a2, a3)


# 72. Write a Python program to get the details of math module.
# # Imports the math module
# import math            
# #Sets everything to a list of math module
# math_ls = dir(math) # 
# print(math_ls)


# 73. Write a Python program to calculate midpoints of a line. 
# print('\nCalculate the midpoint of a line :')

# x1 = float(input('The value of x (the first endpoint) '))
# y1 = float(input('The value of y (the first endpoint) '))

# x2 = float(input('The value of x (the first endpoint) '))
# y2 = float(input('The value of y (the first endpoint) '))

# x_m_point = (x1 + x2)/2
# y_m_point = (y1 + y2)/2
# print();
# print("The midpoint of line is :")
# print( "The midpoint's x value is: ",x_m_point)
# print( "The midpoint's y value is: ",y_m_point)
# print();

# 75. Write a Python program to get the copyright information and write Copyright information in Python code.
# import sys
# print("\nPython Copyright Information")
# print(sys.copyright)
# print()

# 80. Write a Python program to get the current value of the recursion limit.
# import sys
# print()
# print("Current value of the recursion limit:")
# print(sys.getrecursionlimit())
# print()

# 81. Write a Python program to concatenate N strings.
# list_of_colors = ['Red', 'White', 'Black']  
# colors = '-'.join(list_of_colors)
# print()
# print("All Colors: ",colors)
# print()

# 82. Write a Python program to calculate the sum of all items of a container (tuple, list, set, dictionary)
# s = sum([10,20,30])
# print("\nSum of the container: ", s)
# print()

# 84. Write a Python program to count the number occurrence of a specific character in a string
# s = "The quick brown fox jumps over the lazy dog."  
# print("Original string:")
# print(s)
# print("Number of occurrence of 'o' in the said string:")
# print(s.count("o"))


# 86. Write a Python program to get the ASCII value of a character
# print()
# print(ord('a'))
# print(ord('A'))
# print(ord('1'))
# print(ord('@'))
# print()

# 88. Given variables x=30 and y=20, write a Python program to print "30+20=50". 
# x = 30
# y = 20
# print("\n%d+%d=%d" % (x, y, x+y))
# print()

# 89. Write a Python program to perform an action if a condition is true.
# Given a variable name, if the value is 1, display the string "First day of a Month!" and do nothing if the value is not equal.
# n=1
# if n == 1:
#    print("\nFirst day of a Month!")
# print()

# 91. Write a Python program to swap two variables.
# a = 30
# b = 20
# print("\nBefore swap a = %d and b = %d" %(a, b))
# a, b = b, a
# print("\nAfter swaping a = %d and b = %d" %(a, b))
# print()


# 92. Write a Python program to define a string containing special characters in various forms.
# print("\#{'}${\"}@/")
# print("\#{'}${"'"'"}@/")
# print("""\#{'}${"}@/""")
# print('\#{\'}${"}@/')
# print('\#{'"'"'}${"}@/')
# print('''\#{'}${"}@/''')

# 93. Write a Python program to get the Identity, Type, and Value of an object.
# x = "priya"
# print("\nIdentity: ",x)
# print("\nType: ",type(x))
# print("\nValue: ",id(x))


  
#94. Write a Python program to convert a byte string to a list of integers.
# x = b'GpG'              (Initializing a byte string as GpG)
# print(list(x))


# 95. Write a Python program to check whether a string is numeric     
# string = '123ayu456'
# print(string.isnumeric())
    
# string = '123456'
# print(string.isnumeric())


# 98. Write a Python program to get the system time. 
# import time
# print()
# print(time.ctime())
# print()

# 99. Write a Python program to clear the screen or terminal
# import.os
# os.system("cls")


# 100. Write a Python program to get the name of the host on which the routine is running.
# import socket
# host_name = socket.gethostname()
# print("Host name:", host_name)


# 103. Write a Python program to extract the filename from a given path.
# import os
# print()
# print(os.path.basename('/home/seasia/python_prog'))
# print()

# 104. Write a Python program to get the effective group id, effective user id, real group id, a list of supplemental group ids associated with the current process.
# import os
# print("\nEffective group id: ",os.getegid())
# print("Effective user id: ",os.geteuid())
# print("Real group id: ",os.getgid())
# print("List of supplemental group ids: ",os.getgroups())
# print()


# 105. Write a Python program to get the users environment
# import os
# print()
# print(os.environ)
# print()

# 107. Write a Python program to retrieve file properties.
# import os.path
# import time
# print('File         :', __file__)
# print('Access time  :', time.ctime(os.path.getatime(__file__)))
# print('Modified time:', time.ctime(os.path.getmtime(__file__)))
# print('Change time  :', time.ctime(os.path.getctime(__file__)))
# print('Size         :', os.path.getsize(__file__))


    # 109. Write a Python program to check if a number is positive, negative or zero.
    # num = float(input("Input a number: "))
    # if num > 0:
    #    print("It is positive number")
    # elif num == 0:
    #    print("It is Zero")
    # else:
    #    print("It is a negative num)
    


# 110. Write a Python program to get numbers divisible by fifteen from a list using an anonymous function.    
# num_list = [45, 55, 60, 37, 100, 105, 220]
# # use anonymous function to filter
# result = list(filter(lambda x: (x % 15 == 0), num_list))
# print("Numbers divisible by 15 are",result)


# 112. Write a Python program to remove the first item from a specified list
# color = ["Red", "Black", "Green", "White", "Orange"]
# print("Original list elements:")
# print(color)
# del color[0]
# print("After removing the first color:")
# print(color


# 114. Write a Python program to filter the positive numbers from a list
# nums = [34, 1, 0, -23, 12, -88]
# print("Original numbers in the list: ",nums)
# new_nums = list(filter(lambda x: x >0, nums))
# print("Positive numbers in the said list: ",new_nums)


# 115. Write a Python program to compute the product of a list of integers (without using for loop)
# from functools import reduce
# nums = [10, 20, 30,]
# print("Original list numbers:")
# print(nums)
# nums_product = reduce( (lambda x, y: x * y), nums)                   reduce(function, iterable, [, initializer])
# print("\nProduct of the said numbers (without using for loop):",nums_product)



# 116. Write a Python program to print Unicode characters.
# str = u'\u0050\u0052\u0049\u0059\u0041'                         (https://en.wikipedia.org/wiki/List_of_Unicode_characters)
# print()
# print(str)
# print()


# 117. Write a Python program to prove that two string variables of same value point same memory location.
# str1 = "Python"
# str2 = "Python"
# print("\nMemory location of str1 =", hex(id(str1)))
# print("Memory location of str2 =", hex(id(str2)))
# print()

# 118. Write a Python program to create a bytearray from a list.      
# nums = [10, 20, 56, 35, 17, 99]
# # Create bytearray from list of integers.
# values = bytearray(nums)
# for x in values: print(x)


# 119. Write a Python program to round a floating-point number to specified number decimal places
# order_amt = float(input("enter number: "))
# print('\nThe total order amount comes to %f' % order_amt)
# print('The total order amount comes to %.3f' % order_amt)
# print()

# 120. Write a Python program to format a specified string limiting the length of a string
# str_num = int(input("enter number: "))
# print("Original string:",str_num)
# print('%.6s' % str_num)
# print('%.9s' % str_num)
# print('%.10s' % str_num)

#122.Write a Python program to empty a variable without destroying it.
# d = {"x":200}
# l = [1,3,5]
# t= (5,7,8)
# print(type(d)())
# print(type(l)())
# print(type(t)())

# 123. Write a Python program to determine the largest and smallest integers, longs, floats. 
# import sys
# print("Float value information: ",sys.float_info)
# print("\nInteger value information: ",sys.int_info)
# print("\nMaximum size of an integer: ",sys.maxsize) 
        
        
# 124. Write a Python program to check whether multiple variables have the same value.
# p=int(input("enter number1: "))        
# q=int(input("enter number2: "))  
# s=int(input("enter number3: "))  
# if p==q==s:
#     print("values are equal")
# else:
#     print("values are not equal")    
            

#125. Write a Python program to sum of all counts in a collections
# import collections
# num = [2,2,4,6,6,8,6,10,4]
# print(sum(collections.Counter(num).values()))        >>[collections.Counter(num).values() ]     

# 128. Write a Python program to check whether lowercase letters exist in a string
# str1 = input("enter the user data: ")
# print(any(c.islower() for c in str1))


#129. Write a Python program to add leading zeroes to a string.
# str1=input("enter the number:")
# print("Original String: ",str1)
# str1 = str1.ljust(8, '0')
# print(str1)

#130. Write a Python program to use double quotes to display strings
# p=""" "hellooooo" """
# print(p)

# 132. Write a Python program to list home directory without absolute path
# import os.path
# print(os.path.expanduser('~'))

#134. Write a Python program to input two integers in a single line
# print("Input the value of x & y & z")
# x, y, z = map(int, input().split())
# print("The value of x & y &z are: ",x,y,z)

#135. Write a Python program to print a variable without spaces between values. 
# x = int(input("enter number: "))
# print('Value of x is',(x))

# d = {'Red': 'Green'}
# (c1, c2), = d.items()
# print(c1)
# print(c2)

# 137. Write a Python program to extract single key-value pair of a dictionary in variables
# p = {"Name": "Priya"}
# (c1, c2), = p.items()
# print(c1)
# print(c2)


# 138. Write a Python program to convert true to 1 and false to 0
# x = 'true'
# x = int(x == 'true')
# print(x)
# x = 'abcd'
# x = int(x == 'true')
# print(x)

# 141. Write a python program to convert decimal to hexadecimal
# x =  int(input("enter number: "))
# print(format(x, '02x'))

# 144. Write a Python program to check whether variable is integer or string. 
# print(isinstance(25,int) or isinstance(25,str))
# print(isinstance([25],int) or isinstance([25],str))
# print(isinstance("25",int) or isinstance("25",str))


# 145. Write a Python program to test if a variable is a list or tuple or a set.
# x = ('tuple', False, 3.2, 1)
# if type(x) is list:
#     print('x is a list')
# elif type(x) is set:
#     print('x is a set')
# elif type(x) is tuple:
#     print('x is a tuple')    
# else:
#     print('Neither a list or a set or a tuple.')

# 147. Write a Python function to check whether a number is divisible by another number. Accept two integers values form the user.
# def multiple(m, n):
#     	return True if m % n == 0 else False

# print(multiple(25, 5))
# print(multiple(13, 2))


# 149. Write a Python function that takes a positive integer and returns the sum of the cube of all the positive integers smaller than the specified number.
# def sum_of_cubes(n):
#      n -= 1
#  total = 0
#  while n > 0:
#    total += n * n * n
#    n -= 1
#  return total
# print("Sum of cubes smaller than the specified number: ",sum_of_cubes(3))



