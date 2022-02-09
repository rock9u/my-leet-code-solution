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
var diameterOfBinaryTree = function (root) {
  let dia = 0
  function depth(node) {
    if (!node) return 0
    let depthLeft = depth(node.left)
    let depthRight = depth(node.right)
    dia = Math.max(dia, depthLeft + depthRight)
    return Math.max(depthLeft, depthRight) + 1
  }

  depth(root)
  return dia
}

//TODO: revisit
