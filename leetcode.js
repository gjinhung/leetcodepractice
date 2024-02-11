let problem3 = function (s) {
    let res = 0
    let dict = {}
    let count = 0
    for (let end = 0; end < s.length; end++) {
        let letter = s[end]
        if (dict[letter]) {
            if (count > res) {
                res = count
            }
            dict = {}
            dict[letter] = 1
            count = 1
            console.log('letter exists')
        } else {
            count++
            console.log(count)
            dict[letter] = 1
            if (count > res) {
                res = count
            }
            console.log('letter does not exists')
        }
    }
    return res
}

console.log(problem3('dvdf'))