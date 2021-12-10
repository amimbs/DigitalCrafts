def bubble_sort(n):
    n = len(numbers)
    for i in range (n):
        #start at the length of numbers and go down 1 at a time

        for j in range (n - 1):
            if numbers[j] > numbers[j + 1]:
                numbers[j], numbers[j + 1] = numbers[ j + 1], numbers[j]

numbers= [1, 5, 8, 68, 70, 35, 4, 2, 100, 11]

bubble_sort(numbers)

print(f"Here are the sorted numbers:  {numbers}")


