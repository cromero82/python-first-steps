# important! functions declare first, and use it later
def number_is_cousin(number_to_evaluate):
    number_iterator = 1
    module_is_zero_counter = 0

    while number_iterator <= number_to_evaluate:
        if number_to_evaluate % number_iterator == 0:
            module_is_zero_counter += 1
        number_iterator += 1

    if module_is_zero_counter == 2:
        return True
    else:
        return False


# call function with two break line after
is_cousin = number_is_cousin(4)
print(str(is_cousin))
