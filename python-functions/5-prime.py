def is_prime(number):
    if number < 2:
        return False
    elif number == 2:
        return True

    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            return False

    return True
