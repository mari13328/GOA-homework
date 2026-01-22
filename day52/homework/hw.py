
names = ["Batumi","Qobuleti","Tbilisi","qutaisi","zugdidi","poti"]

i = 0


while i < len(names):
    word = names[i]
    if word == word.lower():
        names[i] = word.upper()
        i += 1
    else:
        names.pop(i)

print(names)


                                                                                                                        


text = "HelloCookie"
list1 = []

i = 0
while i < len(text):
    if text[i] == text[i].upper():
        list1.append(text[i].lower())
    else:
        list1.append(text[i].upper())
        i += 1

print(list1)


                                                                                                                        


text = "aBcDeFGhs"
symbols = []

for i in range(len(text)):
    if text[i].islower():
        symbols.append("+")

    elif text[i].isupper():
        symbols.append("-")



i = 0
i1 = symbols.count("-")

while i < len(symbols):
    if i1 % 2 == 0:
        if symbols[i] == "+":
            symbols.pop(i)
        else:
            i += 1

    else:
        if symbols[i] == "-":
            symbols.pop(i)
        else:
            i += 1

print(symbols)


                                                                                                                        





















                                                                                                                        