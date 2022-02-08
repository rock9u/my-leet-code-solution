/**
 * Definition for a binary tree node.
 * function TreeNode(val, left, right) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.left = (left===undefined ? null : left)
 *     this.right = (right===undefined ? null : right)
 * }
 */
/**
 * @param {TreeNode} root
 * @return {boolean}
 */
var isSymmetric = function (root) {
  let queue = [root]

  while (queue.length) {
    let len = queue.length
    let nextQueue = []
    for (let i = 0; i < Math.floor(len / 2); i++) {
      if (queue[i]?.val != queue[len - 1 - i]?.val) return false
    }
    for (let i = 0; i < len; i++) {
      let pNode = queue[i]
      if (pNode) {
        nextQueue.push(pNode.left)
        nextQueue.push(pNode.right)
      }
    }
    queue = nextQueue
  }
  return true
}

//TODO: solve recursively
