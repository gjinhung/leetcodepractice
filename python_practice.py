import math


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

    return [eval(f"{-1}{'*'}{x}") for x in lst]


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


# return list(range(n, 0, -1))


def is_pangram(st):
    alph = [
        "a",
        "b",
        "c",
        "d",
        "e",
        "f",
        "g",
        "h",
        "i",
        "j",
        "k",
        "l",
        "m",
        "n",
        "o",
        "p",
        "q",
        "r",
        "s",
        "t",
        "u",
        "v",
        "w",
        "x",
        "y",
        "z",
    ]
    st = st.lower()
    for x in alph:
        if st.count(x) < 1:
            return False
    return True


# print(is_pangram("The quick brown fox jumps over the lazy dog."))


def alphabet_position(text):
    alph = [
        "a",
        "b",
        "c",
        "d",
        "e",
        "f",
        "g",
        "h",
        "i",
        "j",
        "k",
        "l",
        "m",
        "n",
        "o",
        "p",
        "q",
        "r",
        "s",
        "t",
        "u",
        "v",
        "w",
        "x",
        "y",
        "z",
    ]
    st = text.lower()
    res = []
    for char in list(st):
        if char in alph:
            res.append(f"{alph.index(char) + 1}")
    return " ".join(res)

    # print(alphabet_position("The sunset sets at twelve o' clock."))

    # def twoSum(nums, target):
    # num1 = 0
    # num2 = 1
    # length = len(nums) - 2
    # while num1 <= length:
    #     print(f"{nums[num1]} + {nums[num2]}")
    #     if nums[num1] + nums[num2] == target:
    #         return [num1, num2]
    #     num2 += 1
    #     if num2 == len(nums):
    #         num1 += 1
    #         num2 = num1 + 1
    # return []

    # for num in nums:
    #     diff = target - num
    #     if diff != num:
    #         return [nums.index(num), nums.index(diff)]

    numhash = {nums}
    return numhash


# print(twoSum([3, 2, 4], 6))


def hasDuplicate(nums):
    nums.sort()
    for x in nums:
        if nums.count(x) > 1:
            return True
    return False


def isAnagram(s, t):
    if len(s) != len(t):
        return False
    countS, countT = {}, {}

    for i in range(len(s)):
        countS[s[i]] = 1 + countS.get(s[i], 0)
        countT[t[i]] = 1 + countT.get(t[i], 0)
    return countS == countT


# print(isAnagram("cat", "tdc"))


def twoSum2(nums, target):
    hashSet = {}

    for idx, num in enumerate(nums):
        diff = target - num
        if diff in hashSet:
            return [hashSet[diff], idx]
        else:
            hashSet[num] = idx


# print(twoSum2([3, 4, 5, 6], 7))


# input = array of strs
# output = array of sets of lists with anagrams
# [["hat"],["act", "cat"],["stop", "pots", "tops"]]

from collections import defaultdict


def groupAnagrams(strs):

    ans = defaultdict(list)
    print(ans)

    for s in strs:
        count = [0] * 26
        for c in s:
            count[ord(c) - ord("a")] += 1
        ans[tuple(count)].append(s)
        # print(ans)
    return ans.values()

    # hashSet = {}

    # result = []

    # for idx, str in enumerate(strs):

    #     if len(str) in hashSet:
    #         array = hashSet[len(str)]
    #         array.append([idx, str])
    #         hashSet[len(str)] = array

    #     else:
    #         hashSet[len(str)] = [[idx, str]]

    # for x in hashSet.values():
    #     hashX = {}
    #     for set in x:
    #         res = list(set[1])
    #         res.sort()
    #         res2 = "".join(res)
    #         if res2 in hashX:
    #             hashX[res2].append(strs[set[0]])
    #         else:
    #             hashX[res2] = [strs[set[0]]]
    #     for k in hashX.values():
    #         result.append(k)
    # return result


# print(groupAnagrams(["act", "pots", "tops", "cat", "stop", "hat"]))

# input string
# output true/false


def isPalindrome(s):
    ls = s.lower()
    newS = ""
    for i in range(len(ls)):
        if ls[i].isalnum():
            newS += ls[i]
    if len(newS) == 1:
        return True
    half = 0
    if len(newS) % 2 > 0:
        half = ((len(newS)) / 2) + 0.5
    else:
        half = (len(newS)) / 2
    for x in range(int(half)):
        if newS[x] != newS[len(newS) - x - 1]:
            return False
    return True


# print(isPalindrome("0P"))


def maxProfit(prices) -> int:
    # res = 0
    # l = len(prices) - 1
    # while l > 0:
    #     i = 0
    #     while i < l:
    #         if (prices[l] - prices[i]) > res:
    #             res = prices[l] - prices[i]
    #         i += 1
    #     l -= 1
    # return res
    res = 0
    for idx, ele in enumerate(prices):
        if idx > 0:
            if ele - min(prices[:idx]) > res:
                res = ele - min(prices[:idx])
    return res


# print(maxProfit([1,2,3,4,5]))


