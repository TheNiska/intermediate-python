from trees.tree_models import TreeNode


def preorderTraversal(root: TreeNode) -> list[int]:
    if root is None:
        return []

    result = [root.val]

    if root.left:
        result += preorderTraversal(root.left)

    if root.right:
        result += preorderTraversal(root.right)

    return result
