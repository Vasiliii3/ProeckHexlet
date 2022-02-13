def binary_sum(a, b):
    chislo = int(a, 2) + int(b, 2)
    return format(chislo, "b")

d = binary_sum("1101", "101")

print(type(d))
print(d)
#
# b = "10"
# print(int(b, 2))

# b = 0b10010
#
# print(format(b, 'b'))

def binary_sum2(number_a, number_b):
    binary_a = int(number_a, base=2)
    binary_b = int(number_b, base=2)
    return bin(binary_a + binary_b).replace('0b', '')
