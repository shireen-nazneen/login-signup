def strong_password(password1):
    if len(password1)>=8:
        if "a" in password1 or "b" in password1 or "c" in password1 or "d" in password1  or "e" in password1 or "f" in password1 or "g" in password1 or "h" in password1 or "i" in password1  or "j" in password1 or"k" in password1 or "l" in password1 or "m" in password1 or"n" in password1 or "o" in password1 or "p" in password1 or "q" in password1 or"r" in password1 or "s" in password1 or "t" in password1 or "u" in password1 or"v" in password1 or "w" in password1 or "x" in password1 or "y" in password1 or "z" in password1:
            if "A" in password1 or "B" in password1 or "C" in password1 or "D" in password1  or "E" in password1 or "F" in password1 or "G" in password1 or "H" in password1 or "I" in password1  or "J" in password1 or"K" in password1 or "L" in password1 or "M" in password1 or"N" in password1 or "O" in password1 or "P" in password1 or "Q" in password1 or"R" in password1 or "S" in password1 or "T" in password1 or "U" in password1 or"V" in password1 or "W" in password1 or "X" in password1 or "Y" in password1 or "Y" in password1:
                if "0" in password1 or "1" in password1 or "2" in password1 or "3" in password1 or "4" in password1 or "5" in password1 or "6" in password1 or "7" in password1 or "8" in password1 or "9" in password1:
                    if "@" in password1 or "#" in password1 or "_" in password1  or "$" in password1:
                        return (True)
                    else:
                        return ("you neend to aad one special")
                else:
                    return ("you neend to add one number")
            else:
                return ("you neend to add atlist one capital letter")
        else:
            return ("you neend to add  small letters")
    else:
        return ("your len should be graterthan or equal to 8")
def asking_password():
    i=0
    while True:
        password1=input("enter password------")
        password2=input("re enter password-----")
        if password1==password2:
            result=strong_password(password1)
            if result==True:
                return password1
            else:
                print(result)
                continue
        else:
            print("yor both password sholud be same")
            continue
import json
def readJsonFile(fileName,user_name):
    with open(fileName,"r") as f:
        data=json.load(f)
        list_user=data["user"]
        for i in list_user:
            if user_name == i['name']:
                return True
        return data
def user_exsist(fileName):
    with open(fileName,"r") as f:
        data=json.load(f)
        list_user=data["user"]
        for i in list_user:
            if user_name == i['name'] and password==i["password"]:
                return True
        return False
def writejsonFile(fileName,dataTowrite):
    with open(fileName,"w") as f:
        json.dumps(dataTowrite)
        json.dump(dataTowrite,f,indent=4)
def printing_detials(dic1):
    for i,j in dic1.items():
        if i=="name":
            print(i,":",j)
        if i=="profile":
            a=dic1[i]
            for k,l in a.items():
                print(k,":",l)
user1=input("enter login or singup for singup  press 1 and for  login press 2")
if user1=="1":
    user_name=input("enter your name,,,,,")
    password=asking_password()
    dic1={"name":user_name,"password":password}
    dataFromJson=readJsonFile("data.json",user_name)
    if dataFromJson == True:
        print("alrady exsist")
    else:
        dic1={"name":user_name,"password":password}
        print(user_name," congract you singup secesesfully")
        dataFromJson=readJsonFile("data.json",user_name)
        description=input("enter description------")
        dob=input("enter  your Dob day/month/year-----")
        hobbies=input("enter  your hobbies-----")
        gender=input("enter your gender------")
        dic2={"description":description,"Dob":dob,"hobbies":hobbies,"gender":gender}
        dic1.update({"profile":dic2})
        dataFromJson["user"].append(dic1)
        dataToJson=writejsonFile("data.json",dataFromJson)
        printing_detials(dic1)
elif user1=="2":
    user_name=input("enter user name------")
    password=input("enter password------")
    userexsit=user_exsist("data.json")
    if userexsit==True:
        print(user_name,"your login sucsessfully")
    else:
        print("user is not exsist")
else:
    print("invalid input")
    


            
        