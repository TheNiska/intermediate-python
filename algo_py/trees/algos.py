from tree_models import TreeNode


def preorderTraversal(root: TreeNode) -> list[int]:
    if root is None:
        return []

    result = [root.val]

    if root.left:
        result += preorderTraversal(root.left)

    if root.right:
        result += preorderTraversal(root.right)

    return result


if __name__ == '__main__':
    trea = TreeNode(55,
                    TreeNode(40,
                             TreeNode(30,
                                      TreeNode(10),
                                      TreeNode(10)),
                             TreeNode(20,
                                      TreeNode(9),
                                      TreeNode(9))),
                    TreeNode(50,
                             TreeNode(29,
                                      TreeNode(8),
                                      TreeNode(7)),
                             TreeNode(28,
                                      TreeNode(6),
                                      TreeNode(5))))
    res = preorderTraversal(trea)
    print(res)
