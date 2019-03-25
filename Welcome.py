def HOME():
    global total
    clear()
    print("1-คณิตศาสตร์")
    print("2-ภาษาไทย")
    print("3-วิทยาศาตร์")
    selet=int(input("***กรุณาเลือกหมวดหนังสือ***\n"))
    if selet==1:
        print(">1.1-แคลคลูลัส    "+"ราคา"+"เล่มละ250"+"บาท")
        print(">1.2-สถิติ        "+"ราคา"+"เล่มละ180"+"บาท")
        print(">1.3-สมการ      "+"ราคา"+"เล่มละ125"+"บาท")
        print("กลับสู่เมนูหลักกดเลข "+"0")
        a=float(input())
        if a==0:
            HOME()
        elif a==1.1:
            number=int(input("จำนวนที่ต้องการ(เล่ม) :"))
            total=total+number*250
            meber.append(["แคลคลูลัส ",250,number])
        elif a==1.2:
            number=input("จำนวนที่ต้องการ(เล่ม) :")
            total=total+number*180
            meber.append(["สถิติ ",180,number])
        elif a==1.3:
            number=input("จำนวนที่ต้องการ(เล่ม) :")
            total=total+number*125
            meber.appden(["สมการ ",125,number])
            
        else :
            print("คุณทำรายการไม่ถูกต้อง // กรุณาทำรายการใหม่")
            eletmath=input("Please your mamber")
    elif selet==2:
        print(">2.1-วรรณคดี      "+"ราคา"+"เล่มละ269"+"บาท")
        print(">2.2-ลำนำ        "+"ราคา"+"เล่มละ200"+"บาท")
        print(">2.3-หลักภาษา     "+"ราคา"+"เล่มละ127"+"บาท")
        print("กลับสู่เมนูหลักกดเลข "+"0")
        a=float(input())
        if a==0:
            HOME()
        elif a==2.1:
            number=input("จำนวนที่ต้องการ(เล่ม) :")
            total=total+number*269
            meber.appden(["วรรณคดี ",269,number])
        elif a==2.2:
            number=input("จำนวนที่ต้องการ(เล่ม) :")
            total=total+number*200
            meber.appden(["ลำนำ ",200,number])
        elif a==2.3:
            number=input("จำนวนที่ต้องการ(เล่ม) :")
            total=total+number*127
            meber.appden(["หลักภาษา ",127,number])
        else :
            print("คุณทำรายการไม่ถูกต้อง // กรุณาทำรายการใหม่")
            seletthai=input("Please your mamber")
    elif selet==3:
        print(">3.1-ชีววิทยา       "+"ราคา"+"เล่มละ175"+"บาท")
        print(">3.2-ฟิสิกส์        "+"ราคา"+"เล่มละ326"+"บาท")
        print(">3.3-เคมี         "+"ราคา"+"เล่มละ169"+"บาท")
        print("กลับสู่เมนูหลักกดเลข "+"0")
        a=float(input())
        if a==0:
            HOME()
        elif a==3.1:
            number=input("จำนวนที่ต้องการ(เล่ม) :")
            total=total+number*175
            meber.appden(["ชีววิทยา ",175,number])
        elif a==3.2:
            number=input("จำนวนที่ต้องการ(เล่ม) :")
            total=total+number*326
            meber.appden(["ฟิสิกส์ ",326,number])
        elif a==3.3:
            number=input("จำนวนที่ต้องการ(เล่ม) :")
            total=total+number*169
            meber.appden(["เคมี ",169,number])
        else :
            print("คุณทำรายการไม่ถูกต้อง // กรุณาทำรายการใหม่")
            seletsci=input("Please your mamber")
    else :
        print("คุณทำรายการไม่ถูกต้อง // กรุณาทำรายการใหม่")
    
    
    
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

    



