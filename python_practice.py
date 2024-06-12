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


# print(get_sum(0, -1))


def longest(a1, a2):
    res = ""
    comb = list(set(a1 + a2))
    comb.sort()
    for x in comb:
        res = res + x
    return res


# a = "aretheyhere"
# b = "yestheyareher"

# print(longest(a, b))


def century(year):
    year = f"{year}"
    if year == 0:
        return 0
    if len(year) < 3:
        return 1
    length = len(year)

    res = int(year[0 : length - 2])
    if int(year[-2:length]) > 0:
        res += 1
    return res


# print(century(22289))


def count_sheep(n):
    res = ""
    count = 1
    while count <= n:
        res = res + f"{count} sheep..."
        count += 1
    return res


# return ''.join(f"{i} sheep..." for i in range(1,n+1))


# print(count_sheep(3))


def remove_every_other(my_list):
    res = []
    for x in range(len(my_list)):
        if not x % 2:
            res.append(my_list[x])

    return res


# print(remove_every_other(["Hello", "Goodbye", "Hello Again"]))


def basic_op(operator, value1, value2):
    return eval(f"{value1}{operator}{value2}")


# print(basic_op("+", 4, 7))


def greet(language):
    lan = {
        "english": "Welcome",
        "czech": "Vitejte",
        "danish": "Velkomst",
        "dutch": "Welkom",
        "estonian": "Tere tulemast",
        "finnish": "Tervetuloa",
        "flemish": "Welgekomen",
        "french": "Bienvenue",
        "german": "Willkommen",
        "irish": "Failte",
        "italian": "Benvenuto",
        "latvian": "Gaidits",
        "lithuanian": "Laukiamas",
        "polish": "Witamy",
        "spanish": "Bienvenido",
        "swedish": "Valkommen",
        "welsh": "Croeso",
    }
    return lan.get(language, "Welcome")


# print(greet("irish"))


def invert(lst):
    res = []
    for x in lst:
        res.append(eval(f"{-1}{'*'}{x}"))
    return res


# print(invert([1, 2, 3, 4, 5]))


def number(lines):
    # num = 1
    # res = []
    # for x in lines:
    #     res.append(f"{num}: {x}")
    #     num += 1
    # return res

    return [f"{x+1}: {lines[x]}" for x in range(len(lines))]


# print(number(["a", "b", "c"]))


def validate_pin(pin):
    return len(pin) in [4, 6] and pin.isdigit()


def row_sum_odd_numbers(n):
    # count = 1
    # total = 0
    # res = 0
    # while count < n:
    #     total += count
    #     count += 1
    # start = (total * 2) + 1
    # for x in range(n):
    #     res += start
    #     start += 2
    # return res
    return n**3


# print(row_sum_odd_numbers(3))


def how_much_i_love_you(nb_petals):
    words = ["I love you", "a little", "a lot", "passionately", "madly", "not at all"]
    idx = nb_petals % 6
    return words[idx - 1]


# print(how_much_i_love_you(6))


def switch_it_up(number):
    return [
        "Zero",
        "One",
        "Two",
        "Three",
        "Four",
        "Five",
        "Six",
        "Seven",
        "Eight",
        "Nine",
    ][number]


# print(switch_it_up(0))


def reverse_seq(n):
    return [n - x for x in range(n)]