def isValid(s):

    front = []  # ["[", "("]
    beg = {"{": "}", "[": "]", "(": ")"}
    for x in s:  # x="]"
        if x in beg.keys():  # false
            front.append(x)
        elif not len(front):
            return False
        elif x != beg[front[-1]]:  # x = ] beg[(] = )
            return False
        else:
            del front[-1]
    if not len(front):
        return True
    else:
        return False


# print(isValid("(("))


def search(nums, target):
    if target in nums:
        return nums.index(target)
    else:
        return -1


# print(search([-1,3,3,0,2,4,6,8,3], 3))


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def reverseList(head: ListNode):
    prev = None
    curr = head

    while curr:
        temp = curr.next
        curr.next = prev
        prev = curr
        curr = temp
    return prev


def twoMergedList(list1, list2):
    merged = ListNode()
    curr = merged
    while list1 and list2:
        if list1.val <= list2.val:
            curr.next = list1
            list1 = list1.next
        else:
            curr.next = list2
            list2 = list2.next
        curr = curr.next
    curr.next = list1 or list2
    return merged.next


def topKFrequent(nums, k):
    freq = [[] for i in range(len(nums) + 1)]
    hashMap = {}
    for num in nums:
        hashMap[num] = 1 + hashMap.get(num, 0)

    for e, v in hashMap.items():
        freq[e].append(v)
        # if v > maxV:
        #     maxV = v
        #     maxK = e

    res = []
    for i in range(len(freq) - 1, 0, -1):
        for n in freq[i]:
            res.append(n)
            if len(res) == k:
                return res


# print(topKFrequent([4,2,2,2,2,3,3], 2))


def missingNumber(nums) -> int:
    for x in range(len(nums)):
        if x not in nums:
            return x
    return len(nums)


# print(missingNumber([3,0,1]))


def reverseBits(n) -> int:
    newB = ["0" for i in range(32)]
    count = 0
    b = bin(n)[2::]
    for x in range(len(list(b)), 0, -1):
        newB[count] = b[x - 1]
        count += 1
    return int("".join(newB), 2)


# print(reverseBits(21))


def countingBits(n):
    res = [] * n + 1
    for i in range(n + 1):

        count = list(bin(i)[2::]).count("1")
        res.append(count)
    return res


# print(countingBits(4))


def hammingWeight(n):
    res = 0
    while n:
        n &= n - 1
        res += 1
    return res


# print(hammingWeight(11))


def singleNumber(nums):
    res = 0
    for n in nums:
        res = n ^ res
    return res


def digitize(n):
    return [int(x) for x in str(n)[::-1]]


# print(digitize(3541))


def hoop_count(n):
    return "Great, now move on to tricks" if n >= 10 else "Keep at it until you get it"


# print(hoop_count(0))


def reverse_words(text):
    # newString = text.split(' ')

    # for x in range(len(newString)):
    #     reverse = ''

    #     for y in range(len(newString[x]), 0, -1):
    #         reverse = reverse + (newString[x][y-1])
    #     newString[x] = reverse
    # return ' '.join(newString)
    return " ".join(t[::-1] for t in text.split(" "))


# print(reverse_words('tesT this Example'))


def disemvowel(string_):
    return "".join(c for c in string_ if c.lower() not in "aeiou")
    vowels = ["A", "E", "I", "O", "U"]
    res = ""

    for x in string_:
        if x.upper() not in vowels:
            res += x

    return res


# print(disemvowel("First fixed test"))


def correct(t):
    hashSet = {"5": "S", "0": "O", "1": "I"}

    s = list(t)

    for x in range(len(s)):
        if s[x] in hashSet:
            s[x] = hashSet[s[x]]
        else:
            continue
    return "".join(s)


# print(correct('L0ND0N'))


def stray(arr):
    count = {}
    l = [[] for i in range(len(arr) + 1)]
    for x in arr:
        count[x] = 1 + count.get(x, 0)

    for n, c in count.items():
        l[c] = n
    return l[1]


# print(stray([1, 1, 2]))


def expandedForm(num):
    s = str(num)
    l = len(s)
    res = []
    for i, x in enumerate(s):
        if int(x) > 0:
            e = "0" * (l - (i + 1))
            res.append(f"{x}{e}")

    return " + ".join(res)


# print(expandedForm(70305))


def remove_char(s):
    return s[1:-1]


# print(remove_char('test'))


def sum_str(a, b):
    return str(int(a or 0) + int(b or 0))


# print(sum_str("", '2'))


def other_angle(a, b):
    return 180 - a - b


def human_years_cat_years_dog_years(human_years):
    res = [human_years, 0, 0]
    if human_years == 1:
        res[1] = res[2] = 15
    if human_years == 2:
        res[1] = res[2] = 9 + 15
    if human_years > 2:
        res[1] = 9 + 15 + ((human_years - 2) * 4)
        res[2] = 9 + 15 + ((human_years - 2) * 5)
    return res


# print(human_years_cat_years_dog_years(10))


def divisors(n):
    # count = 0
    # mid = int(math.sqrt(n)) + 1
    # for i in range(1, mid):
    #     if not n%i:
    #         count += 2

    # if (int(math.sqrt(n)) ** 2 == n):
    #     count -= 1
    # return count
    return sum([True if n % i == 0 else False for i in range(1, n + 1)])


