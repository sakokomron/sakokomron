def right_rotate(lst, n):
    return lst[-n % len(lst):] + lst[:-n % len(lst)]
print(right_rotate([2, 1, 2, 3, 1, 9], 2))