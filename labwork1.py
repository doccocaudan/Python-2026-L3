#Ex1
a = float(input("Enter the value of radius:"))
pi = 3.14
print("Circle area = ", pi * a * a)



#Ex2
b = float(input("Enter the temperature in celsius: "))
print("Temperature in fahrenheit: ", b * 9/5 + 32)



#Ex3
c = int(input("Enter number: "))
if c < 2:
  print("is not a prime number")
else:
  print("is a prime number")
for i in range(2, c):
  if c % i == 0:
    print("is not a prime number")
    break
  else:
    print("is a prime number")



#Ex4
d = int(input("Enter a number: "))
sum = 0
for i in range(1,d):
  if d % i == 0:
    sum = i + sum
if sum == d:
  print("is a perfect number")
else:
  print("is not a perfect number")



#Ex5
e = str(input("What is your favorite color: "))
color = ["Yellow" , "Blue" , "Red"]
if e in color:
  print("Your color is at index ", str(color.index(e)), "in my list")
else:
  print("Sorry, I could not find your color")


  #Ex6:
print("range1", list(range(7)))
print("range2", list(range(1,11,3)))
print("range3", list(range(5,0,-1)))
print("range4", list(range(6,-3,-2)))



#Ex7:
def remove_dollar_sign(s):
  return s.replace("$", "")


#Ex8
list_number = [1,4,5,-1,10]
even_list = []
def extract_even(list_number):
  for i in list_number:
    if i % 2 == 0:
      even_list.append(i)
  return even_list
print(extract_even(list_number))


#Ex9:
def nonnegative_number(n):
  if n == 0 and n == 1:
    return 1
  else:
    return n * nonnegative_number(n-1)


#Ex10:
def divisor_number(n):
  for i in range(1,n+1):
    if n % i == 0:
      print(i)


#Ex11:
import math
x1 = int(input("Enter x1: "))
y1 = int(input("Enter y1: "))
x2 = int(input("Enter x2: "))
y2 = int(input("Enter y2: "))
def distance(x1, y1, x2, y2):
    d = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
    return d
result = distance(x1, y1, x2, y2)

print("Distance =", result)


#Ex12:
