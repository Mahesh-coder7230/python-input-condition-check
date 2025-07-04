a1=int(input("Enter No1:"))
a2=int(input("Enter No2:"))
a3=int(input("Enter No3:"))
a4=int(input("Enter No4:"))
if(a1>a2 and a1>a3 and a1>a4):
    print("No.1 is greater",a1)
elif(a2>a1 and a2>a3 and a2>a4):
    print("No.2 is greater" ,a2)
elif(a3>a2 and a3>a1 and a3>a4):
    print("No.3 is greater" ,a3)
elif(a4>a2 and a4>a3 and a4>a1):
    print("No.4 is greater" ,a4)

username=input("Enter your username ")   
if(len(username)<10):
    print("SHort")
else:
    print("OK NICE")
