def build_tree(tree):

    tree_dict = {}
    for i, (left, right) in enumerate(tree):
        tree_dict[i] = (left, right)
    return tree_dict


def is_same_tree(t1, t2, root1, root2):

    if root1 == -1 and root2 == -1:
        return True
    if root1 == -1 or root2 == -1:
        return False
    if root1 not in t1 or root2 not in t2:
        return False

    left1, right1 = t1[root1]
    left2, right2 = t2[root2]

    return is_same_tree(t1, t2, left1, left2) and is_same_tree(t1, t2, right1, right2)


def count_subtrees(t1, t2):

    t1_dict = build_tree(t1)
    t2_dict = build_tree(t2)

    count = 0
    for node in t1_dict:
        if is_same_tree(t1_dict, t2_dict, node, 0):
            count += 1

    return count


def solution(t1, t2):
    return count_subtrees(t1, t2)


print(solution([[1, 2], [3, 4], [5, 6], [-1, 7], [8, 9], [-1, -1], [-1, -1], [-1, -1], [-1, -1], [-1, -1]],
               [[-1, 1], [-1,-1]]))
