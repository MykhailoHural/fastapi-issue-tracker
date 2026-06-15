array_of_int = [1, 2, 4, 5, 6, 9, 3, 7, 8]

new_arr = []
count = 0
for item in array_of_int:
    if item > count:
        count = item
        new_arr.append(item)
new_arr = sorted(array_of_int)

print(new_arr)

array_of_int2 = [1, 2, 4, 5, 6, 9, 3, 7, 8, 11, 34, 23, 27, 13]

print(list(reversed(sorted(array_of_int2))))

items = [
    {"id" : 1, "name" :"Item One", },
    {"id" : 2, "name" :"Item Two", },
    {"id" : 3, "name" :"Item Three", }
]

print(items[1]["name"])