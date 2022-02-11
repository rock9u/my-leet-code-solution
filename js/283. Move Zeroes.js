/**
 * @param {number[]} nums
 * @return {void} Do not return anything, modify nums in-place instead.
 */
var moveZeroes = function (nums) {
  let nonZeroCount = 0
  nums.forEach((el, i) => {
    if (el) {
      nums[nonZeroCount] = el
      nonZeroCount++
    }
  })
  for (let i = nonZeroCount; i < nums.length; i++) {
    nums[i] = 0
  }
}
