# This code is a decoder for RSA ID to get the Age & Gender of the user based on the ID number provided.

# Set current date manually. (Autodate can be implemented later)
CurrentYear = 2025
CurrentMonth = 12
CURR_DAY = 26

id_num = input("Enter 13-digit RSA ID: ")

# Validation
if len(id_num) == 13 and id_num.isdigit():
    
    # Extract Date of Birth (Slicing)
    yy = int(id_num[0:2])
    mm = int(id_num[2:4])
    dd = int(id_num[4:6])

    # Century Logic (Assume 2000s if yy <= 25)
    full_year = 2000 + yy if yy <= 25 else 1900 + yy

    # Age Calculation Logic
    age = CurrentYear - full_year
    # Adjusting the age if birthday hasn't happened yet this year
    if (mm > CurrentMonth) or (mm == CurrentMonth and dd > CURR_DAY):
        age -= 1

    # Gender Logic (7th digit), based on RSA ID structure.
    gender_digit = int(id_num[6])
    gender = "Female" if gender_digit < 5 else "Male"

    print("-" * 20)
    print(f"Birth Date: {dd:02d}/{mm:02d}/{full_year}")
    print(f"Gender:     {gender}")
    print(f"Age:        {age} years old")
    print("-" * 20)

else:
    print("Error: Please enter exactly 13 numeric digits.")