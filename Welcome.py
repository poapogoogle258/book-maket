def HOME():
    global total
    clear()
    print("1-คณิตศาสตร์")
    print("2-ภาษาไทย")
    print("3-วิทยาศาตร์")
    while True:
        selet=int(input("***กรุณาเลือกหมวดหนังสือ***\n"))
        if selet in {1,2,3}:
        break
        print("คุณทำรายการไม่ถูกต้อง // กรุณาทำรายการใหม่")
    
    if selet==1:
        print(">1.1-แคลคลูลัส    "+"ราคา"+"เล่มละ250"+"บาท")
        print(">1.2-สถิติ        "+"ราคา"+"เล่มละ180"+"บาท")
        print(">1.3-สมการ      "+"ราคา"+"เล่มละ125"+"บาท")
        print("กลับสู่เมนูหลักกดเลข "+"0")
        while True:
            a=float(input("กรุณาเลือกเมนู"))
            if a in {0,1.1,1.2,1.3}:
                break
            print("คุณทำรายการไม่ถูกต้อง // กรุณาทำรายการใหม่")
            
        if a==0:
            HOME()
        elif a==1.1:
            number=float(input("จำนวนที่ต้องการ(เล่ม) :"))
            total=total+number*250
            meber.append(["แคลคลูลัส ",250,number])
            endHOME()
        elif a==1.2:
            number=float(input("จำนวนที่ต้องการ(เล่ม) :"))
            total=total+number*180
            meber.append(["สถิติ ",180,number])
            endHOME()
        elif a==1.3:
            number=float(input("จำนวนที่ต้องการ(เล่ม) :"))
            total=total+number*125
            meber.append(["สมการ ",125,number]
            endHOME()
    elif selet==2:
        print(">2.1-วรรณคดี      "+"ราคา"+"เล่มละ269"+"บาท")
        print(">2.2-ลำนำ        "+"ราคา"+"เล่มละ200"+"บาท")
        print(">2.3-หลักภาษา     "+"ราคา"+"เล่มละ127"+"บาท")
        print("กลับสู่เมนูหลักกดเลข "+"0")
        while True:
            a=float(input("กรุณาเลือกเมนู"))
            if a in {0,2.1,2.2,2.3}:
                break
            print("คุณทำรายการไม่ถูกต้อง // กรุณาทำรายการใหม่")
            
        if a==0:
            HOME()
        elif a==2.1:
            number=float(input("จำนวนที่ต้องการ(เล่ม) :"))
            total=total+number*269
            meber.append(["วรรณคดี ",269,number])
            endHOME()
        elif a==2.2:
            number=float(input("จำนวนที่ต้องการ(เล่ม) :"))
            total=total+number*200
            meber.append(["ลำนำ ",200,number])
            endHOME()
        elif a==2.3:
            number=float(input("จำนวนที่ต้องการ(เล่ม) :"))
            total=total+number*127
            meber.append(["หลักภาษา ",127,number])
            endHOME()
    elif selet==3:
        print(">3.1-ชีววิทยา       "+"ราคา"+"เล่มละ175"+"บาท")
        print(">3.2-ฟิสิกส์        "+"ราคา"+"เล่มละ326"+"บาท")
        print(">3.3-เคมี         "+"ราคา"+"เล่มละ169"+"บาท")
        print("กลับสู่เมนูหลักกดเลข "+"0")
        while True:
            a=float(input("กรุณาเลือกเมนู"))
            if a in {0,3.1,3.2,3.3}:
                break
            print("คุณทำรายการไม่ถูกต้อง // กรุณาทำรายการใหม่")
            
        if a==0:
            HOME()
        elif a==3.1:
            number=float(input("จำนวนที่ต้องการ(เล่ม) :"))
            total=total+number*175
            meber.append(["ชีววิทยา ",175,number])
            endHOME()
        elif a==3.2:
            number=float(input("จำนวนที่ต้องการ(เล่ม) :"))
            total=total+number*326
            meber.append(["ฟิสิกส์ ",326,number])
            endHOME()
        elif a==3.3:
            number=float(input("จำนวนที่ต้องการ(เล่ม) :"))
            total=total+number*169
            meber.append(["เคมี ",169,number])
            endHOME()
       
   

def pay():
    global total
    print("***************รายการสินค้า*****************")
    for i in range(len(meber)):
        print("รายการที่",i+1,"}",meber[i][0],"ราคา",meber[i][1],"บาท","จำนวน",meber[i][2],"เล่ม", "รวมราคา",meber[i][1]*meber[i][2],"บาท")
    print("ยอดรวมทั้งหมด ",total,"บาท")
    print("ถ้าต้องการยกเลิกสินค้า กด (-1) ")
    a=int(input("ยอดเงินที่รับมา :"))
    if a== -1:
        pass
    print("เงินทอน :",total - a,"บาท")
    
def endHOME():
    while True :
        a=input("คุณต้องการทำรายการอื่นหรือไม่(y / n) : ")
        if a in {'y','Y','n','N'}:
            break
        print("กรุณาใส่ข้อมูลให้ถูกต้อง")
    if a in {'y','Y'}:
        HOME()
    else:
        pay()    
    
import os
import time
clear = lambda: os.system('cls')
color_greed= lambda : os.system('color 0a')
color_common=lambda : os.system('color 0f')
color_greed()
total =0
meber=[]
welcome1="""
      ____                    _        __  __           _             _   
     |  _ \                  | |      |  \/  |         | |           | |  
     | |_) |   ___     ___   | | __   | \  / |   __ _  | | __   ___  | |_ 
     |  _ <   / _ \   / _ \  | |/ /   | |\/| |  / _` | | |/ /  / _ \ | __|
     | |_) | | (_) | | (_) | |   <    | |  | | | (_| | |   <  |  __/ | |_ 
     |____/   \___/   \___/  |_|\_\   |_|  |_|  \__,_| |_|\_\  \___|  \__|
                                                                          
                                                                          """
welcome2="""
                              _______         
                             |__   __|        
                                | |      ___  
                                | |     / _ \ 
                                | |    | (_) |
                                |_|     \___/ 
                                              """
welcome3="""
             __          __         _                            
             \ \        / /        | |                           
              \ \  /\  / /    ___  | |   ___    ___    _ __ ___  
               \ \/  \/ /    / _ \ | |  / __|  / _ \  | '_ ` _ \ 
                \  /\  /    |  __/ | | | (__  | (_) | | | | | | |
                 \/  \/      \___| |_|  \___|  \___/  |_| |_| |_|
                                                                 
                                                     
"""
print(welcome3)
time.sleep(1)
print(welcome2)
time.sleep(1)
print(welcome1)
time.sleep(1)
clear()
color_common()
username = "e2r"
password = "123"
while(True):
    use = input('Please enter your USERNAME:')
    if use == username :
        pwd = input('Please enter your PASSWORD:')
        if pwd == password:
            print("Hello, "+username+"")
            HOME()
            
            break
    print("กรุณาใส่หรัสใหม่อีกครัง\n")

    



