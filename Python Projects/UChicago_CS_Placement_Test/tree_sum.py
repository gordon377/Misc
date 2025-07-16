from binary_tree import BinaryTree
from typing import Union


def tree_sum(tree: Union[BinaryTree, None], ceiling: int) -> int:
    '''
    Compute the sum of all the values in the tree, up to the given
    ceiling (short-circuiting the traversal of the tree is we hit
    that ceiling)

    Arguments:
        tree: a binary tree with integer values
        ceiling: the maximum value for the sum of values

    Returns:
        The sum of all the values in the tree or, if that sum
        is greater than the ceiling value, return the ceiling
        value.
    '''
    # TODO: Write your solution here

    # Is saving into memory more costly than traversing the tree more?

    def sum(tree, node, workingSum, prevNode)->int:
        print("----------------------------------------------------")
        print("Current Node Value " + f"{node.value}")
        if prevNode != None:
            print("Prev Node Value " + f"{prevNode.value}")
        if node.right != None:
            addition = sum(tree, node.right, workingSum, node)
            if type(addition) == list:
                return addition
            if addition == ceiling:
                return ceiling
            workingSum += addition
        elif node.left != None:
            addition = sum(tree, node.left, workingSum, node)
            if type(addition) == list:
                return addition
            if addition == ceiling:
                return ceiling
            workingSum += addition
        if node == tree: #For when only the root is left
            print("Root Condition")
            finalPass = [workingSum]
            return finalPass
        if (node == prevNode.left and prevNode != None):
            prevNode.left = None
        elif (node == prevNode.right and prevNode != None):
            prevNode.right = None
        print("Addition Value: " + f"{node.value}")
        workingSum+=node.value
        print("working sum", f"{workingSum}")
        if workingSum > ceiling:
            print("Ceiling Reached")
            return ceiling
        else:
            addition = sum(tree, tree, workingSum, None)
            if type(addition) == list:
                return addition
            if addition == ceiling:
                return ceiling
            else:
                workingSum += addition
                return workingSum

    result = sum(tree, tree, 0, None)
    if result == ceiling:
        return ceiling
    else:
        finalSum = result[0] + tree.value
        return finalSum


def mk_node(val: int,
            left: Union[BinaryTree, None],
            right: Union[BinaryTree, None]) -> BinaryTree:
    """
    Create a binary tree node, given the node number, value,
    left child, and right child.
    """
    t = BinaryTree(val)
    t.add_left(left)
    t.add_right(right)
    return t

def mk_sample_tree() -> BinaryTree:
    '''
    Make the sample tree from the problem statement.

    Returns:
        The root node of the sample tree
    '''
    return mk_node(10,
               mk_node(5,
                   None,
                   mk_node(15,
                           mk_node(5, None, None),
                           mk_node(10, None, None))),
               mk_node(20,
                   mk_node(5, None, None),
                   mk_node(5,
                           mk_node(15, None, None),
                           None)))