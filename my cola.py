while True:
    date=input(str('enter the date:'))
    total1=0
    total2=0
    while True:
        while True:
            try:
                a=input(str('shop name:'))
                d=open((a+'.txt'),'r+')
            except FileNotFoundError:
                print('file not found')
                print(total1,total2)
            else:
                break
        b=input(str('paid or buy:'))
        if b=='paid':
            c=input(str('amount:'))
            for line in d:
                e=line
         
            d.write('\n')
            d.write(date)
            total1=total1+int(c)
            d.write('\t')
            d.write('paid   Rs ')
            d.write(c)
            d.write('\n')
            d.write('due amount Rs')
            d.write('\n')
            d.write(str(int(e)-int(c)))
            d.close()
        elif b=='buy':
            c=input(str('amount:'))
            for line in d:
                e=line
            
            d.write('\n')
            d.write(date)
            d.write('\t')
            d.write('bought Rs ')
            total2=total2+int(c)
            d.write(c)
            d.write('\n')
            d.write('due amount Rs')
            d.write('\n')
            d.write(str(int(e)+int(c)))
            d.close()
        elif b=='exit':
            break
        else:
            d.close()
            print('invalid command')
        
        
