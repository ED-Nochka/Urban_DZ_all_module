def calculate_structure_sum(data_structure):
    summa = 0
    for el in data_structure:
        if isinstance(el, int):
            summa += el
        elif isinstance(el, str):
            summa += len(el)
        elif isinstance(el, list) or isinstance(el, tuple):
            summa += calculate_structure_sum(el)
        elif isinstance(el, dict):
            summa += calculate_structure_sum(list(el.keys()))
            summa += calculate_structure_sum(list(el.values()))
        elif isinstance(el, set):
            summa += calculate_structure_sum(el)
    return summa


data_structure = [
  [1, 2, 3],
  {'a': 4, 'b': 5},
  (6, {'cube': 7, 'drum': 8}),
  "Hello",
  ((), [{(2, 'Urban', ('Urban2', 35))}])
]

result = calculate_structure_sum(data_structure)
print(result)
