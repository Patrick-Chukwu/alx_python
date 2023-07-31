def fibonacci_sequence(n):
    if n == 0:
        return 0
    else if n == 1:
        return 1

    prev_num, current_num = 0, 1
    for n in range(2, n+1):
        next_num = prev_num  + current_num
        prev_num, current_num = current_num, next_num

    return current_num
    