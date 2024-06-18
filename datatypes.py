Python 3.12.3 (tags/v3.12.3:f6650f9, Apr  9 2024, 14:05:25) [MSC v.1938 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
a=11
id(a)
140709429385976
#address of variable a
b=a
b
11
id(b)
140709429385976
#same address as a
#memory effecient
#both will point to same box
b=20
id(b)
140709429386264
#even values are object
id(10)
140709429385944
id(11)
140709429385976
k=11
id(k)
140709429385976
type(k)
<class 'int'>
t=5.777
type(t)
<class 'float'>
# DATATYPES
# int,float,complex,bool
a=4
type(a)
<class 'int'>
b=3.5
type(b)
<class 'float'>

c=int(b)
c
3
d=float(a)
d
4.0
e=3+9j
e
(3+9j)
f=complex(a,c)
f
(4+3j)
a>c
True
a<c
False
bool=a>c
bool
True
int(true)
Traceback (most recent call last):
  File "<pyshell#37>", line 1, in <module>
    int(true)
NameError: name 'true' is not defined. Did you mean: 'True'?
int(True)
1
>>> #list,set,tuples
>>> s={5,6}
>>> type(s)
<class 'set'>
>>> t=(4,5)
>>> type(t)
<class 'tuple'>
>>> str="Harini"
>>> str
'Harini'
>>> type(str)
<class 'str'>
>>> #No char
>>> range(10)
range(0, 10)
>>> list(range(10))
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
>>> list(range(2,10,2))
[2, 4, 6, 8]
>>> # start,end,difference (in the above even)
>>> #Squence:list,tuples,set,string,range
>>> a=list(range(10))
>>> a
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
>>> #Dictionary
>>> #Key value pair
>>> val={'Harini':'paint','lily':'garden','harry':'spell'}
>>> type(val)
<class 'dict'>
>>> val.keys()
dict_keys(['Harini', 'lily', 'harry'])
>>> val.values()
dict_values(['paint', 'garden', 'spell'])
>>> val['lily']
'garden'
>>> val.get('harry')
'spell'
>>> #None=NULL
>>> #Mapping:Distionary
