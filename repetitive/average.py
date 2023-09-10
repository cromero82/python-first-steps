my_numbers = [2, 4, 8, 10, 22]
acummulator = 0
size = 0

for number in my_numbers:
    acummulator += number
    size += 1

average = acummulator / size
print("average is: " + str(average))
