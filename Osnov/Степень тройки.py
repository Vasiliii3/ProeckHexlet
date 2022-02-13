def is_power_of_three(a):
    if a == 1:
        return True
    b = int(a ** (1/3))
    c = 3 ** b
    return a == c

a = 729

def is_power_of_three2(number):
    counter = 1  # 3 ** 0
    while counter < number:
        counter *= 3
    return counter == number

print(is_power_of_three2(a))

