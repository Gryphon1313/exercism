def append(list1: list, list2: list) -> list:
    return list1 + list2


def concat(lists: list) -> list:
    result = []
    for lst in lists:
        result.extend(lst)
    return result


def filter(function: callable, list: list) -> list:
    return [item for item in list if function(item)]


def length(list: list) -> int:
    return len(list)


def map(function: callable, list: list) -> list:
    return [function(item) for item in list]


def foldl(function: callable, list: list, initial: any) -> any:
    result = initial
    for item in list:
        result = function(result, item)
    return result


def foldr(function: callable, list: list, initial: any) -> any:
    list = reversed(list)
    for item in list:
        initial = function(initial, item)
    return initial

        


def reverse(list: list) -> list:
    return list[::-1]
