# number to evaluate
my_number = 7

number_iterator = 1
module_is_zero_counter = 0

while number_iterator <= my_number:
    if my_number % number_iterator == 0:
        module_is_zero_counter += 1
    number_iterator += 1

if module_is_zero_counter == 2:
    print("number: " + str(my_number) + " IS cousin")
else:
    print("number: " + str(my_number) + " ISN'T cousin")