# print(divisors(4))


def delete_nth(order, max_e):
    hashSet = {}
    res = []
    for e in order:
        if e not in hashSet or hashSet[e] < max_e:
            hashSet[e] = 1 + hashSet.get(e, 0)
            res.append(e)
    return res


# print(delete_nth([1,2,3,1,2,1,2,3], 2))


def tribonacci(signature, n):
    if n >= 3:
        res = signature
        for i in range(n - len(signature)):
            print(i)
            newNum = sum(res[-3::])
            res.append(newNum)
        return res
    else:
        res = []
        for i in range(n):
            res.append(signature[i])
        return res


# print(tribonacci([1, 2, 3], 2))


def find_smallest_int(arr):
    smallest = arr[0]

    for i in arr:
        if i < smallest:
            smallest = i
    return smallest

    # return min(arr)


# print(find_smallest_int([1,2,3]))


def first_non_consecutive(arr):
    for i in range(1, len(arr)):
        if arr[i] != arr[i - 1] + 1:
            return arr[i]
    return None


# print(first_non_consecutive([1,2,3,4]))


def reverse_list(l):
    return [l[i - 1] for i in range(len(l), 0, -1)]


# print(reverse_list([1,2,3,4]))


def nb_year(p0, percent, aug, p):
    yr = 0
    pop = p0
    while pop < p:
        pop = math.floor(pop + ((pop * (percent * 0.01)) + aug))
        yr += 1
    return yr


# print(nb_year(1000, 2.0, 50, 1214))


def tower_builder(n_floors):
    res = []
    for x in range(0, n_floors):
        res.append(
            f'{" "*(n_floors - x - 1)}{"*" * ((x * 2) + 1)}{" "*(n_floors - x- 1)}'
        )
        # res.append(f"{" "*(n_floors - x)}{res[x-1] + "**"}{" "*(n_floors - x)}")
    return res


# print(tower_builder(3))


def count_smileys(arr):
    count = 0
    for face in arr:
        eyes = False
        nose = True
        validN = ["~", "-"]
        validM = [")", "D"]
        for x in face:
            if not eyes:
                if x == ";" or x == ":":
                    eyes = True
            elif nose:
                if x not in validM and x not in validN:
                    nose = False
                elif x in validM:
                    count += 1

    return count


# print(count_smileys([':-D', ';(', ';D', ':oD', ':o(', ';o(', ':-D', ';-(', ';oD', ':(', ':D', ';o(', ';-(', ';-D', ';D']))


def update_light(current):
    lights = ["green", "yellow", "red", "green"]
    return lights[lights.index(current) + 1]


# print(update_light("yellow"))


def expression_matter(a, b, c):
    return max(
        a + b + c,
        a + b * c,
        (a + b) * c,
        a * b * c,
        a * b + c,
        a * (b + c),
    )


# print(expression_matter(3, 3, 3))


def between(a, b):
    return [x for x in range(a, b + 1)]


# print(between(1,3))


def sort_array(source_array):
    indexes = []
    odds = []
    for idx, el in enumerate(source_array):
        if el % 2 != 0:
            indexes.append(idx)
            odds.append(el)
    odds.sort()
    for x in range(len(indexes)):
        source_array[indexes[x]] = odds[x]
    return source_array


# print(sort_array([]))


def small_enough(array, limit):
    for x in array:
        if x > limit:
            return False
    return True


# print(small_enough([66, 101] ,200))


def gimme(input_array):
    return input_array.index(sorted(input_array)[1])


# print(gimme([15,10,14]))


def pipe_fix(nums):
    return [x for x in range(min(nums), max(nums) + 1)]


# print(pipe_fix([1, 2, 3, 12]))


def decrypt(encrypted_text, n):
    def decryptOnce(encrypted_text):
        odd = ""
        even = ""
        for idx, el in enumerate(encrypted_text):
            if idx % 2:  # if odd
                odd += el
            else:
                even += el
        return odd + even

    res = encrypted_text
    for x in range(n):
        res = decryptOnce(res)
    return res


# print(decrypt("012345", 2))


def encrypt(text, n):
    def encryptOnce(encrypted_text):
        mid = ""
        if len(encrypted_text) % 2:  # if odd
            mid = encrypted_text[math.floor(len(f"{encrypted_text}") / 2)]
            listText = list(encrypted_text)
            listText.pop(math.floor(len(f"{encrypted_text}") / 2))
            encrypted_text = "".join(listText)
        num = ""
        for x in range(math.floor(len(f"{encrypted_text}") / 2)):
            if not mid:
                num += encrypted_text[math.floor(len(f"{encrypted_text}") / 2) + x]
                num += encrypted_text[x]
            else:
                num += encrypted_text[x]
                num += encrypted_text[math.floor(len(f"{encrypted_text}") / 2) + x]
        return mid + num

    for x in range(n):
        text = encryptOnce(text)
    return text


# print(encrypt(decrypt("01234", 2), 2))


