# i = int(input("mayank"))
# while i != 5 and i != 10:
#     print(i)
#     i = int(input("mayank"))


###################################


# def f(x):
#     print(a*x)

# a = int(input("1 :"))
# b = int(input("2 : "))
# f(b)


####################################


# def area(x, y):
#     a = x*y
#     print(a)

# l = int(input("1 : "))
# b = int(input("2 : "))

# area(l, b)


######################################


# def checkNum(i):
#     if(i%2 == 0):
#         print("even")
#     elif(i%2 != 0):
#         print("odd")

# inp = int(input("1: "))
# checkNum(inp)


#####################################


# def area(x,y):

#     a = x*y
#     return a

# l = int(input("l : "))
# b = int(input("b : "))

# ar = area(l,b)
# print(ar)


#########################################


# def prime(x):
#     for i in range(2, int(x**0.5)+1):
#         if x%i == 0:    
#             return False
#     return True
# a = int(input("inp : "))

# for i in range(2,(a+1)):
#     if prime(i):
#         print(i)


################# S.I ##########################


# cp = int(input("Enter the C.P : "))
# sp = int(input("Enter the S.P : "))

# pl = sp - cp

# if(pl>0):
#     print("Profit Amount = ",pl)
# elif(pl<0):
#   print("Loss Amount = ",cp - sp)


################ C.I ###########################


# p = int(input("Enter the depositing amount : "))
# r = int(input("Enter the rate : "))
# t = int(input("Enter the time : "))

# print("Amount = ", (p*r*t/100) )


# p = float(input("Enter the depositing amount : "))
# t = float(input("Enter the time : "))
# r = float(input("Enter the rate : "))
# a = p*(pow((1+r/100),t))
# print("C.I = ", a)


################ area of circle ###################


# r = int(input("Enter the radius : "))
# a = float(22/7*r*r)
# print("Area = ", a)


##################### BMI(overweight) ###################


# h = float(input("ENTER YOUR HEIGHT IN METERS : "))
# w = float(input("ENTER YOUR weight IN KILOGRAMS : "))
# print("BMI", round((w/(h*h)),2))


##################### No. of notes required##################


# print("Available denominations of notes are 2000,500,100,50 ")

# r = int(input("Enter Amount : "))

# print("You will need the following notes")

# tt = int(r/2000)
# ttr = r%2000

# fh = int(ttr/500)
# fhr = ttr%500

# oh = int(fhr/100)
# ohr = fhr%100

# f = int(ohr/50)
# fr = ohr%50

# if(tt>0):
#     print(tt,", 2000 rupees notes")
# if(fh>0):
#     print(fh,", 500 rupees notes")
# if(oh>0):
#     print(oh,", 100 rupees notes")
# if(f>0):
#     print(f,", 50 rupees notes")
# if(fr<=0):
#     print("Total No. of notes you will required = ", tt+fh+oh+f)
# if(fr>0):
#     print("Total No. of notes you will required = ", tt+fh+oh+f, "and more notes")


############## area of trapezoid ############

# h = int(input("Enter the height of traezium : "))
# b = int(input("Enter the height of bottom base : "))
# b1 = int(input("Enter the height of top base : "))

# a = ((b+b1)/2)*h

# print("Area of Trapezoid = ", a)


############## area of sector of circle ##########

# r = int(input("Enter the radius of circle : "))
# a = int(input("Enter the angle of the radii : "))

# ac = 22/7*r*r
# asc = (a/360)*ac

# print("Area of sector of circle = ", asc)


################ checking the triangle sides ##############


# def t(x,y,z):
#     if((x+y)>z and (y+z)>x and (x+z)>y):
#         print(x , y , z, " are the sides of triangle")
#     else:
#         print(x ,y , z, " are not the sides of ")

# ff = int(input("Enter the first side : "))
# fs = int(input("Enter the second side : "))
# ft = int(input("Enter the third side : "))

# t(ff,fs,ft)


################### checking prime #################

# def cp(x):
#     for i in range(2, int(x ** 0.5) + 1):
#         if x % i == 0:
#             return False
#     return True
#
# num = int(input("Enter the number : "))
#
# print(cp(num))


################### HCF and LCM ###############


# def hcf(x ,y):
#     if x>y :
#         return y-(x%y)

#     elif y>x :
#         return x-(y%x)

# i = int(input("Enter the number : "))
# o = int(input("Enter the number : "))

# def lcm(x , y):
#     return x*y / hcf(x,y)

# print(int(lcm(i,o)))


###################### table ##########################


# for i in range(1,11):
#     print("5 X ", i ," = ",(5*i))


##################### finding sqrt( Newton ) ###########################


