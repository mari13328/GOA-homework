

sentence = input("give a sentence: ")
words = []
word = ""
for i in sentence:
    if i !=" ":
        word += i
    else:
        words.append(word)
        word =""
if word:
    words.append(word)
print(words)
duplicants = []
for w in words:
    if w not in duplicants:
        count = 0
        for x in words:
            if x == w:
                count += 1
        print(w,count)
        duplicants.append(w)



