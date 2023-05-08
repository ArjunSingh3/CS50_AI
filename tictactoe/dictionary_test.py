

dictionary_list = {
    -1:[1,1],
    0: [1,2],
    1:[2,2]
}

myKeys = list(dictionary_list.keys())
myKeys.sort()
sorted_dict = {i: dictionary_list[i] for i in myKeys}
print(sorted_dict)
print(sorted_dict.popitem()[1])
print(sorted_dict)