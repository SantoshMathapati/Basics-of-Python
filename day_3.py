Python 3.7.0 (v3.7.0:1bf9cc5093, Jun 27 2018, 04:59:51) [MSC v.1914 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> 12 is 12
True
>>> 12 is 12.
False
>>> id(12)
140707114767744
>>> id(12.0)
2818820979712
>>> 12. is 12.
True
>>> 12 == 12.0
True
>>> # == content equality
>>> # is checks address id() :performs address equality
>>> #--------------------------------
>>> id(12.0)
2818820979808
>>> id(12.0)
2818820978176
>>> 12.0 is 12.0
True
>>> g1 = 12.0
>>> g2 = 12.0
>>> g1 is g2
False
>>> id(g1)
2818820979808
>>> id(g2)
2818820978224
>>> #-------------------
>>> #Operators
>>> # Membership operators
>>> # To check either an object is a member of collection or not
>>> s = 'virat kohli'
>>> s
'virat kohli'
>>> # 2 types: in , not in
>>> 'v' in s
True
>>> # answer is in boolean form
>>> 'rohit' in s
False
>>> 'rohit' not in s
True
>>> 120 in s
Traceback (most recent call last):
  File "<pyshell#28>", line 1, in <module>
    120 in s
TypeError: 'in <string>' requires string as left operand, not int
>>> '120' in s
False
>>> k = [100,102,104]
>>> k
[100, 102, 104]
>>> 100 in k
True
>>> '100' in k
False
>>> k1 = [100,'100','100.0']
>>> 
>>> k1
[100, '100', '100.0']
>>> '100' in k1
True
>>> #---------------------
>>> # Bitwise operator: & (and), | (or), ~ (not), ^ (XOR)
>>> #-----------------------------
>>> # print() function
>>> print()

>>> # print(value,...,sep = ' ',end='\n')
>>> print(100)
100
>>> print(100,200,300)
100 200 300
>>> print(100,'python',30.99)
100 python 30.99
>>> print(100,'python',30.99,sep = '--') #change sep
100--python--30.99
>>> # sep works between 2 objects only
>>> print(100,sep='==>')
100
>>> print(100,'A',sep='==>')
100==>A
>>> # end: default it \n means a new line at end
>>> # we can modify end with any oher string
>>> # other*
>>> print(100,'A')
100 A
>>>  print(100,'A',end='end of stetemnt')
SyntaxError: unexpected indent
>>> print(100,'A',end='end of stetemnt')
100 Aend of stetemnt
>>> # ramesh is 28 yrs old
>>> print(100)
100
>>> print(100,end='\n\n')
100

>>> print(100,end='\n\n\n')
100


>>> # take the help of help() function
>>> help(print)
Help on built-in function print in module builtins:

print(...)
    print(value, ..., sep=' ', end='\n', file=sys.stdout, flush=False)
    
    Prints the values to a stream, or to sys.stdout by default.
    Optional keyword arguments:
    file:  a file-like object (stream); defaults to the current sys.stdout.
    sep:   string inserted between values, default a space.
    end:   string appended after the last value, default a newline.
    flush: whether to forcibly flush the stream.

>>> help(id)
Help on built-in function id in module builtins:

id(obj, /)
    Return the identity of an object.
    
    This is guaranteed to be unique among simultaneously existing objects.
    (CPython uses the object's memory address.)

>>> name  = 'sarang'
     
>>> place = 'Pune'
     
>>> name
     
'sarang'
>>> place
     
'Pune'
>>> # Hello, your name is sarang, and place is Pune
     
>>> print('Hello, your name is:',name)
     
Hello, your name is: sarang
>>> print('Hello, your name is:',name,', and place is:',place)
     
Hello, your name is: sarang , and place is: Pune
>>> # Q> can we use escape sequences: \n(new line), \t(tab 4 space)
     
>>> print('Hello, your name is:',name,', and place is:',place)
     
Hello, your name is: sarang , and place is: Pune
>>> print('Hello, your name is:',name,',\nand place is:',place)
     
Hello, your name is: sarang ,
and place is: Pune
>>> print('Hello, your name is:',name,',\n and place is:',place)
     
Hello, your name is: sarang ,
 and place is: Pune
>>> print('Hello,         your name is:',name,',\n and place is:',place)
     
Hello,         your name is: sarang ,
 and place is: Pune
>>> # space is also a part of string
     
>>> print('Hello, your name is:',name,',\tand place is:',place)
     
Hello, your name is: sarang ,	and place is: Pune
>>> print(1,2,3)
     
1 2 3
>>> print(1,2,3,sep='\t')
     
1	2	3
>>> print(1,'\t',2,'\t',3)
     
1 	 2 	 3
>>> print('Milind','Dhavale')
     
Milind Dhavale
>>> print('Milind'+'Dhavale')
     
MilindDhavale
>>> 'Milind'+'Dhavale' #it does concatention
     
'MilindDhavale'
>>> 'Milind'+' Dhavale'
     
'Milind Dhavale'
>>> 'Milind '+'Dhavale'
     
'Milind Dhavale'
>>> 'Milind'+' '+'Dhavale'
     
'Milind Dhavale'
>>> pi = 3.14
     
>>> r = 4
     
>>> print('Area of circle is:',pi*r**2)
     
Area of circle is: 50.24
>>> area = pi*r*r
     
>>> area
     
50.24
>>> print('Area of circle is:',area)
     
Area of circle is: 50.24
>>> # input(): it is a function, used to take input from user
     
>>> r = input('Enter the radius of a circle:')
     
Enter the radius of a circle:2.1
>>> r
     
'2.1'
>>> type(r)
     
<class 'str'>
>>> # input always takes value in str form
     
>>> # so we need to convert/typecast
     
>>> r = float(input('Enter the radius of a circle:'))
     
Enter the radius of a circle:2.1
>>> r
     
2.1
>>> type(r)
     
<class 'float'>
>>> print('Area of circle is:',pi*r**2)
     
Area of circle is: 13.8474
>>> #---------------
     
>>> 12.33
     
12.33
>>> int(12.33)
     
12
>>> #Typecast means converting a data from one type to other type
     
>>> str(12.33)
     
'12.33'
>>> print('Area of circle is:',round(pi*r**2,2))
     
Area of circle is: 13.85
>>> 
