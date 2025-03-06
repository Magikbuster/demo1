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
print("num2 data type:", type(num2))  # <class 'int'>
print(num2)

num2 = 100  # replaced by new value for previous value.
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
print("num2 data type:", type(var_a))  # <class 'float'>
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
print("Imaginary Value :", var_c.imag)  # Left value is considered as imaginary value
print("Real Value :", var_c.real)  # Left value is considered as real value

var_d = 5 + 10j
var_e = 7 + 15j
var_f = var_d + var_e
print("Addition of complex number:", var_f, type(var_f))

var_g = 10 * 10j
print("Addition of complex number:", var_g, type(var_g), var_g.imag, var_g.real)

result = complex(70, 80)
print(result)  # (70+80j)

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
str_d = """I am working on string data type"""

print(str_a, type(str_a))
print(str_b, type(str_b))
print(str_c, type(str_c))

print(str_a[0])
print(str_a[-5])

######################################
print("$"*50)
"""
# List Data Type
-> List is a mutable data type, we can modify the values in the list.
-> List follows +ve and -ve indexing
-> List can contain all type of data like int, float, str, etc.
-> List represent in square data type.
-> All the values inside list must be comma separated.
"""
list1 = [3, 3.4, 'Hello', ['a', 1, 3]]
print(list1, type(list1))
"""
# indexing - 
 0   1      2       3
[3, 3.4, 'Hello', ['a', 1, 3]]
 -4  -3    -2       -1 
"""
print(list1[3])
print(list1[-3])
print(list1[0])

list2 = [2, 4.5, 'python',
         [2, 4, 'abc'], (4, 5, 6),
         {'s', 'f', 7},            # Set
         {'b': 456, 'c': 524},   # Dictionary
         True, False, None]        # Boolean

print(list2, type(list2))
print("Number of values inside the list :", len(list2))

# Len is inbuilt function which will give the length of string, list tuple anything.
print("String length:", len("String"))  # 6

# Append is a method which can be used to add particular value at last for the selected list
# append can be used to add only one value, and it will be added into last inside the list.
# Method always used with the "."
list3 = [5, 7, 9, 10]
list3.append(15)
print(list3)

# All methods
print(dir(list))
"""
['__add__', '__class__', '__class_getitem__', '__contains__', '__delattr__', '__delitem__', '__dir__', '__doc__', '__eq__',
'__format__', '__ge__', '__getattribute__', '__getitem__', '__getstate__', '__gt__', '__hash__', '__iadd__', '__imul__', '__init__',
'__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__',
'__reversed__', '__rmul__', '__setattr__', '__setitem__', '__sizeof__', '__str__', '__subclasshook__', 'append', 'clear', 'copy', 'count',
'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort']
"""

print("*"*50)
"""
Tuple Data Type - Store such values which can be fixed and not needed to change/modify it.
-> Tuple is a immutable data type, once it is defined we can not modify it.
-> Tuple follows +ve and -ve indexing as like string and list
-> List can contain all type of data like int, float, str, tuple inside tuple, boolean, etc.
-> Tuple represent in round brackets.
-> Tuple is faster than list coz tuple has only one mode of access i.e. READ whereas list has two mode of access i.e. READ & WRITE.
-> Tuple store fixed data which can not be modified like Month in a year or day in a week etc.
"""
tup1 = (4, 4, 5, 6.6, [3, 4, 5],
        {'1': 456}, True)
print(tup1, type(tup1), len(tup1))
print(tup1[4])
print(dir(tuple))
"""
Methods of tuple class - ['__add__', '__class__', '__class_getitem__', '__contains__', '__delattr__', '__dir__', '__doc__', 
'__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getnewargs__', '__getstate__', '__gt__', '__hash__',
'__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mul__', '__ne__', '__new__', '__reduce__',
'__reduce_ex__', '__repr__', '__rmul__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 'count', 'index']
"""

print("#"*50)
"""
#########Dictionary data type#########
Without indexing we are assigning key value to particular data
# dict1 = {key : value} key must be unique and value can be common.
-> Dictionary is a mutable data type, we can update the data at any point of time inside the dictionary.
-> Dictionary does not follow +ve or -ve indexing
-> Dict store values in form of key and value format
-> Dict represent with {} braces.
-> Dict only contain unique keys, no duplicate key allowed in dict.
-> Dict can contain duplicate values for different keys.
-> Only immutable data type can be key in the dict like int, float, string, tuple, boolean
-> All type of data can store in dict.
-> Key will be always left side and value will be right side
-> left side key can be in [] brackets.
"""
dist1 = {'a' : 123, 'b' : 456}
print(dist1['a'])

dict2 = {'name': 'Amit', 'name': 'Gawande'}  # it will only pick last value for same key
dict2[43] = {4, 5, 6}
dict2[(5,6, 7)] = {3, 3, 4, 6}      # remaining all data type can be "KEY"
# dict2[[3, 3.3]] = 'Python'        # TypeError: unhashable type: 'list'
# list is a mutable data type, so it is not allowed to be a "KEY"
dict2['Python'] = 'Good Morning'
dict2[4.5] = 23
dict2[4.5] = True                   # selected this value as its the last or latest value for same key [4.5]
print(dict2)

# example - json is a dictionary format data