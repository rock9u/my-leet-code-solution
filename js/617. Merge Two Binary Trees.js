/**
 * Definition for a binary tree node.
 * function TreeNode(val, left, right) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.left = (left===undefined ? null : left)
 *     this.right = (right===undefined ? null : right)
 * }
 */
/**
 * @param {TreeNode} root1
 * @param {TreeNode} root2
 * @return {TreeNode}
 */
var mergeTrees = function (root1, root2) {
  function merge(root1, root2) {
    if (!root1) {
      return root2
    }

    if (!root2) {
      return root1
    }

    return new TreeNode(
      root1.val + root2.val,
      merge(root1.left, root2.left),
      merge(root1.right, root2.right)
    )
  }

  return merge(root1, root2)
}
