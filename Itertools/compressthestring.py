from itertools import groupby
input_string = input()
grouped_elements = groupby(input_string)
result_tuples = []
for key, group in grouped_elements:
    group_length = len(list(group))
    key_as_integer = int(key)
    result_tuples.append((group_length, key_as_integer))
print(*result_tuples)


"""
    INPUT
1222311

    OUTPUT
(1, 1) (3, 2) (1, 3) (2, 1)

"""
