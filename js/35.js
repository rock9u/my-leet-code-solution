/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number}
 */
var searchInsert = function (nums, target) {
  function binarySearch(start, end) {
    let mid = start + Math.floor((end - start) / 2)
    if (nums[mid] == target) return mid
    if (start == end) return nums[start] > target ? start : start + 1

    return nums[mid] > target
      ? binarySearch(start, mid)
      : binarySearch(mid + 1, end)
  }
  return binarySearch(0, nums.length - 1)
}
