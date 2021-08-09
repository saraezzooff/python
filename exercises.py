#########################
####   Math           ###
#########################
######################
### Problem        ###
######################
#https://edabit.com/challenge/v5gc8FQkDEepkqpfp (Power Calculator)

# def circuit_power(voltage, current):
#     return voltage * current
# 
# print(circuit_power(230, 10))
# print(circuit_power(110, 3))
# print(circuit_power(480, 20))
######################
### Problem        ###
######################
#https://edabit.com/challenge/QzXtDnSZL6y4ZcEvT (Farm problem)

# def animals(chickens, cows, pigs):
#     total_legs = (chickens * 2) + (cows * 4) + (pigs * 4)
#     return total_legs
# 
# print(animals(2, 3, 5))
# print(animals(1, 2, 3))
# print(animals(5, 2, 8))

######################
### Problem        ###
######################
#https://edabit.com/challenge/gwqqc5p3oiFXRJAQm

# def football_points(wins, draws, losses):
#     total_points = (wins * 3) +(draws * 1) +(losses * 0)
#     return total_points
# 
# print(football_points(3, 4, 2))
# print(football_points(5, 0, 2))
# print(football_points(0, 0, 1))

######################
### Problem # 3    ###
######################
#https://edabit.com/challenge/EPS5tFxKQB7vWXLs6
#Create a function that calculates the area of a rectangle. If the arguments are invalid, your function must return -1.
# def area(l, w):
#     if l > 0 and w > 0:
#         return (l*w)
#     else:
#         return -1
#     
# print(area(3, 4))
# print(area(10, 11))
# print(area(-1, 5))
# print(area(0, 2))

######################
### Problem # 4    ###
######################
#Create a function that takes the age in years and returns the age in days.
# def calcAge(age):
#     return age * 365
# 
# print(calcAge(65))
# print(calcAge(0))
# print(calcAge(20))
# 
#######################
### Problem # 4    ###
######################
#https://edabit.com/challenge/rZToTkR5eB9Zn4zLh (Return the Sum of Two Numbers)
# Create a function that takes two numbers as arguments and return their sum.
#def addition(num1,num2):
    #return num1+num2
    #return sum((num1,num2))

# print(addition(3, 2))
# print(addition(-3, -6))
# print(addition(7, 3))
#
#######################
### Problem # 5     ###
#######################
#https://edabit.com/challenge/XnJ24rWW7iJkNrtsh
#Create a function that takes length and width and finds the perimeter of a rectangle.
# def findPerimeter(l,w):
#     return 2 * (l+w)
# 
# print(findPerimeter(6, 7))
# print(findPerimeter(20, 10))
# print(findPerimeter(2, 9))

#######################
### Problem # 6     ###
#######################
#Create a function that takes a number n and returns the nth even number.
# def nthEven(n):
#     x = (n-1) * 2
#     if x % 2 == 0:
#         return x
#     else:
#         return x-1
#     
# print(nthEven(1))
# print(nthEven(2))
# print(nthEven(100))
#

#######################
### Problem # 7     ###
#######################
#https://edabit.com/challenge/9mKB2XJJ9gYgjms4Z
#Given a list of integers, determine whether the sum of its elements is even or odd.
#If the input list is empty, consider it as a list with a zero ([0]).
# def even_or_odd(mylist):
#     sum = 0
#     for n in mylist:
#         sum += n
#     if sum % 2 == 0:
#         return "even"
#     else:
#         return "odd"
# 
# print(even_or_odd([0]))
# print(even_or_odd([1]))
# print(even_or_odd([]))
# print(even_or_odd([0, 1, 5]))


#######################
### Problem         ###
#######################
#https://edabit.com/challenge/yfooETHj3sHoHTJsv (Are the Numbers Equal?)
# def is_same_num(num1, num2):
#     return num1 == num2
# print(is_same_num(4, 8))
# print(is_same_num(2, 2))
# print(is_same_num(2, "2"))


