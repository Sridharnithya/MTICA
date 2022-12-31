string='''today we feel very good'''
ans=[i for i in string if i not in 'AEIOUaeiou']
print(''.join(ans))
