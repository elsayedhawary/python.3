import datetime

print ("Welcone To my Progrm")
print ("1.calculet Age       2.Test")
chooeUs = input("Please choose Number of service ")
if chooeUs == "1":
    yer = input("Enter Your Yer ")
    mon = input("Enter Your Month ")
    days = input("Enter Your Day")
    yern = datetime.datetime.now().year - yer
    monn = datetime.datetime.now().month- mon
    days = datetime.datetime.now().day -  days
    print(yern)
else:
    print("j")    
