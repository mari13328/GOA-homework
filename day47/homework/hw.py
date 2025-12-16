
namee = ["mari","nana","liza","qeta","mzia","ele"]


upper_name = []


for name in namee:
    if name[0] == name[0].upper():
        upper_name.append(name)
print(upper_name)




neme = ["nini","nia","gio"]

surnames = ["SHAKARISHVILI","DOLIDZE","BOLKVADZE"]


for i in range(len(neme)):
    neme[i] = neme[i].upper()

for i in range(len(surnames)):
    surnames[i] = surnames[i].lower()

last = neme + surnames
print(last)





numbers = [3.5,11.3,7.9,8.8,2.3,11.5,34.9,9.9]









cities = ["zugdidi","tbilisi","qutaisi","didgori"]

countrs = ["spain","georgia","japan","italy","china,","india","brazil"]


for i  in range(5):
    countrs.insert(i, cities[i])

print(countrs)