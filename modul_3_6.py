data_structure = [
[1, 2, 3],
{'a': 4, 'b': 5},
(6, {'cube': 7, 'drum': 8}),
"Hello",
((), [{(2, 'Urban', ('Urban2', 35))}])
]

total_sum = 0
reksum = 0
def calculate_structure_sum(*args):
    total_sum = 0
    reksum = 0
    if args == 0:
        return 0
    else:
        for i in args:
            if isinstance(i, int):
                total_sum += i
            elif isinstance(i, str):
                total_sum += len(i)
            elif isinstance(i, (list, tuple, set)):
                reksum = calculate_structure_sum(*i)
                total_sum += reksum
            elif isinstance(i, dict):
                total_sum1 = calculate_structure_sum(*i.items())
                total_sum += total_sum1
        return total_sum



print(calculate_structure_sum(data_structure))