def chop(value, array_of_int):
    result = -1
    begin_search_range = 0
    end_search_range = len(array_of_int) - 1
    while True:
        len_search_range = end_search_range - begin_search_range
        if len_search_range == -1:
            return -1
        elif len_search_range == 0:
            return begin_search_range if array_of_int[begin_search_range] == value else -1
        elif len_search_range == 1:
            if array_of_int[begin_search_range] == value:
                return begin_search_range
            elif array_of_int[end_search_range] == value:
                return end_search_range
            else:
                return -1

        middle_index = begin_search_range + (len_search_range // 2)
        if array_of_int[middle_index] < value:
            begin_search_range = middle_index
        elif array_of_int[middle_index] > value:
            end_search_range = middle_index
        elif array_of_int[middle_index] == value:
            return middle_index


def chop_recursive(value, array_of_int):
    array_length = len(array_of_int)
    if array_length == 0:
        return -1
    elif array_length == 1:
        return 0 if array_of_int[0] == value else -1
    elif array_length == 2:
        if array_of_int[0] == value:
            return 0
        elif array_of_int[1] == value:
            return 1
        else:
            return -1
    else:
        middle_index = len(array_of_int) // 2
        index = 0
        if array_of_int[middle_index] == value:
            index = middle_index
        elif array_of_int[middle_index] < value:
            result_recursive = chop_recursive(value, array_of_int[middle_index:])
            index = middle_index + result_recursive if result_recursive != -1 else -1
        elif array_of_int[middle_index] > value:
            index = chop_recursive(value, array_of_int[:middle_index])
        return index


switcher_dict = {
    0: -1,
    1: 0,
    2: 0,

}


def chop_modular(value, array_of_int):
    if len(array_of_int) >= 3:
        return recursive_searching(value, array_of_int)
    else:
        return terminal_cases(value, array_of_int)


def recursive_searching(value, array_of_int):
    middle_index = get_middle_index(array_of_int)
    result = -1
    if array_of_int[middle_index] == value:
        return middle_index
    elif array_of_int[middle_index] > value:
        result = chop_modular(value, array_of_int[0:middle_index])
        return result if result != -1 else -1
    elif array_of_int[middle_index] < value:
        result = chop_modular(value, array_of_int[middle_index + 1:])
        return result + middle_index + 1 if result != -1 else -1


def terminal_cases(value, array_of_int):
    if len(array_of_int) == 2:
        result = -1
        if array_of_int[0] == value:
            result = 0
        elif array_of_int[1] == value:
            result = 1
        return result

    elif len(array_of_int) == 1:
        return 0 if value == array_of_int[0] else -1

    elif len(array_of_int) == 0:
        return -1


def get_middle_index(array_of_int):
    return -1 if len(array_of_int) == 0 else len(array_of_int) // 2


def chop_simple_structure(value, array_of_int):
    middle_index = get_middle_index(array_of_int)
    result = 0
    if middle_index == -1:
        result = -1
    elif middle_index == 0:
        if array_of_int[0] == value:
            result = 0
        elif len(array_of_int) == 2 and middle_index[1] == value:
            result = 1
        else:
            result = -1
    elif array_of_int[middle_index] == value:
        result = middle_index
    elif array_of_int[middle_index] > value:
        result = chop_modular(value, array_of_int[0:middle_index])
        result = result if result != -1 else -1
    elif array_of_int[middle_index] < value:
        result = chop_modular(value, array_of_int[middle_index + 1:])
        result = result + middle_index + 1 if result != -1 else -1
    return result


def simple_chop(value, array_of_ints):
    length = len(array_of_ints)
    if length >= 3:
        return search_half_of_range(value, array_of_ints)
    else:
        return resolve_terminal_cases(value, array_of_ints)


def resolve_terminal_cases(value, array_of_ints):
    length = len(array_of_ints)
    result = -1
    if length == 0:
        result = -1
    elif length > 0:
        result = 0 if value == array_of_ints[0] else -1
        if result == -1 and length == 2:
            result = 1 if value == array_of_ints[1] else -1
    return result


def search_half_of_range(value, array_of_ints):
    middle_index = len(array_of_ints) // 2
    middle_value = array_of_ints[middle_index]
    result = 0
    if middle_value == value:
        result = middle_index
    elif middle_value < value:
        chop_rec_result = simple_chop(value, array_of_ints[middle_index:])
        result = middle_index + chop_rec_result if chop_rec_result != -1 else -1
    elif middle_value > value:
        result = simple_chop(value, array_of_ints[0:middle_index])
    return result


def binary_chop_iterative(value, array):
    offset = 0
    while len(array) > 1:
        middle_index = len(array) // 2
        middle_value = array[middle_index]
        if value == middle_value:
            array = array[middle_index:middle_index + 1]  # test
            offset += middle_index
        elif value < middle_value:
            array = array[0:middle_index]
        else:
            array = array[middle_index:]
            offset += middle_index

    return offset if len(array) == 1 and array[0] == value else -1


def binary_chop_recursive_new(value, array):
    if len(array) < 2:
        return -1 if len(array) == 0 or value != array[0] else 0  # needed ? len(array) == 0 or
    else:
        middle_index = len(array) // 2
        middle_value = array[middle_index]
        if value == middle_value:
            return middle_index
        elif value < middle_value:
            return binary_chop_recursive_new(value, array[:middle_index])
        else:
            rec_result = binary_chop_recursive_new(value, array[middle_index:])
            return rec_result + middle_index if rec_result != -1 else -1


def binary_chop_iterative_2(value, array):
    offset = 0
    while len(array) > 1:
        middle_index = len(array) // 2
        middle_value = array[middle_index]
        if value == middle_value:
            array = array[middle_index:middle_index + 1]
            offset += middle_index
        elif value > middle_value:
            array = array[middle_index:]
            offset += middle_index
        else:
            array = array[:middle_index]

    return offset if len(array) == 1 and array[0] == value else -1


def binary_chop_recursive_2(value, array):
    if len(array) < 2:
        return 0 if len(array) == 1 and array[0] == value else -1
    else:
        middle_index = len(array) // 2
        middle_value = array[middle_index]
        if value == middle_value:
            return middle_index
        elif value > middle_value:
            rec_result = binary_chop_recursive_2(value, array[middle_index:])
            return middle_index + rec_result if rec_result != -1 else -1
        else:
            return binary_chop_recursive_2(value, array[:middle_index])
