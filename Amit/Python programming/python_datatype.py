"""
Python data types

1. Number
    A. Integer
    B. Float
    C. Complex Number

2. Sequential
    A. String
    B. List
    C. Tuple

3. Dictionary
4. Set
5. Boolean
"""
################################################
# Integer
"""
-> Integer data type represent with keyword as int (<class 'int'>)
-> Integer data type does have any limit to define the value
-> Integer is a immutable data type 
   Note: Immutable = value get replaced with new value for same object, variable - All data type except below one.
         Mutable = Update the value along with the old value. ex. - List, Set, Dictionary
-> Integer data type only contains whole number not with decimal
   Note: Positive and negative whole number can be considered as int only.           
"""
num1 = 40
print(type(num1))
# int()

num2 = 646487894878716878178978978979846841688679871879
print("num2 data type:", type(num2)) # <class 'int'>
print(num2)

num2 = 100 # replaced by new value for previous value.
print(num2)

num3 = 0
num4 = -500
print(num3)
print(num4)
################################################
# Float
"""
-> Float data type represent with keyword as float (<class 'float'>)
-> Float data type does have any limit to define the value
-> Float is a immutable data type
-> Float data type only contains pointer value or value with decimals.
   Note: Positive and negative number with decimal can be considered as float only.           
"""
var_a = 6464878948787168781.78978978979846841688679871879
print("num2 data type:", type(var_a)) # <class 'float'>
print(var_a)

var_b = 66.6689
print(var_b)

print('-'*50)
# Complex Number
"""
-> Complex number is the combination of imaginary and real values
-> Complex number is represent in the format of x & yj, where x = real and y = imaginary number from complex value
   Example - x + yj, x - yj, x * yj, any operator
-> Complex number is the immutable data type.
"""
var_c = 50 + 40j
print("Imaginary Value :", var_c.imag) # Left value is considered as imaginary value
print("Real Value :", var_c.real) # Left value is considered as real value

var_d = 5 + 10j
var_e = 7 + 15j
var_f = var_d + var_e
print("Addition of complex number:", var_f, type(var_f))

var_g = 10 * 10j
print("Addition of complex number:", var_g, type(var_g), var_g.imag, var_g.real)

result = complex(70, 80)
print(result) # (70+80j)

######################################
print("$"*50)
"""
# String Data Type
Note : - string can be use with Double quotes, single quotes or three single or double quotes.
-> Sting is immutable datatype.
-> String follows positive and negative indexing
-> Sting can be defined with single, double and triple quotes
-> String only contains any value under quotes considered as string.
"""
str_a = "Hello"
str_b = 'Python'
str_c = '''I am working on string data type'''
str_c = """I am working on string data type"""

print(str_a, type(str_a))
print(str_b, type(str_b))
print(str_c, type(str_c))

print(str_a[0])
print(str_a[-5])

######################################
print("$"*50)
"""
#  Data Type
"""