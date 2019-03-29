global user
global localtion
print("***กดเพื่อ1ชำระเงินปลายทาง***,***กด2เพื่อชำระเงินผ่านธนาคาร***")
while True:
    try
        aa =int(input("กรุณาใส่ตัวเลขเพื่อกรอกข้อมูลจัดส่ง"))
        if aa in {1,2}:
            break
     except ValueError:
                print("คุณทำรายการไม่ถูกต้อง กรุณาทำใหม่อีกรอบ")
if aa==1 :
    print("***คุณกำลังทำรายการชำระเงินปลายทางปลายทาง***")
    print("กรอกข้อมูลตามตัวอย่าง ชื่อนายเบิดร์ 67/2หมู่3 บ.นกน้อย ต.แม่กา อ.แม่กา จ.พะเยา เบอร์โทรศัพท์ อีเมล รหัสไปรษณีย์ ")
    print(localtion)
    while True:
        checklocaltion =input("ที่อยูของคุนถูกต้องหรือไป (y/n):")
        if checklocaltion in {'y','n'}:
            break
    if checklocation =='y':
        pass
    else:
        while True:
            newdata = input("กรุณากรองที่อยู่ที่รับสินค้า")
            checkdata = inpur("%s\nทีอยู่ของคุณถูกต้องใช้หรือไม่(y/n):"%newdata)
            if checkdata == 'y':
                break
            elif checkdata =='n':
                continue
            else:
                print("กรุณากรองข้อมูลให้ถูกต้อง")
                   
        with open(r"user\%s\localtion.txt"%(username),mode'w')as Newdata:
            Newdata.write(newdata)
            localtion=newdata
            break
            
    print("%d+ ค่าจัดส่ง 35 บาท รวบเป็นเงิน %d"%(total,total+35))
    print("คุณทำรายการเสร็จสิ้นแล้ว ระบบกำลังทำรายการส่ง Thank you")
    
elif aa==2 :
        print("***คุณกำลังทำรายการชำระเงินผ่านทางธนาคาร***")
        print("***แสดงหลักฐานการโอนหรือใบสลิป (เลขที่รายการ)***")
        print("ธนาคาร กสิกรไทย บัญชี 123-4-5678-9 ชื่อบัญชี Error" )
        while True :
            checknumber=input("(เลขที่รายการ)")
            if len(checknumber) == 15:
                break
            else:
                print("กรุณากรองหมายเลขที่ถูกต้อง")
        print("กรอกข้อมูลตามตัวอย่าง ชื่อนายเบิดร์ 67/2หมู่3 บ.นกน้อย ต.แม่กา อ.แม่กา จ.พะเยา เบอร์โทรศัพท์ อีเมล รหัสไปรษณีย์ ")
        print(localtion)
        while True:
            checklocaltion =input("ที่อยูของคุนถูกต้องหรือไป (y/n):")
            if checklocaltion in {'y','n'}:
                break
        if checklocation =='y':
            pass
        else:
            while True:
                newdata = input("กรุณากรองที่อยู่ที่รับสินค้า")
                checkdata = inpur("%s\nทีอยู่ของคุณถูกต้องใช้หรือไม่(y/n):"%newdata)
                if checkdata == 'y':
                    break
                elif checkdata =='n':
                    continue
                else:
                    print("กรุณากรองข้อมูลให้ถูกต้อง")
                   
            with open(r"user\%s\localtion.txt"%(username),mode'w')as Newdata:
                Newdata.write(newdata)
                localtion=newdata
                break
        with openr("list.txt",mode'a')as list_price:
            list_price.write("%s|%d\n"%(checknumber,total+35))
            for i in rebook:
                list_price.write("\t%s|%s|%s"%(i[0],i[1],i[3]))
            
        print("คุณทำรายการเสร็จสิ้นแล้ว ระบบกำลังตรวจสอบการความถูกต้องแล้วจัดส่งสินค้า Thank you")

    #******* แบบว่าอยากให้ที่รับค่ามา(บรรทัศ7.13.15)เก็บค่าไว้ในลิสเป็นฐานข้อมูลไว้อ่ะ*******
    #เขียนยาวเลย

