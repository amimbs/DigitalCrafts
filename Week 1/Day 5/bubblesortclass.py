numbers= [1, 5, 8, 68, 70, 35, 4, 2, 100, 11]

for i in range(0, len(numbers)):
   for j in range(0, len(numbers)):
        if numbers[i] > numbers[j]:
                    # < of we want to reverse it
            # we create a temp variable = to our sort array of [i]. If [j] == [i] it stops
            temp = numbers[i]
            numbers[i] = numbers[j]
            numbers[j] = temp

print(numbers)

