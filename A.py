def HOME():
    print("1-คณิตศาสตร์")
    print("2-ภาษาไทย")
    print("3-วิทยาศาตร์")
    selet=int(input("***กรุณาเลือกหมวดหนังสือ***\n"))
    if selet==1:
        print(">1.1-แคลคลูลัส    "+"ราคา"+"เล่มละ250"+"บาท")
        print(">1.2-สถิติ        "+"ราคา"+"เล่มละ180"+"บาท")
        print(">1.3-สมการ      "+"ราคา"+"เล่มละ125"+"บาท")
        print("กลับสู่เมนูหลักกดเลข "+"0")
        a=int(input())
        if a in (0,1,2,3):
            if a==0:
                HOME()
        else :
            print("คุณทำรายการไม่ถูกต้อง // กรุณาทำรายการใหม่")
            eletmath=input("Please your mamber")
    elif selet==2:
        print(">2.1-วรรณคดี      "+"ราคา"+"เล่มละ125"+"บาท")
        print(">2.2-ลำนำ        "+"ราคา"+"เล่มละ125"+"บาท")
        print(">2.3-หลักภาษา     "+"ราคา"+"เล่มละ125"+"บาท")
        print("กลับสู่เมนูหลักกดเลข "+"0")
        a=int(input())
        if a in (0,1,2,3):
            if a==0:
                HOME()
        else :
            print("คุณทำรายการไม่ถูกต้อง // กรุณาทำรายการใหม่")
            seletthai=input("Please your mamber")
    elif selet==3:
        print(">3.1-ชีววิทยา       "+"ราคา"+"เล่มละ125"+"บาท")
        print(">3.2-ฟืสิกส์        "+"ราคา"+"เล่มละ125"+"บาท")
        print(">3.3-เคมี         "+"ราคา"+"เล่มละ125"+"บาท")
        print("กลับสู่เมนูหลักกดเลข "+"0")
        a=int(input())
        if a in (0,1,2,3):
            if a==0:
                HOME()
        else :
            print("คุณทำรายการไม่ถูกต้อง // กรุณาทำรายการใหม่")
            seletsci=input("Please your mamber")
    else :
        print("คุณทำรายการไม่ถูกต้อง // กรุณาทำรายการใหม่")
    
    
    
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

    


