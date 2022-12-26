Python 3.11.0a5 (main, Feb  3 2022, 19:32:53) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
a='apple';b='paple'
a
'apple'
b
'paple'
sorted(a)
['a', 'e', 'l', 'p', 'p']
sorted(b)
['a', 'e', 'l', 'p', 'p']
'apple'.split()
['apple']
'apple paple'.split()
['apple', 'paple']
'a,p,p,l,e'.split(',')
['a', 'p', 'p', 'l', 'e']
'app.le.is.sweet'.split('.')
['app', 'le', 'is', 'sweet']
'today is monday'.split('')
Traceback (most recent call last):
  File "<pyshell#9>", line 1, in <module>
    'today is monday'.split('')
ValueError: empty separator
'today is monday'.split('')
Traceback (most recent call last):
  File "<pyshell#10>", line 1, in <module>
    'today is monday'.split('')
ValueError: empty separator
'today is monday'.split(' ')
['today', 'is', 'monday']
'today is monday'.split( )
['today', 'is', 'monday']
'computer'.split(',')
['computer']
'computer'.split( )
['computer']
'computer'.split(' ' )
['computer']
'apple mango'.split()
['apple', 'mango']
