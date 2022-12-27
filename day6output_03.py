Python 3.11.0a5 (main, Feb  3 2022, 19:32:53) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
print('{0},{1}, {2}'.format('apple','banana','carrot','pen'))
apple,banana, carrot
print('{0},{1}{0}{0}{3} {2}'.format('apple','banana','carrot','pen'))
apple,bananaappleapplepen carrot
print('{0},{1} {0}{0}{3} {2}'.format('apple','banana','carrot','pen'))
apple,banana appleapplepen carrot
print('{0},{1},{0},{0},{3} {2}'.format('apple','banana','carrot','pen'))
apple,banana,apple,apple,pen carrot
print('{},{}, {}'.format('apple','banana','carrot','pen'))
apple,banana, carrot
print('Gangully purchased a kg of {},a dozen of {}, and half kg of carrot {}'.format('apple','banana','carrot','pen'))
Gangully purchased a kg of apple,a dozen of banana, and half kg of carrot carrot
print('Gangully purchased a kg of {},a dozen of {}, and half kg of {}'.format('apple','banana','carrot','pen'))
Gangully purchased a kg of apple,a dozen of banana, and half kg of carrot
print('Gangully purchased a kg of {},a dozen of {}, and half kg of {}'.format('apple','banana','carrot'))
Gangully purchased a kg of apple,a dozen of banana, and half kg of carrot
print('Gangully purchased a kg of {0}and {2},Manohar purchased a dozen of {1}, and Arun purchased half kg of {2}'.format('apple','banana','carrot'))
Gangully purchased a kg of appleand carrot,Manohar purchased a dozen of banana, and Arun purchased half kg of carrot

====================================================== RESTART: Shell ======================================================
print('{2}, {1}, {0}'.format('apple','banana','carrot'))
carrot, banana, apple
print('{2}, {1},{1}, {0}'.format('apple','banana','carrot'))
carrot, banana,banana, apple
print('{2}, {1}, {0}'.format(*'abcd'))
c, b, a
x,*y,z='computer'
x
'c'
z
'r'
y
['o', 'm', 'p', 'u', 't', 'e']
*x,y='abcd'
x
['a', 'b', 'c']
y
'd'
print('coordinates: (latitude), (longitude)'.format(latitude='37.24N', longitude='-115.81W'))
coordinates: (latitude), (longitude)
print('coordinates: {latitude},{longitude}'.format(latitude='37.24N', longitude='-115.81W'))
coordinates: 37.24N,-115.81W
print('Welcome :{name}, your college is: {college}'.format(name='Gangully, your college is:MTICA'))
Traceback (most recent call last):
  File "<pyshell#21>", line 1, in <module>
    print('Welcome :{name}, your college is: {college}'.format(name='Gangully, your college is:MTICA'))
KeyError: 'college'
print('Welcome :{name}, your college is: {college}'.format(name='Gangully', college='MTICA'))
Welcome :Gangully, your college is: MTICA
print('Welcome :{name}, your college is: {college}'.format(name='Nithya', college='MTICA'))
Welcome :Nithya, your college is: MTICA
coord={'latitude': '37.24N', 'longitude': '-115.81W'}
print('coordinates: {latitude}, {longitude}'.format(**coord))
coordinates: 37.24N, -115.81W
student={41:'Nithya',79:'sanya'}
type(student)
<class 'dict'>
student
{41: 'Nithya', 79: 'sanya'}
student.keys()
dict_keys([41, 79])
student.values()
dict_values(['Nithya', 'sanya'])
type(coord)
<class 'dict'>
coord.keys()
dict_keys(['latitude', 'longitude'])
coord=(3,5)
abc=(2,9)
type(coord)
<class 'tuple'>
type(abc)
<class 'tuple'>
abc[0]
2
print('X: (0[0]); y: (0[1]);abc : {1[0]},{1[1]}'.format(coord,abc))
X: (0[0]); y: (0[1]);abc : 2,9