######################
### Problem        ###
######################
#https://edabit.com/challenge/KjCS7occ9hfu5snpb (Return the Next Number from the Integer Passed)
# def addition(num):
#     return num + 1
# print(addition(0))
# print(addition(9))
# print(addition(-3))

######################
### Problem        ###
######################
#https://edabit.com/challenge/8q54MKnRrm89pSLmW
#Convert Minutes into Seconds ,Write a function that takes an integer minutes and converts it to seconds.
# def convert(minutes):
#     return minutes * 60
# print(convert(5))
# print(convert(3))
# print(convert(2))

# ######################
# ###  lists        ####
######################
######################
### Problem # 1    ###
######################

#https://edabit.com/challenge/hEQ3rBrKrztQK8qAd
# 
# def get_first_value(mylist):
#     for num in mylist:
#         if mylist.index(num) == 0 :
#             return num
# 
# print(get_first_value([1, 2, 3]))
# print(get_first_value([80, 5, 100]))
# print(get_first_value([-500, 0, 50]))


######################
### Problem # 2   ###
######################

# def findLargestNum(mylist):
#     return max(mylist)
# 
# print(findLargestNum([4, 5, 1, 3]))
# print(findLargestNum([300, 200, 600, 150]) )
# print(findLargestNum([1000, 1001, 857, 1]))

######################
### Problem # 3    ###
######################
#https://edabit.com/challenge/ecSZ5kDBwCD3ctjE6


# def find_smallest_num(mylist):
#     return min(mylist)
# 
# print(find_smallest_num([34, 15, 88, 2]))
# print(find_smallest_num([34, -345, -1, 100]))
# print(find_smallest_num([-76, 1.345, 1, 0]))
# print(find_smallest_num([0.4356, 0.8795, 0.5435, -0.9999]))
# print(find_smallest_num([7, 7, 7]))



#####################
###   Strings     ###
#####################
######################
### Problem        ###
######################
#https://edabit.com/challenge/YN9mNNc4mMPDxyhFf   (Basic Variable Assignment)
# def name_string(name):
# 	  b = "Edabit"
# 	  result = name + b
# 	  return result
# print(name_string("Mubashir"))

#####################
### problem       ###
#####################
#https://edabit.com/challenge/pFQPcaaASgHuACbaS

# def concat_name(str1, str2):
#     return str2 + ", "+ str1
# 
# print(concat_name("First", "Last"))
# print(concat_name("John", "Doe"))
# print(concat_name("Mary", "Jane"))

#####################
### problem       ###
#####################
#https://edabit.com/challenge/gt9LLufDCMHKMioh2  (Stuttering Function)
# def stutter(word):
#      return word[0:2]+'... '+word[0:2]+'... '+ word+ '?'
# print(stutter("incredible"))

#####################
### problem       ###
#####################
#https://edabit.com/challenge/Ggq8GtYPeHJQg4v7q
# def replace_vowels(txt, ch):
#     vowels = ['a', 'i', 'e', 'o', 'u']
#     str = ''
#     for ltr in txt:
#         if ltr in vowels:
#             str += ch        
#         else:
#             str += ltr
#     return str
# print(replace_vowels("the aardvark", "#"))
# print(replace_vowels("minnie mouse", "?"))
# print(replace_vowels("shakespeare", "*"))
# print(replace_vowels("all is fair in love and war", "<"))


#####################
### problem       ###
#####################
def card_hide(card):
    
    return '*' * 5
#    print(card[:-4])
#    return '*'*len(card[:-4])+card[-4:]


#     i = -1
#     card2 = ''
#     while i < len(card) -1:
#         if i in range( len(card) - 5 , len(card)-1) :
#             i += 1
#             card2 += card[i]
#         else:
#             card2 += '*'
#             i += 1
#     return card2
print(card_hide("1234123456785678"))
#print(card_hide("8754456321113213"))
#print(card_hide("35123413355523"))
    
    
    
    
    
    
    
    
    
    
    
