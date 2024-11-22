def element_frequency(lst):
    return {i: lst.count(i) for i in range(max(lst) + 1)}
print("Frequency of elements:", element_frequency([2, 1, 2, 3, 1, 9]))