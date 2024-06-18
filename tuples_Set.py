Python 3.12.3 (tags/v3.12.3:f6650f9, Apr  9 2024, 14:05:25) [MSC v.1938 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> #tuples
>>> #   []->()
>>> a=(2,4,6,7,8)
>>> a[4]
8
>>> a.count(4)
1
>>> # we use tuples when there is no need for the change of value
>>> # iteration is faster hence enhancement
>>> # SET
>>> set={12,23,14,75}
>>> s
Traceback (most recent call last):
  File "<pyshell#9>", line 1, in <module>
    s
NameError: name 's' is not defined
>>> set
{75, 12, 14, 23}
>>> # it will not return in the same order
>>> set={12,23,14,75,23}
>>> set
{75, 12, 14, 23}
>>> # redundant wont be displayed
>>> #indexing not supported
>>> set[3]
Traceback (most recent call last):
  File "<pyshell#16>", line 1, in <module>
    set[3]
TypeError: 'set' object is not subscriptable
>>> #list heterogeneous
>>> #tuples cannot change value
>>> #set no sequence & no duplicate value
>>> # tuples immutable
