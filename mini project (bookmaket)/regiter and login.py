def login():
    with open(r"D:\mini project (bookmaket)\Data\meber\meber.txt",mode='r') as login:
        Login = False
        while not(Login):
            username=input("ID       : ")
            login.seek(0,0)
            for line_login in login:
                i=line_login.strip()
                if username == i.split("|")[1]:
                    password=input("Password : ")
                    if password == i.split("|")[2]:
                        Login=True
                        print("Hi! ",i.split("|")[3])
                        break
                    else:
                        break
            if not(Login):
                print("username or password wrong. plase input your username agin ")
    pass
            
def regiter():
    with open(r"D:\mini project (bookmaket)\Data\meber\meber.txt",mode='a') as regiter:
        username=''
        password=''
        while(True):
            username=input("username input:")
            password=input("password input:")
            namecreate=input("name         :")
            if '|' in username or '|' in password or '|' in namecreate:
                print("your input don't have chareter { | } \n pleas input agin")
                continue
            for line_regiter in regiter:
                i=line.strip()
                if username == i.split("|")[1]:
                    print("Don't use this username ")
                    continue
            number_meber=open(r"D:\mini project (bookmaket)\Data\meber\number_meber.txt",mode='r')
            old_meber=number_meber.readline()
            old_meber=int(old_meber)+1
            number_meber.close()
            number_meber=open(r"D:\mini project (bookmaket)\Data\meber\number_meber.txt",mode='w')
            number_meber.write("%07d"%(old_meber))
            number_meber.close()
            regiter.write("%07d|%s|%s|%s\n"%(old_meber,username,password,namecreate))
            print("regiter Succeed ")
            break
        
                
            
                
                