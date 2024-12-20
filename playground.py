with open('test.txt', 'r') as file:
    lines = file.readlines()
even_list = []
for index, value in enumerate(lines):
    if len(lines) >= 2 and index %2 != 0:
        even_list.insert(len(even_list), value)
print(even_list)