def is_palindrome(s):
    return s.lower() == "".join(list(s.lower())[::-1])


# print(is_palindrome("rAcecar"))


def remove(s):
    if s:
        if s[-1] == "!":
            return s[:-1]
        else:
            return s
    return s


# print(remove(""))


def factorial(n):
    if n < 0 or n > 12:
        raise ValueError("Invalid value provided.")
    res = 1
    for x in range(1, n + 1):
        res = res * x
    return res


# print(factorial(3))


def persistence(n):
    count = 0
    while n >= 10:
        multi = 1
        for x in f"{n}":
            multi = multi * int(x)
        n = multi
        count += 1
    return count


# print(persistence(25))


def bin_to_decimal(inp):
    return int(inp, 2)


# print(bin_to_decimal('101010'))

geese = ["African", "Roman Tufted", "Toulouse", "Pilgrim", "Steinbacher"]


def goose_filter(birds):
    return [bird for bird in birds if bird not in geese]


# print(goose_filter(["Mallard", "Hook Bill", "African", "Crested", "Pilgrim", "Toulouse", "Blue Swedish"]))


def reverse_letter(st):
    res = ""
    for letter in st:
        test = letter.isalpha()
        if test:
            res = letter + res
    return res


# print(reverse_letter('ultr53o?n'))


def breakCamelCase(s):
    # res = ""
    # for letter in s:
    #     isUpper = letter.isupper()
    #     if isUpper:
    #         res = res + " " + letter
    #     else:
    #         res = res + letter
    # return res

    return "".join([f" {x}" if x.isupper() else f"{x}" for x in s])


# print(breakCamelCase("helloWorld"))


def shortcut(s):
    # vowels = ['a','e','i','o','u']
    # for x in s:
    #     if x in vowels:

    return "".join([f"{x}" if x not in ["a", "e", "i", "o", "u"] else "" for x in s])


# print(shortcut("hello"))


def chromosome_check(s):
    return (
        "Congratulations! You're going to have a son"
        if s[1] == "Y"
        else "Congratulations! You're going to have a daugther"
    )


def string_to_array(s):
    return s.split(" ")


# print(string_to_array("this is hello"))


def maps(a):
    return [x * 2 for x in a]


# print(maps([1, 2, 3]))


def getConcatenation(nums):
    return nums + nums


# print(getConcatenation([1, 2, 1]))


def replaceElements(arr):
    # res = []
    # while len(arr) > 1:
    #     arr.pop(0)
    #     res.append(max(arr))

    # res.append(-1)
    # return res

    max = arr[-1]
    res = []
    for el in range(len(arr) - 1, 0, -1):
        if arr[el] < max:
            res.insert(0, max)
        else:
            max = arr[el]
            res.insert(0, max)
    res.append(-1)
    return res


# print(replaceElements([17, 18, 5, 4, 6, 1]))


def capitals(word):
    # res = []
    # for idx, letter in enumerate(word):
    #     if letter.isupper():
    #         res.append(idx)
    # return res

    return [idx for idx, letter in enumerate(word) if letter.isupper()]


# print(capitals("CodEWaRs"))


def is_isogram(string):
    hashSet = {}

    for letter in string.lower():
        if letter not in hashSet:
            hashSet[letter] = 1
        else:
            return False
    return True


# print(is_isogram("HelLo"))


def isSubsequence(s, t):
    # hashSet = {}
    # curCount = 0
    # for idx, letter in enumerate(t):
    #     hashSet[idx] = letter
    # for letter in list(s):
    #     print(letter)
    #     if letter not in hashSet:
    #         return False
    #     elif hashSet[letter] < curCount:
    #         return False
    #     else:
    #         curCount = hashSet[letter]
    # return True

    # currentIdx = 0
    # listT = list(t)
    # for letter in s:
    #     if letter not in listT:
    #         return False
    #     idx = listT.index(letter)
    #     if idx < currentIdx:
    #         return False
    #     else:
    #         currentIdx = idx
    #         listT.pop(idx)
    # return True
    if s == "":
        return True
    currentIdx = 0
    for letter in t:
        if letter is s[currentIdx]:
            currentIdx += 1
        if currentIdx == len(s):
            return True
    return False


# print(isSubsequence("ab", "baab"))


def add_length(str):
    # res = []
    # strList = str.split(" ")
    # for word in strList:
    #     res.append(f"{word} {len(word)}")
    # return res

    return [f"{word} {len(word)}" for word in str.split(" ")]


# print(add_length("hello there"))


def positive_sum(arr):
    # res = []
    # for num in arr:
    #     if num > 0:
    #         res.append(num)
    # return sum(res)

    return sum([num if num > 0 else 0 for num in arr])


# print(positive_sum([1, -2, 3, 4, 5]))


def combat(health, damage):
    return health - damage if health - damage >= 0 else 0


# print(combat(20, 0))


def is_anagram(test, original):
    hashSet = {}

    for letter in test.lower():
        if letter in hashSet:
            hashSet[letter] += 1
        else:
            hashSet[letter] = 1

    for letter in original.lower():
        if letter in hashSet:
            hashSet[letter] -= 1
            if hashSet[letter] == 0:
                del hashSet[letter]
        else:
            return False
    if hashSet.keys():
        return False
    return True


