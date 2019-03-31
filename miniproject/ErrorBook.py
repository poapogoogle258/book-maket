def addbook(name,group,price,desrtion='-'):
    global book
    global allgroup
    newbook=[name,group,price,desrtion]
    book.append(newbook)
    allgroup.add(group)
    
def Rebook(num,number):
    global rebook
    global bookgroup
    new_book=list()
    new_book.extend(bookgroup[num-1].copy())
    new_book.append(number)
    rebook.append(new_book)

def showdesrtion(book):
    if book[3] == '-':
        pass
    else:
        print("-"*50)
        print(book[3])

def regiter():
    username =''
    password =''
    name =''
    localtion=''
    
    while True:
        username =input('username :')
        password =input('password :')
        name =input("name :")
        print("กรอกข้อมูลตามตัวอย่าง ชื่อนายเบิดร์ 67/2หมู่3 บ.นกน้อย ต.แม่กา อ.แม่กา จ.พะเยา เบอร์โทรศัพท์ อีเมล รหัสไปรษณีย์ ")
        localtion=input("localtion :")
        if '|' in username or "|" in password or "|" in name or '|' in localtion:
            print("Don't have (|) in data")
            continue
        with open("login\\login.txt",mode='r') as login:
            for i in login:
                i=i.strip()
                if i != "":
                    if username == i.split("|")[0]:
                        print("plean input new username")
                        break
            else:
                #check data angin
                print("Check data have to True")
                print(username)
                print(password)
                print(name)
                print(localtion)
                check=''
                while True:
                    check =input("(y / n)")
                    if check in {'y','n'}:
                        break
                if check == 'y':
                    break
                else :
                    continue
    with open("login\\login.txt",mode='a') as login:
        login.write("%s|%s|%s|%s\n"%(username,password,name,localtion))
    #creat usernewfoder
    path='user\\'+username    
    os.mkdir(path)
    
    pathlocaltion=path+"\\localtion.txt"
    with open(pathlocaltion,mode='w')as f:
        f.write(localtion)
    pathnumlogin=path+"\\numlogin.txt"
    with open(pathnumlogin,mode='w')as f:
        f.write("0")
    pathnumlogin=path+"\\sale.txt"
    with open(pathsale,mode='w')as f:
        f.write("0")
    #endregiter()
    
def login():
    global user
    global localtion
    global username
    global point
    while True:
        username=input("Username  :")
        with open(r"login\login.txt",mode='r') as f:
            for i in f:
                i=i.strip()
                if i != '':
                    if username == i.split('|')[0]:
                        password=input("Password  :")
                        if password == i.split('|')[1]:
                            user = i.split("|")[2]
                            
                            num=0
                            with open(r"user\%s\numlogin.txt"%(username),mode='r')as ff:
                                num=ff.readline()
                            with open(r"user\%s\numlogin.txt"%(username),mode='w')as ff:
                                ff.write(str(int(num)+1))
                            with open(r"user\%s\sale.txt"%(username),mode='r')as ff:
                                point=ff.readline()
                                point=float(point)+1.5
                            with open(r"user\%s\localtion.txt"%(username),mode='r')as ff:
                                localtion=ff.readline()
                            checkpoint(username,int(num)+1)
                            
                            break
                                
                            
            else:
                print("!! No this uesrname !!")
                continue
            break
        
def checkpoint(username,num):
    # point sale
    global point
    data=[10,19,50,100,300,750,1999]
    data2=[5,10,20,35,100,170,200]
    newnum =0
    for i in range(len(data)):
        if int(num) == data[i]:
            newnum = newnum + data2[i]
            break
    point = point + newnum
    with open(r"user\%s\sale.txt"%(username),mode='w')as ff:
        ff.write("%f"%(point))
            

                
def setbook(group):
    global book
    global bookgroup
    bookgroup =[]
    for i in range(len(book)):
        if book[i][1] == group:
            bookgroup.append(book[i].copy())


def inputtest(inbox,*a):
    while True:
        data = input(inbox)
        for i in a:
            if data == str(i):
                return i
        print("กรุณาใส่ข้อมูลออีกครัง")

