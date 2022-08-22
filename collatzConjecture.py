starting_number = 2 ** 1000

while starting_number != 1:
    if starting_number % 2 == 0:
        starting_number //= 2
    else:
        starting_number = starting_number * 3 + 1

print("The number you set abides the collatz conjecture")
