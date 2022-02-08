/**
 * @param {string} s
 * @return {boolean}
 */
var isValid = function (s) {
  let stack = []

  if (s.length % 2) return false
  let starts = ['(', '{', '[']
  let closes = [')', '}', ']']
  let validList = ['()', '{}', '[]']
  for (let i = 0; i < s.length; i++) {
    if (starts.includes(s[i])) stack.push(s[i])
    if (closes.includes(s[i])) {
      let match = `${stack.slice(-1)[0]}${s[i]}`
      if (validList.includes(match)) {
        stack.pop()
      } else {
        return false
      }
    }
  }
  return stack.length == 0
}
