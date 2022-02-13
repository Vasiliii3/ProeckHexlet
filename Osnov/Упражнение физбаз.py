def fizz_buzz(beg, end):
    if beg > end:
        return ""
    a = ""
    for i in range(beg, end+1):
        if i % 3 == 0 and i % 5 == 0:
            a = a + "FizzBuzz "
        elif i % 3 == 0:
            a = a + "Fizz "
        elif i % 5 == 0:
            a = a + "Buzz "
        else:
            a = a + str(i) + " "
    return a.rstrip()


print(fizz_buzz(1, 0))

# Решение учителя
# def fizz_buzz(start, stop):
#     result = ''
#     while start <= stop:
#         if result:
#             result += ' '
#         if start % 15 == 0:
#             result += 'FizzBuzz'
#         elif start % 3 == 0:
#             result += 'Fizz'
#         elif start % 5 == 0:
#             result += 'Buzz'
#         else:
#             result += str(start)
#         start += 1
#     return result


# def fizz_buzz(begin, end):
#     lst = []
#     for num in range(begin, end + 1):
#         if num % 3 and num % 5:
#             lst.append(str(num))
#         else:
#             lst.append("Fizz" * (not num % 3) + "Buzz" * (not num % 5))
#     return " ".join(lst)
