/**
 * Definition for singly-linked list.
 * function ListNode(val, next) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.next = (next===undefined ? null : next)
 * }
 */
/**
 * @param {ListNode} head
 * @return {boolean}
 */
var isPalindrome = function (head) {
  // find length
  // break in half
  // satring from half reverse the linked list
  // check if identical
  let p2 // p2 is the new starting head for reversed ll, it will be lost in the process if no variable to store it
  function reverse(head, prev) {
    if (!head) {
      return head
    }
    if (head && !head.next) {
      head.next = prev
      p2 = head
      return prev
    }
    let temp = reverse(head.next, head)
    temp.next = prev
    return prev
  }

  let length = 0
  let p = head
  while (p) {
    length++
    p = p.next
  }
  if (length < 2) {
    return true
  }
  let half = Math.ceil(length / 2) - 1
  let halfHead = head
  for (let i = 0; i < half; i++) {
    halfHead = halfHead.next
  }

  halfHead.next = reverse(halfHead.next, null)
  let p1 = head
  while (p2) {
    if (p1.val != p2.val) {
      return false
    }
    p1 = p1.next
    p2 = p2.next
  }
  return true
}
