
names = ["goga","irakli","saba","irma"]

new_list =[]


for i in range(0,len(names)):
    new_list.append(names[i])

print(new_list)


                                                                                                                        


names1 = ["goga","irakli","saba","irma"]

new_list1 =[]


for i in names1:
    new_list1.append([i])



                                                                                                                        



names2 = ["goga","irakli","saba","irma"]

new_list2 =[]


for i in names2:
    if i [0] == "g":
        new_list2.append(i)

print(new_list2)


                                                                                                                        
                                                                                                                        

#amatebs elements

names3 = ["goga","irakli","saba","irma"]

names3.insert(2,"gegi")


                                                                                                                        

#shlis elements siidan

names4 = ["goga","irakli","saba","gio","irma","saba","kote","naniko","ia"]

for i in range(len(names4)-1,-1,-1):
    if i % 2 == 0:
        names4.remove(names4[i])
print(names4)



                                                                                                                        


names = ["masha", "liza", "luka", "nuca", "nana", "qeta", "mariami"]

for i in names:          
    if len(i) > 5:          
        names.remove(i)  

print(names)












