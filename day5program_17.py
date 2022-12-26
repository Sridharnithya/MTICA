def extract_Digit(s):
    Digit=''
    for i in s:
        if i in '1234567':
            Digit+=i
    return Digit
str1=input( )
a=extract_Digit(str1)
print("Digits in:'", str1,"'is",a)