def promotion():
    global point
    global sale
    global codesale
    global total
    global printsale
    global uesrname
    global usepoint
    if printsale != '-':
        print("ส่วนลดของคุณตอนนี้คือ :",printsale)
        print("ลดไปทั้งหมด :",sale)
    test1=["ส่วนลนค่าจัดส่ง 35 บาท",
           "ค่าหนังสือทั้งหมดลด 10 % (ไม่รวมค่าจัดส่ง)",
           "ต่าหนังสือทั้งหมดลดลง 79 บาท",
           "ค่าหนังสือทั้งหมดลดลด 100 บาท",
           "ค่าหนังสือทั้งหมดลดลง 25 %(ไม่รวมค่าจัดส่ง)",
           "ค่าหนังสือทั้งหมดลดลง 35 %(ฟรีค่าจะส่ง)"]
    test2=[30,50,100,120,300,500]
    if codesale :
        for i in range(len(test1)):
            print(str(i+1)+")\t",test1[i],"\tpoint",test2[i])
        print("ยกเลิกส่วนลดกด -1\nต้องการกลับกด 0")
        while True:
            checkcode =inputtest("Point : %s point\nกรุณาใส่เลือกส่วนลดตามแต้มของคุณ"%(point),1,2,3,4,5,6,-1,0)
            if checkcode == 0:
                return 0
            elif checkcode ==1:
                if point < test2[checkcode-1]:
                    continue
                sale = 35
                printsale = test1[checkcode-1]
            elif checkcode ==2:
                if point < test2[checkcode-1]:
                    continue
                sale = total*0.1
                printsale = test1[checkcode-1]
            
            elif checkcode ==3:
                if point < test2[checkcode-1]:
                    continue
               
                sale = 79
                printsale = test1[checkcode-1]
            elif checkcode ==4:
                if point < test2[checkcode-1]:
                    continue
                
                sale = 100
                printsale = test1[sheckcode-1]
            
            elif checkcode ==5:
                if point < test2[checkcode-1]:
                    continue
                sale = total*0.25
                printsale = test1[checkcode-1]
            
            elif checkcode ==6:
                if point < test2[checkcode-1]:
                    continue
                sale = total*0.35+35
                printsale = test1[checkcode-1]
            elif checkcode == -1:
                printsale='-'
                sale=0
                usepoint=0
                
            ###########################################
            usepoint=test2[checkcode-1]
            print("ส่วนลดของคุณตอนนี้คือ :",printsale)
            print("ลดไปทั้งหมด :",sale,"บาท")
            
            
            
    else:
        print("คุณใช่แต้มส่วนลดไปแล้ว ไม่สามารถเปลียยแปลงได้")


