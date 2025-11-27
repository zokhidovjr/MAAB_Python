'''A year is a leap year if:
- It is divisible by 4, and
- It is NOT divisible by 100, unless it is also divisible by 400.'''

'''Parameters:
year (int): The year to be checked.

Returns:
bool: True if the year is a leap year, False otherwise.'''
def leap_year(year):
    if not isinstance(year, int):
        raise ValueError("Year must be an integer.")
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

#2
n = int(input())

if n % 2 == 1:
    print("Weird")
elif n % 2 == 0 and 2 <= n <= 5:
    print("Not Weird")
elif n % 2 == 0 and 6 <= n <= 20:
    print("Weird")
else:
    print("Not Weird")

#3
a = int(input("a = "))
b = int(input("b = "))

if a > b:
    a, b = b, a

if a % 2 != 0:
    a += 1

if b % 2 != 0:
    b -= 1

if a <= b:
    result = list(range(a, b + 1, 2))
else:
    result = []

print(result)
#----------------------------
a = int(input("a = "))
b = int(input("b = "))

x, y = min(a, b), max(a, b)

start = x + (x % 2)
end = y - (y % 2)

print(list(range(start, end + 1, 2)))