# print(is_anagram("foefet", "toffee"))


def dir_reduc(arr):
    val = {"NORTH": 1, "SOUTH": -1, "EAST": 2, "WEST": -2}
    if not len(arr):
        return []
    res = [val[arr[0]]]
    for idx in range(1, len(arr)):
        print(f"beginning res {res}")
        dir = arr[idx]
        if not len(res):
            res.append(val[dir])
            print("append first")
        else:
            if res[-1] + val[dir] == 0:
                res.pop()
                print("remove last")
                print(f"remove res {res}")
            else:
                res.append(val[dir])
                print("append end")

    unVal = {1: "NORTH", -1: "SOUTH", 2: "EAST", -2: "WEST"}
    for idx, num in enumerate(res):
        res[idx] = unVal[num]
    return res


# print(
#     dir_reduc(
#         [
#             "EAST",
#             "EAST",
#             "WEST",
#             "NORTH",
#             "WEST",
#             "EAST",
#             "EAST",
#             "SOUTH",
#             "NORTH",
#             "WEST",
#         ]
#     )
# )


def duty_free(price, discount, holiday_cost):
    return math.ceil(holiday_cost / (price * (discount * 0.01)))


# print(duty_free(12, 50, 1000))


def merge_arrays(arr1, arr2):
    return sorted(set(arr1 + arr2))


# print(merge_arrays([1, 3, 5, 7, 9], [1, 4, 10, 8, 6, 4, 2]))


def check_exam(arr1, arr2):
    res = 0
    for idx in range(len(arr1)):
        if arr2[idx] != "":
            if arr2[idx] != arr1[idx]:
                res -= 1
            else:
                res += 4

    return res if res >= 0 else 0


# print(check_exam(["b", "c", "b", "a"], ["", "a", "a", "c"]))


def increment_string(strng):
    stripped = strng.rstrip("1234567890")
    ints = strng[len(stripped) :]

    if len(ints) == 0:
        return strng + "1"
    else:
        length = len(ints)

        new_ints = 1 + int(ints)

        # pad new_ints with zeroes on the left
        new_ints = str(new_ints).zfill(length)

        return stripped + new_ints
    # numIdx = None
    # for idx in range(len(strng) - 1, 0, -1):
    #     if not strng[idx].isnumeric():
    #         numIdx = idx + 1
    #         break
    # if numIdx and numIdx < len(strng):
    #     number = strng[numIdx::]
    #     string = strng[:numIdx]
    #     lenDif = len(number) - len(f"{int(number) + 1}")
    #     zeros = "0" * lenDif
    #     return f"{string}{zeros}{int(number) + 1}"

    # return f"{strng}1"


# print(increment_string("foo001"))


def rain_amount(mm):
    if mm < 40:
        return f"You need to give your plant {40 - mm}mm of water"
    else:
        return "Your plant has had more than enough water for today!"


# print(rain_amount(39))


def feast(beast, dish):
    # first = beast[0] == dish[0]
    # last = beast[-1] == dish[-1]
    # if first and last:
    #     return True
    # else:
    #     return False

    return True if beast[0] == dish[0] and beast[-1] == dish[-1] else False


# print(feast("brown bear", "bear claw"))
# print(feast("great blue heron", "garlic naan"))


def area_or_perimeter(l, w):
    return l * w if l == w else (2 * l) + (2 * w)


# print(area_or_perimeter(4, 4))  # 16
# print(area_or_perimeter(6, 10))  # 32


def square(n):
    return n**2


# print(square(50))
import datetime


def check_coupon(entered_code, correct_code, current_date, expiration_date):
    # dt = datetime(current_date)
    return current_date


# print(check_coupon("123", "123", "September 5, 2014", "October 1, 2014"))


def enough(cap, on, wait):
    space = cap - on - wait
    if space > -1:
        return 0
    else:
        return -space


# print(enough(10, 5, 5))
# print(enough(100, 60, 50))
# print(enough(20, 5, 5))


def capitalize(s):
    even = ""
    odd = ""
    for idx, el in enumerate(s):
        if idx % 2 > 0:  # odd
            even = even + el.upper()
            odd = odd + el.lower()
        else:
            even = even + el.lower()
            odd = odd + el.upper()

    return [odd, even]


# print(capitalize("hello"))


def say_hello(name, city, state):
    return f"Hello, {name[0]} {name[1]}! Welcome to {city}, {state}"


# print(say_hello(["John", "Smith"], "Phoenix", "Arizona"))


def find_it(seq):
    even = []
    odd = []
    for int in seq:
        if int in odd:
            even.append(int)
            odd.remove(int)
        elif int in even:
            odd.append(int)
            even.remove(int)
        else:
            odd.append(int)
    return odd[0]


# print(find_it([1, 2, 2, 3, 3, 3, 4, 3, 3, 3, 2, 2, 1]))