def pay() :
    global rebook
    global total
    global user
    global localtion
    global point
    global sale
    global codesale
    global total
    global printsale
    global username
    total=0
    
    
    
    
    if len(rebook) == 0:
        print("Don't have list now")
        return 0
    print("list","Name book","Group book","price","number","almout")
    for i in range(len(rebook)):
        print("{} {:18}{:18}{:5d}{:5d}{:>5.2f}".format(i+1,rebook[i][0],rebook[i][1],rebook[i][2],rebook[i][4],float(float(rebook[i][2])*float(rebook[i][4]))) )
        total += float(float(rebook[i][4])*float(rebook[i][2]))
    print("ค่าจัดส่ง 35 บาท")
    print("โค้ดส่วนลดราคา :",printsale,"ลดทั้งหมด :",sale,"บาท")
    print("almout :: ",total+35-sale," bath.")
    
        
    
    
    print("***กดเพื่อ1ชำระเงินปลายทาง***,***กด2เพื่อชำระเงินผ่านธนาคาร***,***กด 0 เพื่อต้องการกลับไปหน้่าเลือกหนังสือ***")
    aa=inputtest("กรุณากรอกหมายเลขเพื่อเลือกวิธีจัดส่ง",1,2,0)
    if aa==1 :
        print("***คุณกำลังทำรายการชำระเงินปลายทางปลายทาง***")
        print("กรอกข้อมูลตามตัวอย่าง ชื่อนายเบิดร์ 67/2หมู่3 บ.นกน้อย ต.แม่กา อ.แม่กา จ.พะเยา เบอร์โทรศัพท์ อีเมล รหัสไปรษณีย์ ")
        print(localtion)
        checklocaltion = inputtest("ที่อยูของคุนถูกต้องหรือไป (y/n):",'y','n')
        if checklocaltion =='y':
            pass
        else:
            while True:
                print("กรอกข้อมูลตามตัวอย่าง ชื่อนายเบิดร์ 67/2หมู่3 บ.นกน้อย ต.แม่กา อ.แม่กา จ.พะเยา เบอร์โทรศัพท์ อีเมล รหัสไปรษณีย์ ")
                newdata = input("กรุณากรองที่อยู่ที่รับสินค้า")
                checkdata = inputtest("%s\nทีอยู่ของคุณถูกต้องใช้หรือไม่(y/n):"%newdata,'y','n')
                if checkdata == 'y':
                    break
                elif checkdata =='n':
                    continue
                       
            with open(r"user\%s\localtion.txt"%(username),mode='w')as Newdata:
                Newdata.writelines(newdata)
                localtion=newdata
                
        with open("list.txt",mode='a')as list_price:
                list_price.write("%d\n"%(total+35-sale))
                list_price.writelines(localtion)
                for i in rebook:
                    list_price.write("\t%s|%s|%s|%s\n"%(i[0],i[1],i[2],i[4]))
        print("%d + ค่าจัดส่ง 35 บาท ส่วนลด %d  บาท รวบเป็นเงิน %d"%(total,sale,total+35-sale))
        print("คุณทำรายการเสร็จสิ้นแล้ว ระบบกำลังทำรายการส่ง Thank you")
        
    elif aa==2 :
            print("***คุณกำลังทำรายการชำระเงินผ่านทางธนาคาร***")
            print("***แสดงหลักฐานการโอนหรือใบสลิป (เลขที่รายการ)***")
            print("ธนาคาร กสิกรไทย บัญชี 123-4-5678-9 ชื่อบัญชี Error" )
            print("กรอกข้อมูลตามตัวอย่าง ชื่อนายเบิดร์ 67/2หมู่3 บ.นกน้อย ต.แม่กา อ.แม่กา จ.พะเยา เบอร์โทรศัพท์ อีเมล รหัสไปรษณีย์ ")
            print(localtion)
            checklocaltion =inputtest("ที่อยูของคุนถูกต้องหรือไป (y/n):",'y','n')
            if checklocaltion =='y':
                pass
            else:
                while True:
                    newdata = input("กรุณากรองที่อยู่ที่รับสินค้า")
                    checkdata = inputtest("%s\nทีอยู่ของคุณถูกต้องใช้หรือไม่(y/n):"%newdata,'y','n')
                    if checkdata == 'y':
                        break
                    elif checkdata =='n':
                        continue
                       
                with open(r"user\%s\localtion.txt"%(username),mode='w')as Newdata:
                    Newdata.write(newdata)
                    localtion=newdata
            checknumber=''
            while True:
                checknumber=input("กรุณากรองเลขใบเสร็จของท่าน :")
                if len(checknumber)==15:
                    break
            
            with open("list.txt",mode='a')as list_price:
                list_price.write("%s|%d\n"%(checknumber,total+35-sale))
                list_price.write("%s\n"%localtion)
                for i in rebook:
                    list_price.write("\t%s|%s|%s|%s\n"%(i[0],i[1],i[2],i[4]))
                
            clear()
            print("คุณทำรายการเสร็จสิ้นแล้ว ระบบกำลังตรวจสอบการความถูกต้องแล้วจัดส่งสินค้า Thank you")
    
    elif aa==0:
        return 0
    
    #clear Data for NewData
    total =0
    rebook=[]
    prinrsale='-'
    codesale=True
    with open(r"user\%s\sale.txt"%(username),mode='w')as ff:
        ff.write("%f"%(point-usepoint))
            

            


## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ##
 ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ##

import os
clear = lambda : os.system("cls")
book=[]
bookgroup=[]
allgroup=set()
rebook=[]
sale=0
usepoint=0
point=0
codesale=True
printsale='-'
user=''
localtion=''
total=0
username=''

#
# DegineBook addbook(namebook,groupbook,pricebook)
#
addbook("คู่มือพัฒนาแอพพลิเคชันด้วย Android Studio","บริหาร ธุรกิจ",331)
addbook("คเณิร์ตศาสตร์","บริหาร ธุรกิจ",175)
addbook("Big Data Series III","บริหาร ธุรกิจ",342)
addbook("เศรษฐกิจโลกกับเทคโนโลยี","บริหาร ธุรกิจ",295)
addbook("ลงทุนแมน 9.0","บริหาร ธุรกิจ",297)
addbook("เปิดร้านให้ได้เงินล้านบน Facebook","บริหาร ธุรกิจ",247)
addbook("รู้ทันสันดานคน","ปรัชญา",165)
addbook("ปรัชญาสุภาษิตแห่งชีวิต","ปรัชญา",95)
addbook("เกร็ดเทพเจ้าจีน","ปรัชญา",280)
addbook("ปัญญาญาณ INTUITION","ปรัชญา",208)
addbook("เดินสมาธิ walk","ปรัชญา",208)
addbook("find your way! พิชิตเกมสุดมันในเขาวงกต : ผจญภัยโลกใต้ดิน","หนังสือเด็กน้อย",80)
addbook("find your way! พิชิตเกมสุดมันในเขาวงกต : ผจญภัยในป่าใหญ่","หนังสือเด็กน้อย",80)
addbook("find your way! พิชิตเกมสุดมันในเขาวงกต : ผจญภัยใต้ทะเล","หนังสือเด็กน้อย",80)
addbook("find your way! พิชิตเกมสุดมันในเขาวงกต : ผจญภัยในอวกาศ","หนังสือเด็กน้อย",80)
addbook("หมีน้อยคิดเองทำเองเก่งจัง","หนังสือเด็กน้อย",108)
addbook("เก่งอังกฤษ พิชิต GRAMMAR + แบบฝึกหัด","คู่มือเตรียมสอบ",211)
addbook("ฝ่าด่านโจทย์คณิต พิชิต TCAS","คู่มือเตรียมสอบ",329)
addbook("Lecture สรุปเข้มเคมี ม.ปลาย","คู่มือเตรียมสอบ",177)
addbook("Hack โจทย์ 9 วิชาสามัญ ฟิสิกส์ ม.ปลาย","คู่มือเตรียมสอบ",254)
addbook("สวนสัตว์กระดาษ","วรรณกรรม",280)
addbook("I Decided to Live as Myself","วรรณกรรม",271)
addbook("Practicing Happiness","วรรณกรรม",279)
addbook("Thanks to Me","วรรณกรรม",237)
addbook("Generation of Hopelessness","วรรณกรรม",208)
addbook("เพลงปลอบขวัญ","นิยายโรแมนติก",79)
addbook("มาลี รติกานต์ ชุด ดอกไม้ลายพยัคฆ์","นิยายโรแมนติก",279)
addbook("อมฤต","นิยายโรแมนติก",340)
addbook("โสเภณีเดียงสา","นิยายโรแมนติก",274)
addbook("ล้วงรักจอมวายร้าย","นิยายโรแมนติก",135)


