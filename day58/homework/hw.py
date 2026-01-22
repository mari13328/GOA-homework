
word = input()
num = "" 

for i in range(len(word)-1,-1,-1):
    num += word[i]

                                                                                                                        

numm = [2,4,6,8,10,12,14]
list = []
list2 = []

for i in range(len(numm)):
    if numm[i] % 2 == 0 and i % 2 == 1:
        list.append(numm[i])



                                                                                                                        

lst = [1,2,2,3,3,3,4]
i = 0

while i < len(lst):
    while lst.count(lst[i]) > 1:
        lst.remove(lst[i])
        i += 1
print(lst)
