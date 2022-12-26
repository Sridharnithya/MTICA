def count_Spcharacter(s):
    Spcharacter=0
    for i in s:
        if i not in 'ASDFGHJKLQWRzxvnmc':
            Spcharacter+=1
    return Spcharacter
str1=input( )
a=count_Spcharacter(str1)
print("No of Spcharacters in:'", str1,"'is",a)
