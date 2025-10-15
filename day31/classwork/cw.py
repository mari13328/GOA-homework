                                                                                                                        

list1 = ["giorgi","goga","irina","saba","aleqsandre","nuca","irakli"] #mutable ---> shecvladi
                                                                    #string ---> umutable -->ucvladi
# print(list1[2])

# name ="Lina"
# list1[3]= name
# print(list1)

# list1[0:4] = ["ina","givi","nika","daviti"]
# print(list1)

# list2 = ["petre","pavle"]
# list2[0:2] = ["giorgi","goga","saba","nuca","irakli"]
# print(list2)


# print(list1 + list2)


#-------------------------------------------------------------------------------------------------------------------------


list3 = ["ina","givi","nika","daviti","ia","lizi"]
list3[0:2] = ["irina","miilana","kira"]
print(list3)

list3[4:] = ["gisa","emzari","xvicha"]

print(list3)

#=-----------------------------------------------------------------------------------------------------------------------=

number = int(input("choose any number: "))

if number > 10 and number < 20:
    print("this number is between 10 and 20")
elif number >= 20 and number < 100:
    print("this number is between 20 and 100")
elif number > 100 and number % 2 == 0:
    print("more then 100 and it is even") #Even ---> luwi
else:
    print("get out!!!")

# ლუწი რიცხვები არიაან ისეთი რიცხხვები რომლებიც უნაშთოდ იიყოპა 2-ზე ("Even")
#კენტი რიცხვები არიან ისეთი რიცხვები რომლებიც 2-ზე გაყოპისას ნაშთს გვადზლევს 1-ს ("Odd")

number2 = int(input("enter number"))

if number2 % 2 == 1:
    print("this number is Odd") #this is how we now if the number is Even
elif number % 2 == 0:
    print("this number is Even")


# print(40 != 40)























