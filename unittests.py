
# ------------------------------------------------ #
'''sum_of_two_names'''

# Define a function named sum_of_two_nums, which takes in two numbers and returns the sum of those numbers.



### YOUR CODE STARTS HERE ###

def sum_of_two_nums(num1, num2):
  return num1 + num2
print(sum_of_two_nums(1, 17))

### YOUR CODE ENDS HERE ###


# ------------------------------------------------ #
'''greater_than_ten'''

# Define a function named greater_than_ten, which takes in an integer and returns True if the number is greater than 10 and False if the number is less than 10.


### YOUR CODE STARTS HERE ###

def greater_than_ten(num):
  if num > 10 :
    return True
  else:
    return False
print(greater_than_ten(11))


### YOUR CODE ENDS HERE ###


# ------------------------------------------------ #
'''odd_or_even'''

# Define a function named odd_or_even which takes in an integer and returns 'odd' if the number is odd, and 'even' if the number is even.


### YOUR CODE STARTS HERE ###

def odd_or_even(num):
  if num % 2 == 0:
    return "even"
  else: 
    return "odd"
print(odd_or_even(12))

### YOUR CODE ENDS HERE ###


# ------------------------------------------------ #
'''how_many_legs'''

# Define a function named how_many_legs, which takes three parameters, num_cows, num_chickens, and num_spiders and returns the total number of legs.


### YOUR CODE STARTS HERE ###
def how_many_legs(cow,chickens,spiders):
  legs = cow * 4 + chickens *2 + spiders * 8 
  return legs

print(how_many_legs(3,4,1))

### YOUR CODE ENDS HERE ###


# ------------------------------------------------ #
'''multiple_of_3'''

# Define a function named multiple_of_3, which takes one argument, an integer, and returns True if the integer is a multiple of 3 and False otherwise.


### YOUR CODE STARTS HERE ###

def multiple_of_3(int):
  if int % 3 == 0:
    return True
  else:
    return False
print(multiple_of_3(8))

### YOUR CODE ENDS HERE ###


# ------------------------------------------------ #
'''area_of_triangle'''

# Define a function named area_of_triangle, which takes two arguments as integers, base, and height and returns the area of a triangle of those dimensions. Note: The formula for area of a triangle is base times height divided by 2


### YOUR CODE STARTS HERE ###

def area_of_triangle(base,height):
  area = base * height / 2
  return area
  
print(area_of_triangle(7,10))

### YOUR CODE ENDS HERE ###


# ------------------------------------------------ #
'''concatenator'''

# Define a function named concatenator, which takes in two strings and returns them concatenated together.


### YOUR CODE STARTS HERE ###

def concatenator(str1,str2):
  newstr = str1 + str2
  return newstr
print(concatenator("hello","world"))


### YOUR CODE ENDS HERE ###


# ------------------------------------------------ #
'''less_than_ten'''

# Define a function named less_than_ten, which takes in a string and returns True if the length of the string is less than 10 and False otherwise.


### YOUR CODE STARTS HERE ###

def less_than_ten(str):
  if len(str) < 10:
    return True
  else:
    return False

print(less_than_ten("hfdshgsdfhsdfhsdhfllo"))
### YOUR CODE ENDS HERE ###


# ------------------------------------------------ #
'''even_or_odd'''

# Define a function named even_or_odd which takes in a string and returns 'odd' if the length of the string is odd, and 'even' if the length of the string is even.


### YOUR CODE STARTS HERE ###

def even_or_odd(str):
  if len(str) % 2 == 0:
    return "even"
  else:
    return "odd"
print(even_or_odd("sgsdfhsdfh"))

### YOUR CODE ENDS HERE ###


# ------------------------------------------------ #
'''space_count'''

# Define a function named space_count, which takes a string as an argument, and returns the number of spaces in the string. Note: If there are no spaces, it should return 0.


### YOUR CODE STARTS HERE ###

def space_count(str):
  count = 0
  for i in range(0, len(str)):
    if str[i] == " ":
      count += 1
  return count
print(space_count("terst fsdg sdfg sdfg "))

### YOUR CODE ENDS HERE ###


# ------------------------------------------------ #
'''how_many_vowels'''

# Define a function named how_many_vowels, which takes in a strings and returns the total number of vowels of the string.


### YOUR CODE STARTS HERE ###
def how_many_vowels(str):
  count = 0
  for i in range(0,len(str)):
    i = str[i].lower()
    if i in ["a","e","i","o","u"]:
      count += 1
  return count

print(how_many_vowels("I have seven vowels"))

### YOUR CODE ENDS HERE ###


