
#if ში და elif ში მყოპმა პირობამ ყოველთვის უნდა დააბრუნოს True  or False
#if ის გამოყენება შეგვიძლია მხოლოდ 1 ხელ,ასევე else ის გამოყენებაც მხოლოდ ერთხელ

number = int(input("enter your number")) 

if number > 0:
    print("more then 0") 
if number < 0:
    print("less then 0")
else:
    print("equal zero")



mineral_water = input("enter mineral water")

if mineral_water =="likani":
    print("წამოვიღოთ ლიკანი")
elif mineral_water == "nabeglavi":
    print("წამოვიღოთ ნაბეღლავი")
else:
    print("წამოვიღოთ ბორჯომი")



sia = ["gio",12,True,False,50.6,["lasha",300,True]]
list1 = sia[5]

print(sia[0])
print(sia[5])
print(sia[5][1]) #ასე ვდებთ ელემენტებს ის სიაში რომელიც სხვა სიაშია მოთავსებული



#სიაში მყოპთ ელემენტებს აქვთ თავიანთი მისამართები და ამ მისამართებს index ები ეწოდება

sia1 = ["gio",12,"gushin",False,50.6,"wavida",300,True,"skolashi"]

sentenc = sia1[0] + " " + sia1[2] +" " + sia1[-1] +" "+ sia1[5] #conkantinacia

print(sentenc)




sia2 = ["gio",12,"gushin",False,50.6,"wavida",300,True,"skolashi"]

sia3 = sia2[0:3] #ე ოდესაც სლაისინგ ვიყენებთ ის ყოველთვის აბრუნებს ახალ სიას

print(sia2)


























