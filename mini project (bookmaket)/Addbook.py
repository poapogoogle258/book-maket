# about book
def AddBook(name,group,price):
    while True:
        memberID = 'pass'
        if '|' in name or '|' in group or '|' in price :
            print("you dot'n have to write | in dataBook")
            break
        try :
            with open(r"D:\mini project (bookmaket)\Data\book\number.txt",mode = 'r') as f:
                memberID = f.readline()
                memberID = int(memberID)
        except IOError :
            with open(r"D:\mini project (bookmaket)\Data\book\number.txt",mode = 'w') as f:
                memberID = 0
                f.write("%07d"%(memberID))
                print("Strat read at address 0")
        
        with open(r"D:\mini project (bookmaket)\Data\book\number.txt",mode = 'w') as f:
            f.write("%07d"%(memberID+1))
            
        file = [memberID,name,group,price]
        with open(r"D:\mini project (bookmaket)\Data\book\book.txt",mode = 'a') as f:
            f.write("%s|%s|%s|%s\n"%(memberID,name,group,price))
            
        checkGroup = True
        with open(r"D:\mini project (bookmaket)\Data\book\group.txt",mode = 'r') as f:
            try:
                for i in f :
                    if group == i.strip() :
                        checkGroup = False
                        break
            except IOError :
                print("Don't open file group.txt")
        
        if checkGroup:
            with open(r"D:\mini project (bookmaket)\Data\book\group.txt",mode = 'a') as f:
                f.write("%s\n"%(group))
            
            newgroup =(r'D:\mini project (bookmaket)\Data\book\groupbook\%s.txt'%group) 
            with open(newgroup,mode='a') as f:
                f.write("%s|%s|%s|%s\n"%(memberID,name,group,price))
        else:
            newgroup =(r'D:\mini project (bookmaket)\Data\book\groupbook\%s.txt'%group)
            with open(newgroup,mode='a') as f:
                f.write("%s|%s|%s|%s\n"%(memberID,name,group,price))
        break

def delbook(x):
    pass

def setbook(x):
    global book
    openfile=(r'D:\mini project (bookmaket)\Data\book\groupbook\%s.txt'%x)
    with open(openfile,mode='r')as f:
        after =[]
        for i in f:
            after=[]
            for j in i.split("|"):
                after.append(j)
            book.append(after)
    
def setgroup():
    global group
    with open(r'D:\mini project (bookmaket)\Data\book\group.txt',mode='r') as f:
        for i in f:
            group.append(i)
            
    
    
        
        
    