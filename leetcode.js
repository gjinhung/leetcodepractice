
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

console.log(removeElement([0, 1, 2, 2, 3, 0, 4, 2], 2))