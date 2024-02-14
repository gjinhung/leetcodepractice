
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
        console.log(dict)
        console.log(letter)
        console.log(`left = ${left} right = ${right} count = ${count}`)
    }
    return count
}

console.log(problem3('abcabcbb'))
