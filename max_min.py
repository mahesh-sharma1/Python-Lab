def find_max(numbers):
    # if not numbers:
    #     return None
    max_num = numbers[0]
    for num in numbers:
        if num > max_num:
            max_num = num
    return max_num

def find_min(numbers):
    # if not numbers:
    #     return None
    min_num = numbers[0]
    for num in numbers:
        if num < min_num:
            min_num = num
    return min_num

# Test the functions
test_list = [20, 15, 7, 69, 99, 0, 8]
print(f"List: {test_list}")
print(f"Maximum: {find_max(test_list)}")
print(f"Minimum: {find_min(test_list)}")