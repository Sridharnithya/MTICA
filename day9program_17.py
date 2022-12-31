for i in range(33, -7,-5):
    if i%3==0:
        print("Yes",i)
    elif i//23==0:
        break
    elif i%4==0:
        continue
    else:
        print('No',i)
    print('Looping',i)
