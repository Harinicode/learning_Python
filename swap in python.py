Python 3.12.3 (tags/v3.12.3:f6650f9, Apr  9 2024, 14:05:25) [MSC v.1938 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> a,b=9,3
>>> temp=a
>>> a=b
>>> b=temp
>>> a
3
>>> b
9
>>> a=a+b
>>> b=a-b
>>> a=a-b
>>> a
9
>>> b
3
>>> #   Lets consider two numbers 4(100) and 5(101) if we add we get 9(1001)
>>> #
>>> # we are wasting 1 bit so the +- method is not convenient
>>> #XOR does not waste bit
>>> a=a^b
>>> b=a^b
>>> a=a^b
>>> a
3
>>> b
9
>>> a,b=b,a
>>> a
9
>>> b
3
>>> # ROT_TWO() swaps the top most stack items
