import random
number = random.randint(-10000, 10000)
last_digit = abs(number) % 10
if last_digit > 5 and number > 0:
    print("Last digit of", number, "is", last_digit, "and is greater than 5")
elif last_digit < 6 and number > 0:
    print("Last digit of", number, "is", last_digit, "and is less than 6 and not 0")
elif last_digit == 0:
    print("Last digit of", number, "is", last_digit, "and is zero")
elif number < 0:
    print("Last digit of", number, "is", -last_digit, "is less than 6 and not 0")
else:
    print("TypeError")
