x = int(input('Number of subjects'))
a=[]
for i in range(1,x+1):
    print('subjects',i)
    a1=input('subject (1-7 charcters) :')
    a2=float(input('credit (0.00-12.00) (cradits:)'))
    print("A,Excellent,4.0")
    print("B+,Good,3.5")
    print("B,Good,3.0")
    print("C+,Fair,2.5")
    print("C,Fair,2.0")
    print("D+,Poor,1.5")
    print("D,Poor,1.0")
    print("F,Fall,0.0")
    aa=input()
    if aa=='A'or aa=='a':
        aa=4.0
    elif aa=='B+'or aa=='b+':
        aa=3.5
    elif aa=='B' or aa=='b':
        aa=3.0
    elif aa=='C+'or aa=='c+':
         aa=2.5
    elif aa=='C'or aa=='c':
        aa=2.0
    elif aa=='D+'or aa=='d+':
        aa=1.5
    elif aa=='D'or aa=='d':
        aa=1.0
    elif aa=='F'or aa=='f':
        aa=0
    a.append([a1,a2,aa])
    
print("summary Data")
print("Number Subject Credit Grade")
total1=0
total2=0
for i in range(x):
    print(a[i][0],a[i][1],a[i][2])
    total1=total1+a[i][1]*a[i][2]
    total2=total2+a[i][1]
   
print("GPA = %.2f" %(total1/total2))


        
          
