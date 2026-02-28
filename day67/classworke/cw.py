

def new_list(list_num):
    sum = 0
    for i in list_num:
        sum += i * i 
    return sum

print(new_list([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))



                                                                                                                        

def list1(num):
    list2 = ["Gio","goga","Nika","data","ilia"]
    amout = 0
    for i in list2:
        if len(i) >= 4 and i == i.capitalize():
            amout += 1
    return amout * num

print(list1(5))



                                                                                                                        

def changelist(string1):
    word = ""
    for i in string1:
        if i not in "aeiouAEIOU":
            word += i.upper()
    return word

print(changelist("my name is anton"))






