
print() # ფუნქცია

# + - / * // ** %

5 + 10 # 15

7 ** 2 # 49

7 / 5 # 1.35

# ლოგიკური ოპერატორები 

False and True

True or True

# not ლოგიკური ოპერატორები

#print(not True)
#print(not False)


# შედარების ოპერატორები 
# > < == != >= <=

5 > 1

8 <= 8

34 == 10


# მინიჭების ოპერატორები
# = += -=

number = 4
number += 1

# კუთვნილების ოპერატორე

for i in range(10):
    print(i)


#in -> კუთვნილების ოპერატორი

numbers = [1, 2, 3, 4, 5, 6, 7]

print(7 in numbers)

print(2 in numbers)

print("gio" in numbers)




                                                                                                                        

                                                                                                                        


text = input("შიყვანე ტექსტი")

if 'a' in text or 'A' in text:
    print(' ტექსტი შეიცავს a ასოს')
else:
    print('ტექსტი შეიცავს a ასოს')




text2 = input("შეიყვანე ტექსტი")

for i in text:
    print(i)

text2 = input("შეიყვანე ტექსტი")

for i in text:
    if i == "a" or i == "A":
        continue
    print(i)









