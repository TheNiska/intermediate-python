import trees.algos as alg
from trees.tree_models import TreeNode
from analyzer import get_time


def main():
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

    t = get_time(alg.preorderTraversal, trea)
    print(t)


if __name__ == '__main__':
    main()
