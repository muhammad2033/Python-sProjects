# finding digits from the given list

def is_group_number(group_data, n):
    for value in group_data:
        if n == value:
            return True
        else:
            return False


print(is_group_number([2, 3, 4, 5, 6, 8], 3))
print(is_group_number([1, -3, 8, 5, 6, 8], -1))
