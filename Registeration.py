fname=""
p=""

def reg():
    global fname
    global p
    fname=input('Enter First Name:')
    Lname=input('Enter Last name:')
    Age=int(input('Enter Age:'))
    pwd=int(input('Enter password:'))
    a=str(Age)
    p=str(pwd)
    f=open('login.txt','a')
    #f=open('login.txt','w')
    f.write(fname)
    f.write(Lname)
    f.write(a)
    f.write(p)
    f.close()
    print('data enter successfully')



def login():
   
    finame=input('Enter name:')
    pawd=int(input('Enter password:'))
    q=str(pawd)         
    #f.read('login.txt','r')   
    if finame==fname and p==q:
       print('Correct!')
    else:
       print('Fail')


while True:
    print('1.Register')
    print('2.Login')
    print('3.Exit')
    choice=int(input('Enter choice 1 or 2:'))
    
    if choice==1:
        reg()
    elif choice==2:
        login()
    elif choice==3:
        print('Exit')
        break
    else:
        print('Wrong Choice')

    
