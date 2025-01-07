def apply_all_func(int_list, *functions):
    results = {}
    for func in functions:
        results[func.__name__] = func(int_list)
    return results


def min_f(args):
    min_ = min(args)
    return min_


def max_f(args):
    max_ = max(args)
    return max_


def len_f(args):
    len_ = len(args)
    return len_


def sum_f(args):
    sum_ = sum(args)
    return sum_


def sort_f(args):
    sort_list = sorted(args)
    return sort_list


print(apply_all_func([6, 20, 15, 9], max, min))
print(apply_all_func([6, 20, 15, 9], len, sum, sorted))
