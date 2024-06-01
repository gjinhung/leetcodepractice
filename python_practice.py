def is_same_num(num1, num2):
    if num1 == num2:
        return True
    return False


# print(is_same_num(4, 8))   #>  False
# print(is_same_num(2, 2))   #>  True
# print(is_same_num(2, "2"))


def not_equal(num1, num2):
    return num1 != num2


# print(not_equal(0, 2))  # >  True
# print(not_equal(2, 2))  # >  False
# print(not_equal(2, "2"))


def And(a, b):
    return a and b


# print(And(True, False))  # > False
# print(And(True, True))  # > True
# print(And(False, True))  # > False
# print(And(False, False))  # > False


def find_digit_amount(a):
    return len(str((a * a) ** 0.5)) - 2
    # return len(a)


# print(find_digit_amount(123))  # > 3
# print(find_digit_amount(-56))  # > 2
# print(find_digit_amount(7154))  # > 4
# print(find_digit_amount(61217311514))  # > 11
# print(find_digit_amount(0))


def recursive_fib(n):
    if n <= 1:
        return n
    else:
        return recursive_fib(n - 1) + recursive_fib(n - 2)


# print(recursive_fib(1))  # > 1
# print(recursive_fib(2))  # > 1
# print(recursive_fib(4))  # > 3
# print(recursive_fib(6))  # > 8
# print(recursive_fib(12))  # > 144


def recursive_countdown(n):
    if n == 0:
        return
    else:
        print(n)
        return recursive_countdown(n - 1)


# recursive_countdown(5)  # > 5 4 3 2 1)


def is_prime(n, l=2):
    if n <= 2:
        return True if n == 2 else False

    if n == l:
        # print(l)
        return True

    if n % l == 0:
        # print(l)
        return False

    return is_prime(n, l + 1)


# print(is_prime(1))  # > False
# print(is_prime(2))  # > True
# print(is_prime(3))  # > True
# print(is_prime(5))  # > True
# print(is_prime(9))  # > False
# print(is_prime(143))  # > False


def count_by(x, n):
    list = []
    i = 1

    while i <= n:
        list.append(x * i)
        i = i + 1

    return list


# print(count_by(1, 10))
# print(count_by(2, 5))


def double_char(s):
    return "".join(c * 2 for c in s)


# print(double_char("String"))


def is_even(n):

    return True if not n % 2 else False


# print(is_even(0.5))


def series_sum(n):
    res = 0
    div = 1
    for x in range(n):
        res += 1 / div
        div = div + 3
    return f"{res:.2f}"


# print(series_sum(1))


def to_jaden_case(string):
    str = string.split(" ")
    res = []
    for x in str:
        x = x.capitalize()
        res.append(x)
    " ".join(res)
    return " ".join([elem for elem in res])


def get_middle(s):
    index, odd = divmod(len(s), 2)
    return s[index] if odd else s[index - 1 : index + 1]


def get_sum(a, b):
    sum = 0
    if a == b:
        return a
    if a < b:
        while a < (b + 1):
            sum = sum + a
            a += 1
        return sum
    else:
        while b < (a + 1):
            sum = sum + b
            b += 1
        return sum


print(get_sum(0, -1))
