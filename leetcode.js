
let problem3 = function (s) {
    let dict = {}
    let count = 0
    let left = 0; right = 0;
    for (; right < s.length; right++) {
        let letter = s[right]
        if (dict[letter] >= left) { //if the letter position 
            left = dict[letter] + 1
        }
        (dict[letter] = right)

        count = Math.max(right - left + 1, count)
    }
    return count
}

// console.log(problem3('abcabcbb'))

let problem5 = function (s) {
    let res

    for (let i = 0; i < s.length; i++) {
        let left = i; right = i + 1
        let letter = s[i]
        let nextLetter = s[i + 1]
        if (letter === nextLetter) {

        }

    }
}

// console.log(problem5('abba'))

let isPalindrome = function (x) {
    x = x.toString()
    let res = true
    let mid = (x.length - 1) / 2
    for (let i = 0; i < mid; i++) {
        let left = x[i]
        let right = x[x.length - 1 - i]

        console.log(`${left} = ${right}`)
        if (left != right) {
            return false
        }
    }
    return res


};

// console.log(isPalindrome(1221))

let romanToInt = function (s) {
    let romanDict = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000
    }
    let arr = ["I", "V", "X", "L", "C", "D", "M"]
    let passed = []
    let res = 0;
    for (let i = s.length - 1; i >= 0; i--) {
        let letter = s[i].toUpperCase()
        if (passed.find((x) => x === letter)) {
            res = res - romanDict[letter]
        } else if (arr.indexOf(letter) > 0) {
            res = res + romanDict[letter]
            let sliced = arr.slice(0, arr.indexOf(letter))
            passed.push(...sliced)
        } else {

            res = res + romanDict[letter]
        }
    }
    return res
}

// console.log(romanToInt('MCMXCIV'))

let longestCommonPrefix = function (strs) {
    let res = ''
    let count = 0
    let firstWord = strs[0]
    let left = 0
    for (let i = 0; i <= firstWord.length; i++) {
        let con = true
        let letters = firstWord.slice(left, i)
        strs.forEach(word => {
            let newLetters = word.slice(left, i)
            if (newLetters !== letters) {
                con = false
            }
        });
        if (con === false) {
            // left++
            // i--
            return res
        } else {
            if ((i - left) > count) {
                count = i - left
                res = letters
            }
        }
    }
    return res
}

// console.log(longestCommonPrefix(["a"]))

let isValid = function (s) {
    const pairs = {
        ")": "(",
        "}": "{",
        "]": "["
    }

    let stack = []

    if (s.length % 2 === 1) {
        return false
    }

    for (let i = 0; i < s.length; i++) {
        let x = s[i]
        if (!pairs[x]) {
            stack.push(x)
        } else if (pairs[x]) {
            if (pairs[x] != stack[stack.length - 1]) {
                return false
            } else {
                stack.pop()
            }
        }

    }

    return (!stack.length > 0)
};

// console.log(isValid("{[{}]}"))


let removeDuplicates = function (nums) {
    let index = 1
    for (let i = 0; i < nums.length - 1; i++) {
        if (nums[i] != nums[i + 1]) {
            nums[index] = nums[i + 1]
            index++
        }
    }
    return index
};

// console.log(removeDuplicates([0, 0, 1, 1, 1, 2, 2, 3, 3, 4]))


var removeElement = function (nums, val) {
    let index = 0
    for (let i = 0; i < nums.length; i++) {
        let int = nums[i]
        if (int != val) {
            nums[index] = int
            index++
        }
    }
    return index
};

// console.log(removeElement([0, 1, 2, 2, 3, 0, 4, 2], 2))

var strStr = function (haystack, needle) {
    let index = -1
    for (let i = 0; i <= haystack.length - needle.length; i++) {
        let letter = haystack[i]
        if (letter === needle[0]) {
            let word = haystack.slice(i, i + needle.length)
            if (word === needle) {
                return i
            }
        }
    }
    return index
};

// console.log(strStr("leetcode", "leeto"))

let mergeTwoLists = function (list1, list2) {
    let l1Idx = 0;
    let l2Idx = 0;
    let res = []
    for (let i = 1; i <= list1.length + list2.length; i++) {
        if (list1[l1Idx] <= list2[l2Idx]) {
            res.push(list1[l1Idx])
            l1Idx++
        } else {
            res.push(list2[l2Idx])
            l2Idx++
        }
    }
    return res
}

// console.log(mergeTwoLists([], []))

let searchInsert = function (nums, target) {
    for (let i = 0; i < nums.length; i++) {
        let num = nums[i]
        let next = nums[i + 1]
        if (target <= num) {
            return i
        }
        if (target > num && target < next) {
            return i + 1
        }
    }
    return nums.length
};

let lengthOfLastWord = function (s) {
    let sArr = s.split(" ")
    for (let i = sArr.length - 1; i >= 0; i--) {
        let str = sArr[i]
        if (str) {
            return str.length
        }
    }
}

// console.log(lengthOfLastWord("   fly me   to   the moon  "))

let plusOne = function (digits) {
    let multiplier = digits.length - 1
    let number = 0
    for (let i = 0; i < digits.length; i++) {
        let num = digits[i]
        number = number + (10 ** multiplier) * num
        multiplier--

    }



    return number
};

// console.log(plusOne([6, 1, 4, 5, 3, 9, 0, 1, 9, 5, 1, 8, 6, 7, 0, 5, 5, 4, 3]))


let addBinary = function (a, b) {
    let binaryDec = function (x) {
        let multiple = 0;
        let num = 0;
        for (let i = x.length - 1; i >= 0; i--) {
            let number = x[i]
            if (+number) {
                num = num + (2 ** multiple)
                multiple++
            } else {
                multiple++
            }

        }
        return +num
    }

    let sum = binaryDec(a) + binaryDec(b)

    return (sum.toString(2))
};

// console.log(addBinary("11", "1"))

let climbStairs = function (n) {
    debugger
    let res = 0
    if (!n || n === 1) {
        return 1
    }
    if (n > 1) {
        let left = climbStairs(n - 1)
        let right = climbStairs(n - 2)
        res = left + right
        return res
    }
}

console.log(climbStairs(10))