import pymysql

conn = pymysql.connect(host='localhost',
user='root',
password='root',
db='game')

print('Do you want to play the new game?', end=' ')
print('Enter Y for Yes & N for No')
your_choice=input('Enter Your Choice: ')
if your_choice=='Y':
    try:
        name=input('Enter your name')
        
        result,chances,cout=0,1,0
        global w,x,y,z
        list_num=[]
        list_guess=[]
        
        import datetime

        start_time=datetime.datetime.now()
        
                
        def comp(num):
            
            a=math.floor(num/1000)
            b=math.floor((num-1000*a)/100)
            c=math.floor((num-100*(10*a+b))/10)
            d=math.floor(num-10*(100*a+10*b+c))
            list_num.append(a)
            list_num.append(b)
            list_num.append(c)
            list_num.append(d)
            
            
        
        def choice(guess):
                
            w=math.floor(guess/1000)
            x=math.floor((guess-1000*w)/100)
            y=math.floor((guess-100*(10*w+x))/10)
            z=math.floor(guess-10*(100*w+10*x+y))
            list_guess.append(w)
            list_guess.append(x)
            list_guess.append(y)
            list_guess.append(z)
            print(list_guess)
            
        def score():
            global cout
            for i in range(0,4):
                if list_num[i]==list_guess[i]:
                    print('+',end=' ')
                    cout=cout+4
                elif list_num[i] in list_guess and list_num[i]!=list_guess[i]:
                    print('-',end=' ')
                    cout=cout+1
                else:
                    print('#',end=' ')
                    cout=cout-1
        import random
        num=random.randrange(1000, 10000)
        import math
        comp(num)
        value=int(input("Guess the num between 1000 to 10000:" ))
        choice(value)
        
        
        while chances>0:
            
            if num==value:
                print('congratulation you win')
                cout=cout+10
                end_time=datetime.datetime.now()
                samay=end_time-start_time
                samay=samay.total_seconds()
                print('My num by computer was', num)
                print('Your final score is:',cout)    
                print('Total',chances ,'chances you took to guess')
                
                print('time you took',samay)
                break    
            else:
                score()
                print('your score is: ', cout)
                list_guess=[]
                value=int(input("Guess the num between 1000 to 10000:" ))
                choice(value)
                chances=chances+1
            
        
    except:
        print('some problem in inserting')
        
else:
    print('Thankyou')
    
cursor=conn.cursor()
if chances<5 :
    result=cout*2
elif chances>5 and chances<10:
    result=cout
else:
    result=cout//2
                
cursor.execute("INSERT INTO project VALUES('{}',{},{},{},{})".format(name,chances,samay,cout,result))
conn.commit()
    