#
allgroup=list(allgroup)
while True:#login
    while True:#login page 
        test=input("you have Username (y/n):")
        if test =='y':
            login()
            break
        elif test =='n':
            regiter()
        else:
            print("??")
    
    print("login BY:",user,"!!")
    while True:# Main mune
        clear()
        input1=0
        checklogin=False
        fcheck =inputtest("กรุณาเลือกรายทำ\n1.)เลือกหมวดหมู่หนังสือ \n2.)กำหนดส่วนลด\n3.)ชำละรายการสั้งชื่อหนังสือ %s รายการ\n4.)ยกเลิกรายการทั้งหมดแล้วกลับหน้า login\n"%(len(rebook)),1,2,3,4)
        if fcheck == 1:
            pass
        elif fcheck == 2 :
            promotion()
            continue
        elif fcheck == 3 :
            pay()
            continue
        elif fcheck == 4:
            checklogin = True
            
        if checklogin:
            break
        
        while True: # loop select number group
            #memu Group
            for i in range(len(allgroup)) :
                print(str(i+1)+"),",allgroup[i])
            input1=input("ถ้าต้องการกลับหน้าหลักกรูณากด 0\nกรุณาใส่เลขหมวดหมู่ต้องการ :")
            if input1 == '0':
                checklogin = True
                break
            elif input1 in [str(x) for x in range(1,len(allgroup)+1)]:
                #### Setbook new ###
                input1 = int(input1)
                setbook(allgroup[input1-1])
                while True: # loop select number book of groupbook
                    print("หมวดหนังสือหน้านี้ :",allgroup[input1-1])
                    for i in range(len(bookgroup)):
                        print("%d) Name: %s Price: %s"%(i+1,bookgroup[i][0],bookgroup[i][2]))
                    input2=0
                    check3 = False
                    try:
                        input2=int(input("ถ้าต้องการกลับไปเมนูเลือกหมวดหมู่หนังสือกดเลข 0 \nกรุณาเลือกหมายเลขหนังสือ :"))
                    except ValueError:
                        print("กรูณากรอกข้อมูลใหม่")
                        continue
                        
                    if input2 == 0:
                        break

                    elif input2 in range(1,len(bookgroup)+1):
                        print("name angin:","%d)\t Name: %s \tPrice: %s"%(input2,bookgroup[input2-1][0],bookgroup[input2-1][2]))
                        check1=True
                        while True: # loop select rebook(numberbook of group)
                            check =input("ถ้าต้องการกลับไปเมนูเลือกหมวดหมู่หนังสือกดเลข 0 \nกรุณาเลือกจำนวนหนังสือที่ต้องการ(เล่ม) :")
                            if int(check) == 0:
                                check1=False
                                break
                            if int(check)>0:
                                Rebook(input2,int(check))
                                break
                            else:
                                print("??")
                                continue
                        if check1 == False:
                            continue
                #endinput rebook
                continue
            else:
                print("กรูณากรองข้อมูลที่ถูกต้อง")
            
        if checklogin:
            continue
        
        
        

        
                
        
    
    

    

        
            
                    
    
    
    
    
    
    
        
        
        