def stock_list(list_of_art, list_of_cat):
    hash = {}
    for cat in list_of_cat:
        hash[cat] = 0
    for art in list_of_art:
        letter = art.split(" ")[0][0]
        num = int(art.split(" ")[1])
        if letter in list_of_cat:
            hash[letter] += num

    values = list(hash.values())
    res = []
    for idx, cat in enumerate(list_of_cat):
        res.append(f"({cat} : {values[idx]})")
    return (" - ").join(res)


# "(A : 0) - (B : 1290) - (C : 515) - (D : 600)"

# print(
#     stock_list(
#         ["ABAR 200", "CDXE 500", "BKWR 250", "BTSQ 890", "DRTY 600"],
#         ["A", "B"],
#     )
# )


def whatday(num):
    days = [
        "",
        "Sunday",
        "Monday",
        "Tuesday",
        "Wednesday",
        "Thursday",
        "Friday",
        "Saturday",
    ]
    if num < 8 and num > 0:
        return days[num]
    else:
        return "Wrong, please enter a number between 1 and 7"


# print(whatday(9))


def sum_array(arr):
    if not arr or not len(arr) or len(arr) == 1:
        return 0
    arr.sort()
    arr.pop()
    arr.pop(0)
    if not len(arr):
        return 0
    return sum(arr)


# print(sum_array([6]))


def remove_exclamation_marks(s):
    # res = ""
    # for x in s:
    #     if x != "!":
    #         res += x
    # return res

    return "".join([x for x in s if x != "!"])


# print(remove_exclamation_marks("Hello World!"))


def high(x):
    highest = 0
    highestW = ""
    alph = "abcdefghijklmnopqrstuvwxyz"
    letterHash = {}
    for idx, letter in enumerate(list(alph)):
        letterHash[letter] = idx + 1
    listWords = x.split(" ")
    for word in listWords:
        total = 0
        for letter in word:
            total += letterHash[letter]
        if total > highest:
            highest = total
            highestW = word

    return highestW


# print(high("man i need a taxi up to ubud"))


def remove_url_anchor(url):
    if "#" in url:
        idx = url.index("#")
        return url[:idx]
    else:
        return url


# print(remove_url_anchor("www.codewars.comabout"))


def race(v1, v2, g):
    if v1 >= v2:
        return None

    time_in_hours = g / (v2 - v1)  # lead / (2nd person speed - 1st person speed)
    hours = int(time_in_hours)
    minutes = int((time_in_hours - hours) * 60)
    seconds = int(((time_in_hours - hours) * 60 - minutes) * 60)

    return [hours, minutes, seconds]


def mxdiflg(a1, a2):
    if len(a1) == 0 or len(a2) == 0:
        return -1
    a1Arr = []
    a2Arr = []
    for a in a1:
        a1Arr.append(len(a))
    for a in a2:
        a2Arr.append(len(a))
    a1Max = max(a1Arr)
    a1Min = min(a1Arr)
    a2Max = max(a2Arr)
    a2Min = min(a2Arr)
    return max(a1Max - a2Min, a2Max - a1Min)


# print(
#     mxdiflg(
#         [
#             "hoqq",
#             "bbllkw",
#             "oox",
#             "ejjuyyy",
#             "plmiis",
#             "xxxzgpsssa",
#             "xxwwkktt",
#             "znnnnfqknaz",
#             "qqquuhii",
#             "dvvvwz",
#         ],
#         ["cccooommaaqqoxii", "gggqaffhhh", "tttoowwwmmww"],
#     )
# )


def powers_of_two(n):
    return [2**x for x in range(n + 1)]


# print(powers_of_two(2))


def hero(bullets, dragons):

    return True if bullets / 2 > dragons else False


def count(s):
    hash = {}
    for x in s:
        if x in hash:
            hash[x] += 1
        else:
            hash[x] = 1
    return hash


def to_alternating_case(string):
    res = ""

    for letter in string:
        if letter.isalpha():  # is it a letter?
            if letter.isupper():
                res += letter.lower()
            else:
                res += letter.upper()

        else:
            res += letter
    return res


def list_squared_pre(n):
    res = []
    for x in range(1, n + 1):

        if n % x == 0:
            res.append(x * x)

    total = sum(res)
    sqrt = math.sqrt(total)
    if sqrt == int(sqrt):
        return math.sqrt(total)
    return False


def list_squared(m, n):
    res = []
    for x in range(m, n + 1):
        sqrt = list_squared_pre(x)
        if sqrt:
            res.append([x, int(sqrt) * int(sqrt)])
    return res


# print(list_squared(1, 250))


def list_squared(m, n):
    result = []
    for num in range(m, n + 1):
        divisors = set()
        for i in range(1, int(math.sqrt(num) + 1)):
            if num % i == 0:
                divisors.add(i**2)
                divisors.add(int(num / i) ** 2)
        total = sum(divisors)
        sr = math.sqrt(total)
        if sr - math.floor(sr) == 0:
            result.append([num, total])
    return result


