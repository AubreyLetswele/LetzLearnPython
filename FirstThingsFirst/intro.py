#This piece of code will have all basics combined to get started with Python.

# 1. Declaring variables and printing them together.
firstline="Hello Python"
secondline="Hello World"
year=2025
#print(firstline +", " + secondline + " " + str(year))


# 2. getting datatypes and conditional booleans.
name = "Aubrey"
age = 21
salary = 45000.50
#print(type(name))  
#print(type(salary))  
#print(isinstance(age, int))



# 3. Simple math.
x=6
y=4
z1=x+y
z2=x*y
z3=x/y
z4=x-y
z5=x**y
z6=x%y
z7=round(x//y,1) #round to 1 decimal place.

# 4. String slicing, this is useful for extracting specific parts of strings.
s="PythonProgramming"
slice1=s[0:6]
slice2=s[6:]
#print("Sliced string: ", slice1, slice2)

# 5. Lists, creating a string list, works the same with other data types.
Samsung_Items = [
  "Smart TV", 
  "smartphone", 
  "laptop", 
  "Buds",
  "Tablet"
]
Samsung_Items.append("Refrigerator")  # Adding an item to the list.
Samsung_Items[0]="Microwave" # lists are mutable, so we can change items.
#print(Samsung_Items[2])  # Accessing a specific item by index.
#print("Samsung Items: ", Samsung_Items)


# 6. Simple function with 1 parameter and a default value.
def greet_user(username="Guest"):
    """Displays a personalized greeting."""
    if isinstance(username, str) and username.strip():
        print(f"Hello, {username.strip().title()}!")
    else:
        print("Hello, Guest!")    
#greet_user("Aubrey")


# 7. Useful built-in functions
xarr=[14, 42, 3, 84, 95, 60]

mx= max(xarr) 
min= min(xarr)
ln= len(xarr)
srt= sorted(xarr)
srtR= sorted(xarr, reverse=True)
#print("Max:", mx, "Min:", min, "Length:", ln, "Sorted:", srt, "Reverse Sorted:", srtR)


# 8. Exception Handling, (can be done for all tryes of errors: IndexError, ValueError, KeyError, etc)
prices = [559, 879, "N/A", 349]
try:
  print(sum(prices))
except TypeError:
  print("Check the prices")
finally:
  print("Need help? Contact us")
  
  
  # 9. Lamda function for quick operations.
  res = (lambda x, y: x + y) (2, 3)
  #print("lambda result:", res)
  
  # 10. Map and filters
  #List of names in various cases
names = ["aubreyletz", "bob", "AUBREY", "lEtz"]
def capitalize(name): # Function to capitalize each name
  return name.capitalize()
capitalized = map(capitalize, names)
capitalized = list(capitalized)
#print(capitalized)
  
   
#Example 2: Applying a discount to a list of prices using map()
prices = [30.00, 10.10, 8, 19.00]
def discount(price):
  discounted_price = price * 0.9
  return discounted_price
discounted_prices = list(map(discount, prices))
#print("Discounted Prices:", discounted_prices)



# 11. importing modules and using functions from them.
import math
import random
import datetime

sqrt_val = math.sqrt(64)
randN= random.randint(1, 100)
current_date = datetime.datetime.now().date()



# 12. importing libraries and using them.
import numpy as np
arrayN = np.array([1, 2, 3, 4, 5])
meanN = np.mean(arrayN)
print("Mean of array:", meanN)

