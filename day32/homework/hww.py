#1

for i in range(1,51):
    if i % 2 == 0:
        print("Even" + str(i))
    elif i % 2 == 1:
        print("Odd" + str(i))


#2


if i in range(20):

    if i % 3 == 0 and 1 % 5 == 0:
        print()
    elif i % 3 == 0:
        print()
    elif i % 5 == 0:
        print()


x = 0
y = 0

helloo = int(input("enter a number:"))

for i in range(0,helloo):
    if i % 2== 0:
        x= x + 1
    elif i % 2 == 1:
        y = y + 1

print(x)
print(y)




list = [5,10,15,20,25,30]

for i in range(6):
    if list[i] % 5 == 0:
        print(list[i])




input = input("enter your name")

for i in range(len(input)):
    print(i)


















