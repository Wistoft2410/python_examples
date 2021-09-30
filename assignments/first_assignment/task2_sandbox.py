list_of_strings = ["Hello; 123; 231. Hej; 654; 866. Davs; 345; 234. Goddag; 534; 765. Møjn!; 657; 456."]
print(list_of_strings[0])

strings = []

for row in list_of_strings:
    strings.append(row.split("."))

print(strings[-1]) #printing the last index


""" list_of_lists = [[]]

for item in strings:
    list_of_lists.append(item.split(";")[0])

print(list_of_lists) """