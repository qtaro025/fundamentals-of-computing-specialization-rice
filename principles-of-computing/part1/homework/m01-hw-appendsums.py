def appendsums(lst):
    """Repeatedly append the sum of the current last three elements of
    lst to lst.

    Args:
        lst (list): list of number
    Note: The function should loop for 25 times
    """
    ntimes = 25

    for dummy_val in range(0, ntimes):
        lst.append(sum(lst[-3:]))
        print(lst)

    return lst

sum_three = [0, 1, 2]
appendsums(sum_three)
print(sum_three[10])
print(sum_three[20])