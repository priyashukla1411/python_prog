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









