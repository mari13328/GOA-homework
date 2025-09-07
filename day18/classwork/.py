
# hi1=int(input("შეიყვანეთ პირველი რიცხვი:"))
# hi2=int(input("შიყვანეთ მეოტე რიცხვი:"))
# hi3=int(input("შეიყვანეთ მესამე რიცხვი:"))

# if hi1 == hi2:
#     print("სამივე ტოლია")
#     if hi1 == hi2:
#         print("1 და 2 ტოლია")
#     elif hi2 == hi3:
#         print("2 და 3 ტოლია")
#     else hi1 == hi2 == hi3
#      print("არცერთი არის ტოლი")



month = int(input("შეიყვანეთ რიცხვი (1-დან 12-მდე):"))

if month==12 or month==1 or month==2:
    print("ზამთარი")
elif month==3 or month==4 or month==5:
    print("გაზაპხული")
elif month==6 or month==7 or month==8:
     print("ზაფხული")
elif month==9 or month==10 or month==11:
    print("შემოდგომა")
else:
    print("არასწოეი რიცხვი შეიყვანე")




name=input("enter your name:")

if name=="admin":
    password=input("enter your password:")
    if password=="adminpassword123":
        print("სალამი ადმინ")
    else:
        print("წვდომა არ გაქვს")
else:
    print("სალამი მომხმარებელო")