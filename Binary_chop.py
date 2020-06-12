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
            index = middle_index + chop_recursive(value, array_of_int[middle_index:])
        elif array_of_int[middle_index] > value:
            index = chop_recursive(value, array_of_int[:middle_index])
        return index
