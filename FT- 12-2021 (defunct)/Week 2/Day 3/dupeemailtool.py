with open ("emails.txt") as file:
    content = file.read()

print(content)

bad_list = []

bad_list.append(content)

print("Before removing dupes")
for i in range(len(bad_list)):
    print(bad_list[i])

print("**************************************************************")

good_list = []

print("After removing dupes")
for i in bad_list:
    if i not in good_list:
        good_list.append(i)

for i in range(len(good_list)):
    print(good_list[i])