def find_even_index(arr):
    # leftIdx = 0
    # left = arr[leftIdx]
    # rightIdx = len(arr) - 1
    # right = arr[rightIdx]

    # while leftIdx is not rightIdx:
    #     if rightIdx == -1:
    #         return -1
    #     if left >= right:
    #         right = right + arr[rightIdx - 1]
    #         rightIdx -= 1
    #         # print(f"{leftIdx} - {rightIdx}")

    #     if right > left:
    #         # if not arr[leftIdx + 1]:
    #         #     return -1
    #         left = left + arr[leftIdx + 1]
    #         leftIdx += 1

    # # print(left)
    # # print(right)
    # return leftIdx\
    left = 0
    right = sum(arr[1:])
    for idx in range(len(arr)):
        if idx == 0:
            left = 0
        else:
            left = sum(arr[:idx])
        if idx == len(arr) - 1:
            right = 0
        else:
            right = sum(arr[idx + 1 :])
        if left == right:
            return idx
    return -1


# print(find_even_index([0, 8]))
# print(find_even_index([1, 100, 50, -51, 1, 1]))


def queue_time(customers, n):
    queue = [0] * n
    for x in range(len(customers)):
        shortest = queue.index(min(queue))
        queue[shortest] += customers[x]

    return max(queue)


# print(queue_time([1, 2, 3, 4, 5], 100))


def find_short(s):
    l = s.split(" ")
    for idx, word in enumerate(l):
        l[idx] = len(word)
    return min(l)


# print(find_short("bitcoin take over the world maybe who knows perhaps"))


def two_sum(numbers, target):
    for index in range(len(numbers), 0, -1):
        idx = index - 1
        if target - numbers[idx] in numbers[:idx]:
            return (idx, numbers.index(target - numbers[idx]))


# print(two_sum([2, 2, 3], 4))


def sum_mul(n, m):
    res = 0
    if n == m or m < n:
        return "INVALID"
    else:
        for number in range(0, m, n):
            res += number
    return res


# print(sum_mul(2, 9))


def distinct(seq):
    res = []
    sortedSeq = sorted(seq)
    for num in sortedSeq:
        if num not in res:
            res.append(num)
    return res


# print(distinct([1, 2, 2, 3, 3, 4, 4, 7, 5, 6, 7, 7, 7]))


def sort_by_length(arr):
    return sorted(arr, key=len)
    # res = []
    # hash = {}
    # for letter in arr:
    #     hash[len(letter)] = letter

    # sortH = sorted(hash.keys())
    # for h in sortH:
    #     res.append(hash[h])
    # return res


# print(sort_by_length(["Telescopes", "Glasses", "Eyes", "Monocles"]))


def share_price(invested, changes):
    total = invested
    for c in changes:
        total = total + (total * (c * 0.01))
    return "{:.2f}".format(round(total, 2))


def multiplication_table(size):
    return [[n * num for n in range(1, size + 1)] for num in range(1, size + 1)]


# print(multiplication_table(0))


def sum_pairs(ints, s):
    cache = set()
    for i in ints:
        if s - i in cache:
            return [s - i, i]
        cache.add(i)


# print(sum_pairs([1, 2, 3, 4, 1, 0], 2))
# print(sum_pairs([10, 5, 2, 3, 7, 5], 10))


def number(bus_stops):
    total = 0
    for pair in bus_stops:
        diff = pair[0] - pair[1]
        total += diff
    return total


# print(number([[10, 0], [3, 5], [5, 8]]))


def get_size(w, h, d):
    area = 2 * ((w * h) + (w * d) + (h * d))
    volume = w * h * d
    return [area, volume]


class Ball(object):
    def __init__(self, type="regular"):
        self.ball_type = type


# print(Ball().ball_type)


def better_than_average(class_points, your_points):
    return your_points > sum(class_points) / len(class_points)


def get_real_floor(n):
    if n == 15:
        return 13
    elif n > 13:
        return n - 2
    elif n >= 1:
        return n - 1
    else:
        return n


def check_for_factor(base, factor):
    return base % factor == 0


def longest_consec(strarr, k):
    if len(strarr) == 0 or k > len(strarr) or k <= 0:
        return ""
    lengths = []
    for word in strarr:
        lengths.append(len(word))
    longestLength = 0
    longestW = ""
    print(lengths)
    for x in range(0, len(strarr)):
        print(x)
        if sum(lengths[x : x + k]) > longestLength:
            longestLength = sum(lengths[x : x + k])
            longestW = "".join(strarr[x : x + k])
    return longestW


# print(
#     longest_consec(
#         [
#             "ejjjjmmtthh",
#             "zxxuueeg",
#             "aanlljrrrxx",
#             "dqqqaaabbb",
#             "oocccffuucccjjjkkkjyyyeehh",
#         ],
#         0,
#     )
# )


def hex_to_dec(s):
    return int(s, 16)


def predict_age(age_1, age_2, age_3, age_4, age_5, age_6, age_7, age_8):
    def multiple(n):
        return n * n

    multiply = list(
        map(multiple, [age_1, age_2, age_3, age_4, age_5, age_6, age_7, age_8])
    )

    totalSum = sum(multiply)

    square = math.sqrt(totalSum)
    return int(square / 2)


