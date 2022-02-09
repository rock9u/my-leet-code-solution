/**
 * @param {number[]} prices
 * @return {number}
 */
var maxProfit = function (prices) {
  let min = prices[0]
  let max = prices[0]
  let diff = 0
  for (let i = 1; i < prices.length; i++) {
    if (min > prices[i]) {
      min = prices[i]
      max = min
    }

    if (max < prices[i]) {
      max = prices[i]
      diff = Math.max(diff, max - min)
    }
  }
  return diff
}
