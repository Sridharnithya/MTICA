def extract_Specialcharacter(s):
    character=''
    for i in s:
        if i in '!@$&(*%#*)':
            character+=i
    return character
str1=input( )
a=extract_Specialcharacter(str1)
print("characters in:'", str1,"'is",a)