# def sqrt(x):
#     left = 0
#     right = x
#     mid = (left + right) / 2
#     sq = mid ** 2
#     while abs(sq - x) > 0.00000000000000001:
#         if sq < x:
#             left = mid
#         elif sq > x:
#             right = mid
#         mid = (left + right) / 2
#         sq = mid ** 2
#     return mid
#
#
# num = int(input("Enter the Number = "))
#
# print(sqrt(num))


##################### Logarithm ###################


# def log(num,con):
#     left = 0
#     right = num
#     mid = (left + right) / 2
#     inter = con ** mid
#     while abs(inter - num) > 1e-100:
#         if inter < num:
#             left = mid
#         elif inter > num:
#             right = mid
#         mid = (left + right) / 2
#         inter = con ** mid
#     return mid
#
#
# print(log(81,3))
# print(log(1,2))


################ Armstrong ################


# def isArmstrong(num):
#     total = 0
#     org = num
#     c = 0
#     while num != 0:
#         num //= 10
#         c += 1
#     num = org
#     while num != 0:
#         digit = num % 10
#         num //= 10
#         total += digit ** c
#     return total == org
#
#
# # print(isArmstrong(371))
#
#
# def printArmstrongs(lower, upper):
#     for i in range(lower, upper + 1):
#         if isArmstrong(i):
#             print(i)
#
#
# x = int(input("Enter the Lower limit = "))
# y = int(input("Enter the Upper limit = "))
#
# printArmstrongs(x, y)



################ lambda functions ##########

# double = lambda x : 2*x
# print(double(5))


########## binary to decimal #########

# def btod(b):
#     org = b
#     num = 0
#     i = 0
#     r = 0
#     while b != 0:
#         r = b % 10
#         num += r*2**i
#         b //= 10
#         i += 1
#     return num
# x = int(input())
# print(btod(x))

########## find the ascii code #################


# print(ord('a') + 1)

################ check the char is lower or upper#############

# i = (input("Enter the char = "))

# if  i >= 'a' and i <= 'z':
#     print("Lower case")
# elif i >= 'A' and i <= 'Z':
#     print("Upper case")
# else:
#     print("Else case") 



##################################

# i = (input("Enter the char = "))

# if 'a' <= i <= 'z':
#     print("Lower case")
# elif 'A' <= i <= 'Z':
#     print("Upper case")
# else:
#     print("Else case") 


################ Store more than one variable #################


# funds = [100,50,50,10]
# print(funds)
# print(funds[1])


############### change the value array of particular index #######################


# m = [10,1,3,55,5,35,"",3]
# print(m)
# m[1] = 1000
# print(m)
# m[1:2] = [1000]
# print(m)


############### print the data by range ####################


# m = [3534535,"a",5353 , 545,334,51,2,4]
# print(m[:2])
# print(m[1:2:3])
# print(m[::-1]) #reverse the list
# print(m[-1:-9:-1])


############### built in methods ###################

# m = [2,35,34,6,456,6,56,45,56]
# m.append(30)  #add 30 at he end
# m.insert(0,30) #30 will be added at any positions depending on the input

# m.pop() #it removes the value by index
#         #clear the value
#         #if nothing value is given then it will by default delete the last value

# x = m.pop() #store the value of which has been removed by pop
# print(x)    #
# print(m)

# m.remove(56) #remove the value by value
# m.remove(56)
# print(m)

# x = m.count(56) #count the occurence of value
# print(x)

# x = m.index(56) #says index value of the value
# x = m.index(56,7) #search the value after index 6
# print(x)

# x = len(m) # says the no. value in list
# print(x)

# print(max(m)) #says the maximum value in the list
# print(sum(m)) #says the sum of all the no. of the lists

# print(m + [2,2,3])

# for i in range(0, len(m)):
    # print(m[i])

# for v in m:      # enhanced for-loop
    # print(v)


# for i,v in enumerate(m): # enumerate 
#     print(i,v)


# def total(lst):
#     result = 0
#     for i in lst:
#         result += i
#     return result

# print(total(m))

# def max(lst):
#     maximum = lst[0]
#     for v in lst:
#         if v > maximum:
#             maximum = v
#     return maximum

# print(max(m))


# def linearSearch(lst, val):
#     for i in range(0,len(lst)):
#         if lst[i] == val:
#             return i
#     return i 

# print(linearSearch(m,56))

# m = [5.25,44,65,65,6648,2]
# b = m
# print(id(m))
# print(id(b))

# c = list(m)
# print(id(c))

# e = m[:]
# print(id(e))

# # is compare the address

# print(m is b)
# print(m is c)
# print(c is b)


# result = []
# for i in range(1,6):
#     result.append(i**2)
# print(result)

#list comprehension
result = [x**2 for x in range(1,6)]
print(result)

result = [x**2 for x in range(1,6) if x > 1]
print(result)



############### Complexity #####################





















