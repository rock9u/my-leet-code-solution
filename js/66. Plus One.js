/**
 * @param {number[]} digits
 * @return {number[]}
 */
var plusOne = function (digits) {
  function plusOneSingle(digit) {
    return { carry, digit: newDigit }
  }

  let res = []
  let carry = 1
  for (let i = digits.length - 1; i >= 0; i--) {
    if (carry) {
      carry = digits[i] == 9 ? true : false
      let newDigit = carry ? 0 : digits[i] + 1
      res = [newDigit, ...res]
    } else res = [digits[i], ...res]
  }
  return carry ? [carry, ...res] : res
}