# ------------------------------------------------ #
'''three_es'''

# Define a function named three_es, which takes in one argument, a string, and returns True if the string contains at least 3 e's and False otherwise. Don't forget to account for capitalization.


### YOUR CODE STARTS HERE ###
def three_es(str):
  e_count = 0
  for i in range(0,len(str)):
    if str[i] in ["e","E"]:
      e_count += 1
  if e_count == 3:
    return True
  else:
    return False
print(three_es("eeee"))


### YOUR CODE ENDS HERE ###


# ------------------------------------------------ #
'''
1. LOG GENERATOR
  Write a Function called log_generator that takes 5 arguments:
    a string date in the form 'mm-dd-yyyy' (exactly 10 characters)
    a string ip_addr in the form 'xxx.xxx.xxx.xxx' (minimum 7 characters, maximum 15 characters)
    a string proto (either 'TCP' or 'UDP')
    an int src_port (in the range of 0-65535)
    an int dst_port (in the range of 0-65535)
  
  Your function should test for proper date length:
    if the length of the given date is not exactly 10 charaters (dashes included), return "Error: Incorrect date format given. Date must be formatted as mm-dd-yyyy"
  
  Your function should test for proper IP address length:
    if the length of the given ip address is less than 7 or greater than 15, your function should return "Error: Impossible IP address length given"
  
  Your function should test for proper protocols:
    if a string other than "TCP"or "UDP" is given (capitalization counts), your function should return "Error: Incorrect protocol given. Must be TCP or UDP"
  
  Your function should test for proper src_port ranges:
    if an int smaller than 0 or larger than 65535 is given for either the src or dst port, your function should return "Error: Incorrect port number given for src_port: <src_port>"

  Your function should test for proper dst_port ranges:
    if an int smaller than 0 or larger than 65535 is given for either the src or dst port, your function should return "Error: Incorrect port number given for dst_port: <dst_port>"

  If everything is formatted correctly, your function should create a log entry and return it in the format:

"<date> | <ip_addr> | <proto> | <src_port> | <dst_port>"'''


### YOUR CODE STARTS HERE ###

def log_generator(date, ip, proto, srcport, dstport):
  log = ""
  if len(date) != 10:
    return "Error: Incorrect date format given. Date must be formatted as mm-dd-yyyy"
  else:
    log += date + " | "
  if len(ip) < 7 or len(ip) > 15:
    return "Error: Impossible IP address length given"
  else:
    log += ip + " | "
  if proto in {"UDP", "TCP"}:
    log += proto + " | "
  else:
    return "Error: Incorrect protocol given. Must be TCP or UDP"
  if srcport < 0 or srcport > 65535:
    return "Error: Incorrect port number given for src_port: " + str(
      srcport)
  else:
    log += str(srcport) + " | "
  if dstport < 0 or dstport > 65535:
    return "Error: Incorrect port number given for dst_port: " + str(
      dstport)
  else:
    log += str(dstport) 
  return log


print(log_generator('08-16-1998', '192.168.1.1', 'UDP', -1, 80))

### YOUR CODE ENDS HERE ###


# ------------------------------------------------ #
'''
2. ASCII BATTLE OF THE B AND P CHARACTER CLANS
  The Bs and the Ps are two warring ASCII Character Clans and they cannot decide who is the better ASCII Character Clan. The B's think they are better because they have an even number of humps, while the Ps think their odd number of humps are more artistically pleasing.

  Write a function Bs_or_Ps that takes a string battle as an argument, that only contains the characters "B" and "P" (capitalization counts) in varying amounts.

  If there are more Bs than Ps, return "The B Character Clan is victorious!"
  If there are more Ps than Bs, return "The P Character Clan is victorious!"
  In the event of a tie:
    If there are an even amount of Bs and Ps, then the Bs ultimately win and return "The B Character Clan is victorious!"
    If there are an odd amount of Bs and Ps, then the Ps ultimately win and return "The P Character Clan is victorious!"
  BONUS: Only use one return statement in the entire function'''


### YOUR CODE STARTS HERE ###

def Bs_or_Ps(str):
  b_count = 0
  p_count = 0
  for i in str:
    if i == "B":
      b_count += 1
    elif i == "P":
      p_count += 1
    else:
      pass
  if b_count > p_count:
    return "The B Character Clan is victorious!"
  elif b_count < p_count:
    return "The P Character Clan is victorious!"
  elif b_count == p_count and b_count % 2 == 0:
    return "The B Character Clan is victorious!"
  else:
    return "The P Character Clan is victorious!"


print(Bs_or_Ps("BBBPPP"))


### YOUR CODE ENDS HERE ###