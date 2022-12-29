num1=int(input("Enter a number:"))
num2=int(input("Enter a number:"))

try:
    res=int(num1)/int(num2)
except (ZeroDivisionError,ValueError):
    print("Exception handled by Manohar")

except Exception as ob:
    print(ob)
else:
    print(num1,'/',num2, '=',res)
finally:
    print('Thanks')

print("Visit again at python class at MTICA")
