date=input(str('enter the date:'))
while True:
    while True:
        try:
            a=input(str('shop name:'))
            d=open((a+'.txt'),'r+')
        except FileNotFoundError:
            print('file not found')
        else:
            break
    for lines in d:
        if lines[0:10]==date:
            print(lines)
            break
    
