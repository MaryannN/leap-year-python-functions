# Code your functions here!

# 1. Write a function that checks to see if a given year is a leap year, by replacing "pass" with your own code, and returns either the boolean value True or False.

# def is_leap_year(year):
#   if year % 4 == 0:
#     return True
#   else:
#     return False
  
# 2. Write a function that takes in the current year and returns a string telling when the next leap year will be.

# def next_leap_year(year):
#   if year % 4 == 0:
#     return True
#   else:
#     left = year % 4
#     return f"{year} is not a leap year, but it will be in {left} years"

# 3. Write a function that takes in two years as arguments (a start_year and a last_year), and then prints out every single year between them that is a leap year. 

leap_years = []

def between_leap_year(start, end):
  year = start
  while year <= end:
    if year % 4 == 0:
      print(f"{year} is a leap year")
      leap_years.append(year)
    else:
      print(f"{year} is not a leap year")
    year += 1
  return leap_years 
