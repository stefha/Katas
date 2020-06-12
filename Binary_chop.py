def chop(value, array_of_int):
    result = -1
    begin_search_range = 0
    end_search_range = len(array_of_int)-1
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
    return -1
