

arr = ["cuty","car","apple","boy","dog","hgfvgsgcfsfd"]


longest_item = arr[0]


for item in arr:
    # თუ  item სიგრძე მეტია longest_item სიგრძეზე მაშინ,longest_item შევიყვანოთ item
    if len(item) > len(longest_item):
        longest_item = item

print(longest_item)








