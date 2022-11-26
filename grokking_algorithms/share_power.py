def sum_my(list_my):
    if list ==[]:
        return 0
    value = list_my[0] + sum_my(list_my[1:])
    return value


lst = [1, 2, 4, 5, 6]
sum_my(lst)
