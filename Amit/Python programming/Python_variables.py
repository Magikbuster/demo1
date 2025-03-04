"""
# a is nothing but the variable and 10 is the value for that variable a and "=" is nothing but the assignment operator in python
a = 10

# print will give you the value of variable a here.
# Note: - print with double quotes will print whatever available inside the print function,
# if we want to print value of variable we dont need to use double quotes inside print function.
print(a)

# id() function return the memory address of any variable
print(id(a))

# New variable
b = 10
# value for new variable b is same as a so it will be stored in same memory no new memory address assigned.
# if two variable holding the same value will keep the same memory address
# Memory manager is smart so he will store same address when we have same values for different variables
print(id(b))

# if values are different then memory will be different
c = 20
print(id(c))

# Assign same value to 3 different variables
p = q = r = 30
print("Value of p:", p)
print("Value of q:", q)
print("Value of r:", r)

# We can use multiple things inside print depending on the requirement
# id value for the same variables are as follows
print("Value of r:", p, id(p))
print("Value of r:", q, id(q))
print("Value of r:", r, id(r))

# Assign three different variables and different values to it.
x, y, z = 15, 25, 35
print("Value of r:", x, id(x))
print("Value of r:", y, id(y))
print("Value of r:", z, id(z))

# user can not assign any address to any variables explicitly, its predefined and can not be manipulated.

# Rules to define the variables
# 1. There should not be space in variable name
#    Example -> a b = 5 its invalid as it has space and a_b = 5 is valid as no space in between and managed with underscore.
#    Example -> a b c = 5 its invalid as it has space and User_name_value = MAGIK is valid as no space in between and managed with underscore.
user_name_value = 'MAGIK'
print (user_name_value)
# Note: - if using alphabets or alphanumneric keep the values in single quotes as character, for integer we dont need any quotes.

# 2. Special Characters are not allowed in tha variable name
#    example -> email&id is invalid
#    example -> email_id is valid
email_id = 'ammygawande@gmail.com'
print (email_id)

# 3. Can not contain number as prefix in the variable name
#    example -> 1var_value is invalid
#    example -> var_value1 is valid
var_value_1 = 'AMIT'
print (var_value_1)

# 4. Variable names are case-sensitives
Name = 'Amit'
name = 'Gawande'
nAme = 'Subhash'
NAME = 'Rekha'

print (Name)
print (NAME)
print (nAme)
print (name)
"""
##############################################################
"""
Math Operator
+ : Plus
- : Minus
* : Multiplication
/ : division with single slash
// : division with double slash
% : Remainder operator
** : power operator
== : Equal operator
"""

print ("_"*50)
# This will repeat "_" value 50 times
print ("#"*50)
# This will repeat "#" value 50 times
# Addition of two values
var1 = 10
var2 = 20
print ("Value of addition:", var1+var2)
var3 = var1+var2                                # store the addition value in var3
print ("Additional result:", var3)

print ("#"*50)
# Multiplication of two values
var4 = 10
var5 = 20
print ("Value of addition:", var4 * var5)
multiplication = var4*var5
print ("Additional result:", multiplication)

print ("#"*50)
# Subtraction of two values
A = 7
B = 25
C = B-A
print ("Subtraction result:", C)

print ("#"*50)
# Division of two values with single slash
A = 35
B = 7
print ("Div_1_slash result:", A/B)
# Div with single slash - will give you remainder values/values with pointers
# Div with double slash - will give you integer values/values without pointers/complete value without decimal
# Division of two values with double slash
A = 35
B = 7
print ("Div_1_slash result:", A//B)

print ("#"*50)
# Power operator
print("Power of 2:", 2**2) #2*2
print ("Cube of 2:", 2**3) #2*2*2
print ("Result is:", 2**4) #2*2*2*2