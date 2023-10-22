from trees.tree_models import TreeNode
from typing import Optional


def preorderTraversal(root: Optional[TreeNode]) -> list[int]:
    if not root:
        return []

    result = [root.val]

    if root.left:
        result += preorderTraversal(root.left)

    if root.right:
        result += preorderTraversal(root.right)

    return result


def inorderTraversal(root: Optional[TreeNode]) -> list[int]:
    result = []
    if not root:
        return result

    if root.left:
        result += inorderTraversal(root.left)

    result += [root.val]

    if root.right:
        result += inorderTraversal(root.right)

    return result


def postorderTraversal(root: Optional[TreeNode]) -> list[int]:
    result = []
    if not root:
        return result

    if root.left:
        result += postorderTraversal(root.left)

    if root.right:
        result += postorderTraversal(root.right)

    result += [root.val]
    return result
