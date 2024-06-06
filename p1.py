Python 3.12.3 (tags/v3.12.3:f6650f9, Apr  9 2024, 14:05:25) [MSC v.1938 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> 2=5
SyntaxError: cannot assign to literal here. Maybe you meant '==' instead of '='?
>>> 2+5
7
>>> 9-2
7
>>> 4*3
12
>>> 4/2
2.0
>>> 4%2
0
>>> 1/2
0.5
>>> 5//2
2
>>> 5+7-2
10
>>> 2+3*4
14
>>> (2+3)*4
20
>>> 2*2*2
8
>>> 2**3
8
>>> 1//2
0
>>> 1%2
1
>>> 2%5
2
>>> 2/5
0.4
>>> 'harini'
'harini'
>>> 2%5
2
>>> print('harini')
harini
print("harini's laptop")
harini's laptop
print('harini "laptop"')
harini "laptop"
print('harini's laptop"')
      
SyntaxError: unterminated string literal (detected at line 1)
print('harini\'s "laptop"')
      
harini's "laptop"
harini**3
      
Traceback (most recent call last):
  File "<pyshell#24>", line 1, in <module>
    harini**3
NameError: name 'harini' is not defined
harini+ harini
      
Traceback (most recent call last):
  File "<pyshell#25>", line 1, in <module>
    harini+ harini
NameError: name 'harini' is not defined
'harini'**3
      
Traceback (most recent call last):
  File "<pyshell#26>", line 1, in <module>
    'harini'**3
TypeError: unsupported operand type(s) for ** or pow(): 'str' and 'int'
'harini'+'harini'
      
'hariniharini'
10*'harini'
      
'hariniharinihariniharinihariniharinihariniharinihariniharini'
print('c:\docs\nave')
      
c:\docs
ave
print(r'c:\docs\nave')              //raw
      
c:\docs\nave
Traceback (most recent call last):
  File "<pyshell#30>", line 1, in <module>
    print(r'c:\docs\nave')              //raw
NameError: name 'raw' is not defined
print(r'c:\docs\nave')
      
c:\docs\nave
