"""
Write a python function to validate the Regualr Expression for the following :-

a. Email Address
"""

def validate_email(email):

    if email.count('@') != 1:
        return False
    
    username, domain = email.split('@')
    
    if not username or not domain:
        return False
    
    if '.' not in domain:
        return False
    
    domain_name, extension = domain.rsplit('.', 1)
    if not domain_name or not extension:
        return False
    
    return True
print ("Email Address Validation")
print("Correct Email address venktrmn2114@gmail.com  : ",validate_email("venktrmn2114@gmail.com"))
print("Incorrect Email address venktrmn2114gmail.com  : ",validate_email("venktrmn2114gmail.com"), "\n")

"""
Write a python function to validate the Regualr Expression for the following :-

b. Mobile numbers of Bangladesh
"""


def validate_bangladesh_mobile(number):
    if not number.startswith("+8801"):
        return False
    
    if number[5] not in "3456789":
        return False
    
    if len(number) != 14:
        return False
    
    if not number[6:].isdigit():
        return False
    
    return True

print ("Mobile numbers Validation of Bangladesh ")

print("Correct Mobile numbers of Bangladesh +8801712345678  : ", validate_bangladesh_mobile("+8801712345678"))
print("Incorrect Mobile numbers of Bangladesh +88934426952  : ", validate_bangladesh_mobile("+88934426952"), "\n")



"""
Write a python function to validate the Regualr Expression for the following :-

c. Telephone number of USA
"""

def validate_usa_phone(number):
    if not number.startswith("+1"):
        return False
    
    if len(number) != 12:
        return False
    
    if not number[2:].isdigit():
        return False
    
    return True

print("Telephone number Validation of USA ")  

print("Correct Telephone number of USA +19344269524  : ", validate_usa_phone("+19344269524"))
print("Incorrect Telephone number of USA +193442695240  : ", validate_usa_phone("+193442695240"), "\n")




"""
Write a python function to validate the Regualr Expression for the following :-

d. 16 character Alpha-Numeric password composed of alphabets of Upper Case, Lower Case, Special Characters, Numbers.
"""

def validate_password(password):
    if len(password) < 16:
        return False
    
    has_upper = has_lower = has_digit = has_special = False
    special_characters = "@$!%*?&"
    
    for char in password:
        if char.isupper():
            has_upper = True
        elif char.islower():
            has_lower = True
        elif char.isdigit():
            has_digit = True
        elif char in special_characters:
            has_special = True
    
    return has_upper and has_lower and has_digit and has_special


print("Validation for Strong PassWord ")  
    
  
print("Strong Password Venkat@9344269524  : ", validate_password("Venkat@9344269524"))
print("Weak Password venkat24  : ", validate_password("venkat24"), "\n")