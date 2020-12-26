# -*- coding: utf-8 -*-

class TreeNode:

    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def create_binary_tree(input_list: list):
    """
    构建二叉树
    :param input_list:
    :return:
    """
    if input_list is None or len(input_list) == 0:
        return None

    data = input_list.pop(0)
    if data is None:
        return None

    node = TreeNode(data)
    node.left = create_binary_tree(input_list)
    node.right = create_binary_tree(input_list)

    return node


def pre_order_traversal(node: TreeNode):
    """
    前序遍历
    :param node:
    :return:
    """
    if node is None:
        return None

    print(node.data)
    pre_order_traversal(node.left)
    pre_order_traversal(node.right)
    return node


def in_order_traversal(node: TreeNode):
    """
    中序遍历
    :param node:
    :return:
    """
    if node is None:
        return None

    in_order_traversal(node.left)
    print(node.data)
    in_order_traversal(node.right)

    return node


def post_order_traversal(node: TreeNode):
    """
    后序遍历
    :param node:
    :return:
    """
    if node is None:
        return
    post_order_traversal(node.left)
    post_order_traversal(node.right)
    print(node.data)
    return node


def pre_order_traversal_with_stack(node: TreeNode):
    """
    二叉树非递归前序遍历
    :param node:
    :return:
    """
    stack = []
    while node is not None or len(stack) > 0:
        while node is not None:
            print(node.data)
            stack.append(node)
            node = node.left

        if len(stack) > 0:
            node = stack.pop()
            node = node.right


from queue import Queue


def level_order_traversal(node):
    queue = Queue()
    queue.put(node)
    while not queue.empty():
        node = queue.get()
        print(node.data)
        if node.left is not None:
            queue.put(node.left)
        if node.right is not None:
            queue.put(node.right)


if __name__ == '__main__':
    my_input_list = list([3, 2, 9, None, None, 10, None, None, 8, None, 4])
    print(my_input_list)
    root = create_binary_tree(my_input_list)
    print(root)
    print("前序遍历：")
    pre_order_traversal(root)
    print("中序遍历：")
    in_order_traversal(root)
    print("后序遍历：")
    post_order_traversal(root)
    print("二叉树非递归前序遍历：")
    pre_order_traversal_with_stack(root)
    print("层序遍历:")
    level_order_traversal(root)