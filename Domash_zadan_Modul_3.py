data_structure = [
[1, 2, 3],
{'a': 4, 'b': 5},
(6, {'cube': 7, 'drum': 8}),
"Hello",
((), [{(2, 'Urban', ('Urban2', 35))}])
]
def calculate_structure_sum(*data_structure):
    summa = 0
    for i in data_structure:
        if isinstance(i, int):
            summa = i + summa

        elif isinstance(i, str):
            summa = len(i) + summa

        elif isinstance(i, (list, set, tuple)):
            summa = calculate_structure_sum(*i) + summa

        elif isinstance (i, dict):
            summa = calculate_structure_sum(*i.keys(), *i.values()) + summa

    return summa

calculate_structure_sum(data_structure)

result = calculate_structure_sum(data_structure)
print(result)