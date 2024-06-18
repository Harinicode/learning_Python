Python 3.12.3 (tags/v3.12.3:f6650f9, Apr  9 2024, 14:05:25) [MSC v.1938 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
5//6
0
5/6
0.8333333333333334
a,b=3,5
a
3
b
5
-b
-5
b
5
b=-b
b
-5
a<b
False
a>b
True
a==b
False
b=3
a==b
True
a
3
a<=b
True
a>=b
True
a<>b
SyntaxError: invalid syntax
a!=b
False
>>> a<4&&b<4
SyntaxError: invalid syntax
>>> a<4&b<4
False
>>> a<4andb<4
SyntaxError: invalid decimal literal
>>> a<4 and b<4
True
>>> a<4 or b>4
True
>>> ~(a<4 or b>4)

Warning (from warnings module):
  File "<pyshell#24>", line 1
DeprecationWarning: Bitwise inversion '~' on bool is deprecated. This returns the bitwise inversion of the underlying int object and is usually not what you expect from negating a bool. Use the 'not' operator for boolean negation or ~int(x) if you really want the bitwise inversion of the underlying int.
-2
>>> not (a<4 or b>4)
False
>>> #The topics above are based on relational and logical operator
>>> #Number System
>>> bin(5)
'0b101'
>>> bin(25)
'0b11001'
>>> 0b11001
25
>>> oct(25)
'0o31'
>>> hex(25)
'0x19'
>>> hex(13)
'0xd'
>>> hex(10)
'0xa'
>>> 0xf
15
