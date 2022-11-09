Python 3.7.0 (v3.7.0:1bf9cc5093, Jun 27 2018, 04:59:51) [MSC v.1914 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> 3j
3j
>>> type(3j)
<class 'complex'>
>>> 2 +3j
(2+3j)
>>> type(2 +3j)
<class 'complex'>
>>> '3j'
'3j'
>>> type('3j')
<class 'str'>
>>> ''
''
>>> type('')
<class 'str'>
>>> type("")
<class 'str'>
>>> type(2 +3j)
<class 'complex'>
>>> r = 4
>>> pi = 3.14
>>> area = pi*r**2
>>> area
50.24
>>> r = 5
>>> r
5
>>> area
50.24
>>> area = pi*r**2
>>> area
78.5
>>> #----------------------------
>>> # Operators
>>> # Assignment operators
>>> a = 100
>>> a
100
>>> a + 100
200
>>> # but ur a is unchanged
>>> a
100
>>> a = a + 100 #uppdate a here
>>> a
200
>>> a += 50 # a = a + 50
>>> a
250
>>> # = assignment operator
>>> # +=,-=,*=, /=, %=,//=,**=
>>> a
250
>>> a -= 100 #a = a -100
>>> a
150
>>> a *= 2
>>> a
300
>>> a **= 2
>>> a
90000
>>> # apply remaining operators
>>> #----------------
>>> # Comparison or conditional operators
>>> # when we want to compare 2 object then use these operators
>>> # < > <= >= == !=
>>> 1 < 2
True
>>> # output is always in boolean form: True and False
>>> 'python' == 'Python'
False
>>> # how to check 2 objects are same or nt
>>> # use id()==> returns address of that object
>>> # if address of 2 objects is same then both objects are identical
>>> # otherwise the are different
>>> id('python')
1779695221648
>>> id('Python')
1779656316440
>>> # as id is different u get here False result
>>> x = 500
>>> y = 500
>>> x == y
True
>>> id(x)
1779695889840
>>> id(y)
1779695890320
>>> # == is used for content equality
>>> # not used for address equality
>>> # if we want to check for address equality
>>> # then use another operator
>>> # identity operator
>>> # is is not
>>> x == y
True
>>> id(x)
1779695889840
>>> id(y)
1779695890320
>>> x is y
False
>>> x
500
>>> y
500
>>> p1 = 'python'
>>> p1
'python'
>>> p2 = 'Python'
>>> p2
'Python'
>>> p1 == p2 # CONTENT EQUALITY
False
>>> p1 is p2
False
>>> # ADDRES EQUALITY
>>> # Q. WHAT IS ADDRESS EQUALITY AND CONTENT EQUALITY
>>> p = 10
>>> p
10
>>> q = 10.
>>> q
10.0
>>> # content equality
>>> p == q
True
>>> # address equality
>>> p is q
False
>>> id(p)
140707628307776
>>> id(q)
1779655556072
>>> id(p) == id(q)
False
>>> # not equal to !=
>>> 12 != 67
True
>>> p1
'python'
>>> p2
'Python'
>>> p1 != p2
True
>>> #----------------
>>> d1 = 200
>>> d1
200
>>> id(d1)
140707628313856
>>> d2 = 200
>>> d2
200
>>> id(d2)
140707628313856
>>> #-------------
>>> e1 = 22.22
>>> e1
22.22
>>> id(e1)
1779655556240
>>> e2 = 22.22
>>> e2
22.22
>>> id(e2)
1779655556096
>>> e3 = 22.22
>>> e3
22.22
>>> id(e3)
1779655556288
>>> 22.22
22.22
>>> id(200)
140707628313856
>>> id(d1)
140707628313856
>>> #-----------------------
>>> # Logical Operators
>>> # and or not
>>> # Used to compare  outputs of 2 conditions
>>> nm = 'rakesh'
>>> nm
'rakesh'
>>> ad = 23
>>> ag = 23
>>> ag
23
>>> # it result boolean output
>>> True and True
True
>>> True and False
False
>>> False and True
False
>>> False and False
False
>>> #-----------
>>> nm == 'rakesh'
True
>>> ag == 23
True
>>> nm == 'rakesh' and ag == 23
True
>>> nm == 'rakesh' and ag == 26
False
>>> nm == 'rupesh' and ag == 23
False
>>> nm == 'rupesh' and ag == 90
False
>>> #----------------
>>> # or
>>> True or True
True
>>> True or False
True
>>> False or True
True
>>> False or False
False
>>> nm =='ramesh' and ag == 23
False
>>> nm =='ramesh' or ag == 23
True
>>> # plz try other options
>>> #----------
>>> # not: negation
>>> not True
False
>>> not False
True
>>> nm =='sameer'
False
>>> not nm =='sameer'
True
>>> nm
'rakesh'
>>> not ag == 23
False
>>> ag == 23
True
>>> report = '+ve'
>>> report
'+ve'
>>> not
SyntaxError: invalid syntax
>>> not report == '-ve'
True
>>> not report == '+ve'
False
>>> #-------------------
>>> 10 and 12
12
>>> 'amol' and 'ramesh'
'ramesh'
>>> -1 and  -3
-3
>>> 12.5 and 56.6
56.6
>>> # Rule: if x value is True, then return y
>>> # x and y
>>> bool(10)
True
>>> bool('amol')
True
>>> bool(-1)
True
>>> bool(12.5)
True
>>> # all objects are True always except False, None, '',0
>>> bool(0)
False
>>> bool(None)
False
>>> bool('')
False
>>> bool(False)
False
>>> # Rule2: if x value is False then it returns x
>>> 0  and 2
0
>>> None and 'python'
>>> None
>>> None
>>> False and 34
False
>>> ''  and 55
''
>>> 
