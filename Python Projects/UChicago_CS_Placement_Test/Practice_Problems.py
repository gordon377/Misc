#WARM-UP

#All That Wasted Space

def total_wasted_space(shipments: list[int], bin_size: int) -> int:
    '''
    This function takes a list of integers, representing the number of items
    in each shipment, and a bin size, and computes the total wasted
    space across all shipments.

    Arguments:
        shipments: a list of integers
        bin_size: the capacity of each bin (all bins have the same capacity)

    Returns:
        The total wasted space across all shipments.
    '''

    # Your code here

    sum = 0

    for x in shipments:
        sum += bin_size-(x%bin_size)

    return sum


testList = [23, 31]

print(total_wasted_space(testList, 10))


#Expand

def expand(lb: int, ub: int, skip: list[int]) -> list[int]:
    """
    Create a list of integers from a lower bound to an upper bound,
        inclusive on both sides, excluding any value that is a divisor
        of a value in list of values to skip.

    Inputs:
        lb [int]: lower bound
        ub [int]: upper bound
        skip list[int]: list of multiples to skip

    Returns list[int]: List of integers from lb to ub (inclusive)
        except for any integer that is a divisor of a value in skip.
    """
    assert lb >= 2
    assert lb <= ub

    # TODO: Implement this function.
    expandList = []
    toSkip = False

    while lb <= ub:
        for x in skip:
            if lb%x == 0:
                toSkip = True
                break
        if toSkip == False: expandList.append(lb)
        toSkip = False
        lb+=1

    return expandList

lowerBound = 2
upperBound = 9
skip = [2]

print(expand(lowerBound, upperBound, skip))

#COMPUTATIONAL THINKING

#Summing Tiles

from tile import Tile


def sum_tiles(matrix: list[list[int]], tiles: list[Tile]) -> int:
    """
    Return the sum of the tile values.

    Inputs:
      matrix: the matrix of values
      tiles: a list of Tiles.

    Return: the sum of the tile values.
    """
    # TODO: complete this function.

    sum = 0

    for x in tiles:
        r_range = x.r1-x.r0
        c_range = x.c1-x.c0
        for i in range(r_range):
            for p in range(c_range):
                try:
                    sum += matrix[x.r0+i][x.c0+p]
                except IndexError: #Catches when trying to access values outside the matrix bounds
                    continue
            i+=1

    return sum


#Room Cleaner (Do Later)


#Object-Oriented Programmming

#Scooter Pool

from location import Location
from scooter import Scooter
from scooter_pool import ScooterPool

scooterGroup = ScooterPool()

print(scooterGroup.add_scooter("ID1", 0, 2))
print(scooterGroup.add_scooter("ID2", 0, 4))
print(scooterGroup.add_scooter("ID3", 2, 7))
print(scooterGroup.add_scooter("ID4", 0, 5))

print(scooterGroup.num_scooters_in_range(Location(2,2),4))


#Orders

from line_item import LineItem
from order import Order

Apples = LineItem("Apple", 1, 5)
Oranges = LineItem("Orange", 2, 3)

grouping = Order(12.5)

grouping.add_line_item(Apples)
grouping.add_line_item(Oranges)
print(grouping.total_cost())

#RECURSION

#Tree Sum

from tree_sum import tree_sum, mk_node, mk_sample_tree, BinaryTree

print (tree_sum(mk_sample_tree(), 30))