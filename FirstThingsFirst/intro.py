#This piece of code will have all basics combined to get started with Python.

# 1. Declaring variables and printing them together.
firstline="Hello Python"
secondline="Hello World"
year=2025
print(firstline +", " + secondline + " " + str(year))


# 2. getting datatypes and conditional booleans.
name = "Aubrey"
age = 21
salary = 45000.50
print(type(name))  
print(type(salary))  
print(isinstance(age, int))



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
print("Sliced string: ", slice1, slice2)


# 5. Simple function with 1 parameter and a default value.
def greet_user(username="Guest"):
    """Displays a personalized greeting."""
    if isinstance(username, str) and username.strip():
        print(f"Hello, {username.strip().title()}!")
    else:
        print("Hello, Guest!")
        
greet_user("Aubrey")
