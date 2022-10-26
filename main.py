# Define a function named sum_of_two_nums, which takes in two numbers and returns the sum of those numbers.


def sum_of_two_nums(num_1, num_2):
  sum = num_1 + num_2
  return sum


print(sum_of_two_nums(6, 4))

# Define a function named greater_than_ten, which takes in an integer and returns True if the number is greater than 10 and False if the number is less than 10.


def greater_than_ten(x: int):
  if x > 10:
    return True
  if x < 10:
    return False


print(greater_than_ten(5))


# Define a function named odd_or_even, which takes in an integer and returns 'odd' if the number is odd, and 'even' if the number is even.
# Hint: you will need to use the modulus operator
def odd_or_even(x: int):
  if x % 2 == 0:
    return "even"
  else:
    return "odd"


print(odd_or_even(6))

# Define a function named how_many_legs, which takes three parameters, num_cows, num_chickens, and num_spiders, and returns the total number of legs.


def how_many_legs(num_cows, num_chickens, num_spiders):
  total_legs = num_cows * 4 + num_chickens * 2 + num_spiders * 8
  return total_legs


print(how_many_legs(2, 3, 4))


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
    return "Error: Incorrect port number given for src/dst_port: " + str(
      srcport)
  else:
    log += str(srcport) + " | "
  if dstport < 0 or dstport > 65535:
    return "Error: Incorrect port number given for src/dst_port: " + str(
      dstport)
  else:
    log += str(dstport) + " | "
  return log


print(log_generator('08-16-1998', '192.168.1.1', 'UDP', 6558, 80))


def bs_or_ps(str):
  b_count = 0
  p_count = 0
  for i in str:
    if i == "B":
      b_count += 1
    elif i == "P":
      p_count += 1
    else:
      pass
  if b_count < p_count:
    return "P's win"
  elif b_count > p_count:
    return "B's win"
  elif b_count == p_count and b_count % 2 == 0:
    return "B's win"
  else:
    return "P's win"


print(bs_or_ps("BBBPPP"))