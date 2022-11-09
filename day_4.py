Python 3.7.0 (v3.7.0:1bf9cc5093, Jun 27 2018, 04:59:51) [MSC v.1914 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> id(12)
140706937492864
>>> id(12.0)
1923380067424
>>> a = 12
>>> id(a)
140706937492864
>>> #------------------
>>> print()

>>> help(Print)
Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    help(Print)
NameError: name 'Print' is not defined
>>> help(print())

Help on NoneType object:

class NoneType(object)
 |  Methods defined here:
 |  
 |  __bool__(self, /)
 |      self != 0
 |  
 |  __repr__(self, /)
 |      Return repr(self).
 |  
 |  ----------------------------------------------------------------------
 |  Static methods defined here:
 |  
 |  __new__(*args, **kwargs) from builtins.type
 |      Create and return a new object.  See help(type) for accurate signature.

>>> help(id)
Help on built-in function id in module builtins:

id(obj, /)
    Return the identity of an object.
    
    This is guaranteed to be unique among simultaneously existing objects.
    (CPython uses the object's memory address.)

>>> # -------------------------
     
>>> place = 'pune'
     
>>> print('Hello Good morning')
     
Hello Good morning
>>> print('Hello \nGood morning')
     
Hello 
Good morning
>>> print('Hello \tGood morning')
     
Hello 	Good morning
>>> #----------------------
     
>>> # Typecasting:
     
>>> # Type conversion
     
>>> # converting a data from one type to other
     
>>> a
     
12
>>> #convert a into a str
     
>>> str(a)
     
'12'
>>> a
     
12
>>> type(a)
     
<class 'int'>
>>> num = '23234'
     
>>> num
     
'23234'
>>> type(num)
     
<class 'str'>
>>> #convert num to float
     
>>> float(num)
     
23234.0
>>> # 2 Types
     
>>> # 1. Implicite conversion
     
>>> # A conversion perfromed by python itself
     
>>> 10 + 20
     
30
>>> 10 + 20.
     
30.0
>>> 10/2
     
5.0
>>> #2. Explicite conversion
     
>>> # a conversion performed by user as per requirement
     
>>> int(10 + 20.)
     
30
>>> num
     
'23234'
>>> #convert num into complex format
     
>>> complex(num)
     
(23234+0j)
>>> #----------------------
     
>>> type(num)
     
<class 'str'>
>>> num
     
'23234'
>>> num = float(num)
     
>>> num
     
23234.0
>>> type(num)
     
<class 'float'>
>>> rate = 10
     
>>> rate
     
10
>>> qty = input('Enter your quantity:')
     
Enter your quantity:5
>>> qty
     
'5'
>>> #final bill
     
>>> rate * qty
     
'5555555555'
>>> # in above case it is performing repettition
     
>>> rate * int(qty)
     
50
>>> #####################
     
>>> # NUMBER SYSTEM:
     
>>> # Binary [0,1]- base 2
     
>>> # Octal [0-7]-  base 8
     
>>> # Decimal [0-9]- base 10
     
>>> # Hexa decimal [0-9A-F]
     
>>> # Default number system we have is Decimal
     
>>> n = 100
     
>>> n
     
100
>>> # Decimal to Other number system conversion
     
>>> bin(n)
     
'0b1100100'
>>> bin(15)
     
'0b1111'
>>> help(bin)
     
Help on built-in function bin in module builtins:

bin(number, /)
    Return the binary representation of an integer.
    
    >>> bin(2796202)
    '0b1010101010101010101010'

>>> #octal
     
>>> oct(n)
     
'0o144'
>>> oct(9)
     
'0o11'
>>> bin(12.33)
     
Traceback (most recent call last):
  File "<pyshell#70>", line 1, in <module>
    bin(12.33)
TypeError: 'float' object cannot be interpreted as an integer
>>> # bin to octal
     
>>> bin(15)
     
'0b1111'
>>> oct('0b1111')
     
Traceback (most recent call last):
  File "<pyshell#73>", line 1, in <module>
    oct('0b1111')
TypeError: 'str' object cannot be interpreted as an integer
>>> 0b1111
     
15
>>> 0o11
     
9
>>> oct(0b1111)
     
'0o17'
>>> oct(15)
     
'0o17'
>>> #hex
     
>>> n
     
100
>>> hex(n)
     
'0x64'
>>> 0x64
     
100
>>> 0o23
     
19
>>> oct(19)
     
'0o23'
>>> 0o23
     
19
>>> 0O23
     
19
>>> #---------------------------------------
     
>>> # We can not use reserved words as an identifiers
     
>>> # keywords are reserved words in python
     
>>> import keyword
     
>>> keyword.kwlist
     
['False', 'None', 'True', 'and', 'as', 'assert', 'async', 'await', 'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield']
>>> in  = 500
     
SyntaxError: invalid syntax
>>> or = 'python'
     
SyntaxError: invalid syntax
>>> #----------------------------
     
>>> print= 10
     
>>> print
     
10
>>> id = 900
     
>>> id
     
900
>>> print()
     
Traceback (most recent call last):
  File "<pyshell#98>", line 1, in <module>
    print()
TypeError: 'int' object is not callable
>>> print(100)
     
Traceback (most recent call last):
  File "<pyshell#99>", line 1, in <module>
    print(100)
TypeError: 'int' object is not callable
>>> type(print)
     
<class 'int'>
>>> type(id)
     
<class 'int'>
>>> id(100)
     
Traceback (most recent call last):
  File "<pyshell#102>", line 1, in <module>
    id(100)
TypeError: 'int' object is not callable
>>> 
