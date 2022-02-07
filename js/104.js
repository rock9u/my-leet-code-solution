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
 * @return {number}
 */
var maxDepth = function (root) {
  if (!root || Object.is(root.val, null)) {
    return 0
  }
  let depth = 0
  let queue = [root]
  let nextDepthQueue = []
  while (queue.length) {
    let pNode = queue.shift()
    bfs(nextDepthQueue, pNode)

    if (!queue.length) {
      depth++
      queue = nextDepthQueue
      nextDepthQueue = []
    }
  }

  return depth
}

function bfs(queue, root) {
  if (isNull(root)) {
    return
  }
  if (!isNull(root.left)) {
    queue.push(root.left)
  }
  if (!isNull(root.right)) {
    queue.push(root.right)
  }
}

function isNull(root) {
  return !root || Object.is(root.val, null) || Object.is(root.val, undefined)
}
