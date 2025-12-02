

word1 = input("Enter whatewer you whant")
for i in word1:
    print(i)
    if i == "e" or i == "E":
        break




enter = input()

if "bad" in enter:
    print("akrdzaluli sityva")
else:
    print("yvelaperi rigzea")






num1 =input("give a sentence")

for i in num1:
    if i == "":
        continue
    print(i)




numm1 = int(input("Enter first number:"))

numm2 = int(input("Enter second number"))

for i in range(numm1,numm2):
    if i % 15 == 0:
        print(i)
        break





list = ["goga","liza","luka","nana"]

# len == gvibrunebs strings an siis sigrdzees

for i in range(len(4)):
    print(list[i])



#1)
list1 = "giorgi"

for i in range(len(list1)):
    print(list[i])


#2)

list2= [2,3,4,5,6,8]

for i in list2:
    print(i)



name = "goga aris kargi moswavle"

if "kargi" in name:
    print(True)
elif "kargi" not in name:
    print(False)

#1)

name1 = "goga"

vowels ="aeiou"

for i in name1:
    if i in vowels:
        print(True)
    else:
        print(False)


#2)


name2 = "goga"

vowels1 ="aeiou"

for i in name2:
    if i in vowels1:
        print(True)
    else:
        print(False)








