Python 3.12.3 (tags/v3.12.3:f6650f9, Apr  9 2024, 14:05:25) [MSC v.1938 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
a=[2,4,7,9]
a
[2, 4, 7, 9]
a[2]
7
a[0:2]
[2, 4]
a[1:]
[4, 7, 9]
a[:2]
[2, 4]
a[-1]
9
a[-1:-2]
[]
a[-3]
4
a=['abc','xyz','ijk','mno']
a
['abc', 'xyz', 'ijk', 'mno']
val=[3170,'Harini','cse']
b=[1,2,3,4]
str=[b,a]
str
[[1, 2, 3, 4], ['abc', 'xyz', 'ijk', 'mno']]
len(a)
4
a.append('A')
a
['abc', 'xyz', 'ijk', 'mno', 'A']
b.insert(5)
Traceback (most recent call last):
  File "<pyshell#22>", line 1, in <module>
    b.insert(5)
TypeError: insert expected 2 arguments, got 1
b
[1, 2, 3, 4]
b.insert(2,5)
b
[1, 2, 5, 3, 4]
b.remove(7)
Traceback (most recent call last):
  File "<pyshell#26>", line 1, in <module>
    b.remove(7)
ValueError: list.remove(x): x not in list
b.remove(5)
b
[1, 2, 3, 4]
b.pop(3)
4
b
[1, 2, 3]
>>> b.pop()
3
>>> //last elt
SyntaxError: invalid syntax
>>> del a[2:]
>>> a
['abc', 'xyz']
>>> #mulltiple deletion
>>> b
[1, 2]
>>> b.extend(6,8,9)
Traceback (most recent call last):
  File "<pyshell#37>", line 1, in <module>
    b.extend(6,8,9)
TypeError: list.extend() takes exactly one argument (3 given)
>>> b.extend([5,6,8,9])
>>> b
[1, 2, 5, 6, 8, 9]
>>> # [] is mandetory as we are passing the list
>>> min(b)
1
>>> max(b)
9
>>> sum(b)
31
>>> g=[5,3,8,1,10,9]
>>> g.sort()
>>> g
[1, 3, 5, 8, 9, 10]
>>>     # list.min()
...     
>>>     #
...     
>>>     #list.max()
...     
>>> #list.sort()
...     
>>> #list.sum
...     