# print(predict_age(65, 60, 75, 55, 60, 63, 64, 45))
# Take a list of ages when each of your great-grandparent died.
# Multiply each number by itself.
# Add them all together.
# Take the square root of the result.
# Divide by two.


def rev_rot(strng, sz):
    if sz <= 0 or str == "":
        return ""
    subString = []
    for x in range(0, len(strng), sz):
        if len(strng[x : x + sz]) == sz:
            subString.append(strng[x : x + sz])
    for idx, el in enumerate(subString):
        listedEl = list(el)
        intList = map(int, listedEl)
        if not sum(intList) % 2:
            subString[idx] = ("").join(listedEl[::-1])
        else:
            first = listedEl[0]
            new = []
            for x in range(1, len(listedEl)):
                new.append(el[x])
            new.append(first)
            subString[idx] = ("").join(new)
    return ("").join(subString)


# If the sum of a chunk's digits is divisible by 2, reverse that chunk; otherwise rotate it to the left by one position.
# 33047 91089 28157
# print(rev_rot("733049910872815764", 5))


def no_boring_zeros(n):
    stringN = list(f"{n}")
    if n == 0:
        return 0
    trigger = True
    for el in range(len(stringN), 0, -1):
        if trigger:
            if stringN[el - 1] == "0":
                stringN[el - 1] = ""
            else:
                trigger = False
    return int("".join(stringN))


# print(no_boring_zeros(2016))
# print(no_boring_zeros(-100))
# print(no_boring_zeros(0))


def apple(x):
    if (int(x) * int(x)) > 1000:
        return "It's hotter than the sun!!"
    else:
        return "Help yourself to a honeycomb Yorkie for the glovebox."

    # Your job is simple, if x squared is more than 1000, return It's hotter than the sun!!, else, return Help yourself to a honeycomb Yorkie for the glovebox.


# print(apple("50"))


def words_to_marks(s):
    alphabet = list("abcdefghijklmnopqrstuvwxyz")
    hash = {}
    sum = 0
    for idx, letter in enumerate(alphabet):
        hash[letter] = idx + 1
    for letter in list(s):
        sum += hash[letter]

    return sum


def problem(a):
    if isinstance(a, str):
        return "Error"
    else:
        return (a * 50) + 6


# print(problem("happy"))

# Make a function that returns the value multiplied by 50 and increased by 6. If the value entered is a string it should return "Error".


def containsDuplicate(nums):
    seen = set()
    for num in nums:
        if num in seen:
            return True
        seen.add(num)
    return False

    # print(
    containsDuplicate(
        [
            274,
            -735,
            -911,
            80,
            454,
            -511,
            922,
            -775,
            985,
            -669,
            -463,
            -896,
            -629,
            -586,
            910,
            -361,
            288,
            -375,
            88,
            556,
            -578,
            -406,
            -87,
            25,
            377,
            -635,
            -445,
            -289,
            646,
            -962,
            -487,
            -924,
            -968,
            -962,
            502,
            36,
            129,
            -611,
            54,
            -27,
            -496,
            915,
            -84,
            -782,
            349,
            678,
            332,
            -114,
            345,
            14,
            119,
            710,
            821,
            -194,
            988,
            38,
            -369,
            409,
            -559,
            -529,
            -298,
            -593,
            705,
        ]
    )


# )


def isAnagram(s, t):
    hashSet1 = {}
    hashSet2 = {}
    for l in s:
        if l in hashSet1:
            hashSet1[l] += 1
        else:
            hashSet1[l] = 1
    for l in t:
        if l in hashSet2:
            hashSet2[l] += 1
        else:
            hashSet2[l] = 1
    if hashSet1 == hashSet2:
        return True
    else:
        return False


# print(isAnagram("anagram", "nagaream"))


def sum_two_smallest_numbers(numbers):
    numbers.sort()
    return numbers[0] + numbers[1]


def calculate_years(principal, interest, tax, desired):
    years = 0
    bank = principal
    while bank < desired:
        years += 1
        newInterest = bank * interest
        newTax = newInterest * tax
        bank = bank + newInterest - newTax
    return years


# print(calculate_years(1000, 0.05, 0.18, 1100))


def people_with_age_drink(age):
    if age < 14:
        return "drink toddy"
    elif age < 18:
        return "drink coke"
    elif age < 21:
        return "drink beer"
    else:
        return "drink whisky"


# print(people_with_age_drink(13))
# print(people_with_age_drink(17))
# print(people_with_age_drink(18))
# print(people_with_age_drink(20))
# print(people_with_age_drink(30))


def string_clean(s):
    listS = list(s)
    res = []
    for letter in listS:
        x = letter.isnumeric()
        if not x:
            res.append(letter)
    return "".join(res)


# print(string_clean("This looks5 grea8t!"))


def derive(coefficient, exponent):
    return f"{coefficient * exponent}^{exponent - 1}"


# print(derive(2, 3))


def no_odds(values):
    return [x for x in values if not x % 2]


# print(no_odds([1, 2, 3, 4, 5, 6, 7]))


def sum_digits(number):
    total = 0
    string = f"{number}"
    for number in string:
        if number.isnumeric():
            total += int(number)

    return total


print(sum_digits(10))
