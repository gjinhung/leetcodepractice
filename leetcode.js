
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

console.log(problem3('abcabcbb'))

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

console.log(problem5('abba'))