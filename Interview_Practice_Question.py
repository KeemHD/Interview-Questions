#Hi, here's your problem today.
# This problem was recently asked by Facebook:
#Given an array and an integer k, rotate
# the array by k spaces. Do this without generating
# a new array and without using extra space.
#8/20/20

def rotate_list(nums, k):
    # Fill this in.
    print(nums,k)

    i = 0
    while i < k:
        temp = nums[0]
        for n in range(len(nums)-1):
            nums[n] = nums[n+1]
        nums[n+1] = temp
        i+=1


a = [1, 2, 3, 4, 5]

print("Rotate Array 8-20")
print("<-----------------START--------------<")
rotate_list(a, 2)
print(a)
# [3, 4, 5, 1, 2]
print("<-----------------START--------------<")

#Hi, here's your problem today.
# This problem was recently asked by Google:

#Given a node in a binary search tree
# (may not be the root), find the next largest
# node in the binary search tree (also known as an
# inorder successor). The nodes in this binary search
# tree will also have a parent field to traverse up the tree.
#8/19/20

class Node:
    def __init__(self, value, left=None, right=None, parent=None):
        self.value = value
        self.left = left
        self.right = right
        self.parent = parent

    def __repr__(self):
        return f"(Value: {self.value}, Left: {self.left}, Right: {self.right})"

def inorder_successor(node):
    # Fill this in.
    print()

tree = Node(3)
tree.left = Node(2)
tree.right = Node(4)
tree.left.parent = tree
tree.right.parent = tree
tree.left.left = Node(1)
tree.left.left.parent = tree.left
tree.right.right = Node(5)
tree.right.right.parent = tree.right
#     3
#    / \
#   2   4
#  /     \
# 1       5
print("Inorder Successor 8-19")
print("<-----------------START--------------<")
print(inorder_successor(tree.left))
# 3
print(inorder_successor(tree.right))
# 5
print("<-----------------END--------------<")
#Hi, here's your problem today.
# This problem was recently asked by Google:

#Given a binary tree, find and return the largest path
# from root to leaf.
#8/18/20

class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

def largest_path_sum(tree):
    # Fill this in.
    print()

tree = Node(1)
tree.left = Node(3)
tree.right = Node(2)
tree.right.left = Node(4)
tree.left.right = Node(5)
#    1
#  /   \
# 3     2
#  \   /
#   5 4
print("Largest Path Sum from Root To Leaf 8-18")
print("<-----------------START--------------<")
print(largest_path_sum(tree))
# [1, 3, 5]
print("<-----------------END--------------<")

#Hi, here's your problem today.
# This problem was recently asked by AirBNB:

#Given a phone number, return all valid words
# that can be created using that phone number.

#For instance, given the phone number 364
#we can construct the words ['dog', 'fog'].
#8/17/20

lettersMaps = {
    1: [],
    2: ['a', 'b', 'c'],
    3: ['d', 'e', 'f'],
    4: ['g', 'h', 'i'],
    5: ['j', 'k', 'l'],
    6: ['m', 'n', 'o'],
    7: ['p', 'q', 'r', 's'],
    8: ['t', 'u', 'v'],
    9: ['w', 'x', 'y', 'z'],
    0: []
}
validWords = ['dog', 'fish', 'cat', 'fog']

def makeWords(phone):
    #Fill this in
    print(phone)

print("Phone Numbers 8-17")
print("<-----------------START--------------<")
print(makeWords('364'))
# ['dog', 'fog']
print("<-----------------END--------------<")


#Hi, here's your problem today.
# This problem was recently asked by Uber:

#Given a list of possible coins in cents,
# and an amount (in cents) n, return the
# minimum number of coins needed to create
# the amount n. If it is not possible to create the
# amount using the given coin denomination, return None.
#8/16/20

def make_change(coins, n):
    # Fill this in.
    print(coins,n)
    change = []

    for i in range(len(coins)):
        value = coins[len(coins)-1-i]

        if value <= n:
            num_of_coins = int(n/value)
            n = n-(num_of_coins * value)


            i = 0
            while i < num_of_coins:
                change.append(value)
                i +=1

    return str(len(change)) + " coins "+ str(change)

print("Making Change 8-16")
print("<-----------------START--------------<")
print(make_change([1, 5, 10, 25], 36))
# 3 coins (25 + 10 + 1)
print("<-----------------END--------------<")

#Hi, here's your problem today.
# This problem was recently asked by LinkedIn:

#Given a list of numbers and an integer k,
# partition/sort the list such that the all
# numbers less than k occur before k, and all
# numbers greater than k occur after the number k.
#8/15/20

def partition_list(nums, k):
    # Fill this in.
    print(nums,k)
    output = []

    for n in nums:
        if n < k:
            output.insert(0,n)
        else:
            output.append(n)

    return output

print("Partition a List 8-15")
print("<-----------------START--------------<")
print(partition_list([2, 2, 2, 5, 2, 2, 2, 2, 5], 3))
# [2, 2, 2, 2, 2, 2, 2, 2, 5]
print("<-----------------END--------------<")


#Hi, here's your problem today.
# This problem was recently asked by Twitter:

#Given a linked list, swap the position of the
# 1st and 2nd node, then swap the position of the
# 3rd and 4th node etc.
#8/14/20

class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

    def __repr__(self):
        return f"{self.value}, ({self.next.__repr__()})"

def swap_every_two(llist):
    # Fill this in.
    print(llist)


print("Swap Every Two Nodes in a Linked List 8-14")
print("<-----------------START--------------<")
llist = Node(1, Node(2, Node(3, Node(4, Node(5)))))
print(swap_every_two(llist))
# 2, (1, (4, (3, (5, (None)))))
print("<-----------------END--------------<")


#Hi, here's your problem today.
# This problem was recently asked by Twitter:

#Given a binary tree and an integer k, filter
# the binary tree such that its leaves don't
# contain the value k. Here are the rules:

#- If a leaf node has a value of k, remove it.
#- If a parent node has a value of k, and
# all of its children are removed, remove it.
#8/13/20

class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

    def __repr__(self):
        return f"value: {self.value}, left: ({self.left.__repr__()}), right: ({self.right.__repr__()})"

def filter(tree, k):
    # Fill this in.
    print()
#     1
#    / \
#   1   1
#  /   /
# 2   1
n5 = Node(2)
n4 = Node(1)
n3 = Node(1, n4)
n2 = Node(1, n5)
n1 = Node(1, n2, n3)

print("Filter Binary Tree Leaves 8-13")
print("<-----------------START--------------<")
print(filter(n1, 1))
#     1
#    /
#   1
#  /
# 2
# value: 1, left: (value: 1, left: (value: 2, left: (None), right: (None)), right: (None)), right: (None)
print("<-----------------END--------------<")


#Hi, here's your problem today.
# This problem was recently asked by Apple:

#Create a class that initializes with a list
# of numbers and has one method called sum.
# sum should take in two parameters, start_idx and
# end_idx and return the sum of the list from
# start_idx (inclusive) to end_idx` (exclusive).

#You should optimize for the sum method.
#8/12/20

class ListFastSum:
    def __init__(self, nums):
        self.nums = nums

    def sum(self, start_idx, end_idx):
        # Fill this in.
        print()

print("Optimized List Sum 8-12")
print("<-----------------START--------------<")
print(ListFastSum([1, 2, 3, 4, 5, 6, 7]).sum(2, 5))
# 12 because 3 + 4 + 5 = 12
print("<-----------------END--------------<")

#Hi, here's your problem today.
# This problem was recently asked by Apple:

#Given a list of points, an interger k,
# and a point p, find the k closest points to p.
#8/11/20

class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __repr__(self):
        return f"({self.x}, {self.y})"

def closest_points(points, k, p):
    # Fill this in.
    print(points)

points = [
    Point(0, 0),
    Point(1, 1),
    Point(2, 2),
    Point(3, 3),
]

print("Nearest Points 8-11")
print("<-----------------START--------------<")
print(closest_points(points, 2, Point(0, 2)))
# [(0, 0), (1, 1)]
print("<-----------------END--------------<")


#Hi, here's your problem today.
# This problem was recently asked by Microsoft:

#Given a string, determine if there is a way
# to arrange the string such that the string
# is a palindrome. If such arrangement exists,
# return a palindrome (There could be many arrangements).
# Otherwise return None.
#8/10/20

def find_palindrome(s):
    # Fill this in.
    print(s)
    my_dict = {}

    for c in s:
        if c not in my_dict:
            my_dict[c] = 1
        else:
            my_dict[c]+=1

    odd = 0
    for x in my_dict:
        if (my_dict[x] % 2) == 1:
            odd += 1

    if odd > 1:
        status = False
    else:
        status = True

    str = ""
    mid = ""
    if status:
        print(my_dict)
        for x in my_dict:
            if my_dict[x] % 2 == 0:
                i = 0
                while i < my_dict[x] / 2:
                    str += x
                    i+=1
            else:
                mid = x


        rev_str = str[::-1]

        if mid != "":
            i = 0
            while i < my_dict[mid]:
                str+=mid
                i+=1

        str+= rev_str
    else:
        return None

    return str
print("Check for Palindrome 8-10")
print("<-----------------START--------------<")
print(find_palindrome('momom'))
# momom
print("<-----------------END-------------<")


#Hi, here's your problem today.
# This problem was recently asked by Microsoft:

#A maze is a matrix where each cell can either be a 0 or 1.
# A 0 represents that the cell is empty, and a 1 represents
# a wall that cannot be walked through. You can also only
# travel either right or down.

#Given a nxm matrix, find the number of ways
# someone can go from the top left corner to the
# bottom right corner. You can assume the two
# corners will always be 0.

#Example:
#Input: [[0, 1, 0], [0, 0, 1], [0, 0, 0]]
# 0 1 0
# 0 0 1
# 0 0 0
#Output: 2
#The two paths that can only be taken in the
# above example are: down -> right -> down -> right,
# and down -> down -> right -> right.
#8/9/20

def paths_through_maze(maze):
    # Fill this in.
    print(maze)




print("Maze Paths 8-9")
print("<-----------------START--------------<")
print(paths_through_maze([[0, 1, 0],
                          [0, 0, 1],
                          [0, 0, 0]]))
# 2
print("<-----------------END--------------<")

#Hi, here's your problem today.
# This problem was recently asked by Amazon:

#Given a string, return the first recurring
# letter that appears. If there are no recurring
# letters, return None.

#Example:
#Input: qwertty
#Output: t

#Input: qwerty
#Output: None
#8/8/20

def first_recurring_char(s):
    # Fill this in.
    print(s)
    my_dict = {}

    for c in s:
        if c in my_dict:
            return c
        my_dict[c] = 1

    return None

print("First recurring character 8-8")
print("<-----------------START--------------<")
print(first_recurring_char('qwertty'))
# t

print(first_recurring_char('qwerty'))
# None
print("<-----------------END--------------<")

#Hi, here's your problem today.
# This problem was recently asked by Amazon:

#Given a 32 bit integer, reverse the bits and return that number.

#Example:
#Input: 1234
# In bits this would be 0000 0000 0000 0000 0000 0100 1101 0010
#Output: 1260388352
# Reversed bits is 0100 1011 0010 0000 0000 0000 0000 0000
#8/7/20

def to_bits(n):
    return '{0:08b}'.format(n)

def reverse_num_bits(num):
    # Fill this in.
    print(num)
    bit_stream = to_bits(num)
    bit_stream = bit_stream[::-1]
    total = 0
    base = 1

    while len(bit_stream) < 32:
        bit_stream += "0"

    for i in range(len(bit_stream)):
        if int(bit_stream[len(bit_stream)-1-i]) == 1:
            total += base
        base *= 2

    return total

print("Reverse Bits 8-7")
print("<-----------------START--------------<")
print(to_bits(1234))
# 10011010010
print(reverse_num_bits(1234))
# 1260388352
print(to_bits(reverse_num_bits(1234)))
# 1001011001000000000000000000000
print("<-----------------END--------------<")

#Hi, here's your problem today.
# This problem was recently asked by Facebook:

#Given a list of words, for each word find the
# shortest unique prefix. You can assume a word
# will not be a substring of another word
# (ie play and playing won't be in the same words list)

#Example
#Input: ['joma', 'john', 'jack', 'techlead']
#Output: ['jom', 'joh', 'ja', 't']
#8/6/20

def shortest_unique_prefix(words):
    # Fill this in.
    print(words)
    prefix_dict = {}
    output = []


    for w in words:
        i = 0
        pre = ""

        while i < len(w):
            pre += w[i]

            if pre not in prefix_dict:
                prefix_dict[pre] = 1
                output.append(pre)
                break
            i+=1

    return output

print("Shortest unique prefix 8-6")
print("<-----------------START--------------<")
print(shortest_unique_prefix(['joma', 'john', 'jack', 'techlead']))
# ['jom', 'joh', 'ja', 't']
print("<-----------------END--------------<")

#Hi, here's your problem today.
# This problem was recently asked by Facebook:

#Given an expression (as a list) in reverse polish notation,
# evaluate the expression. Reverse polish notation is
# where the numbers come before the operand.
# Note that there can be the 4 operands '+', '-', '*', '/'.
# You can also assume the expression will be well formed.

#Example
#Input: [1, 2, 3, '+', 2, '*', '-']
#Output: -9
#The equivalent expression of the above reverse polish
# notation would be (1 - ((2 + 3) * 2)).
#8/5/20

def reverse_polish_notation(expr):
    # Fill this in.
    print(expr)
    num_stack = []
    op_stack = []

    for i in range(len(expr)):
        if str(expr[i]).isnumeric():
            num_stack.append(expr[i])
        else:
            op_stack.append(expr[i])

    total = num_stack.pop()

    for op in op_stack:
        if op == "+":
            total+=num_stack.pop()

        elif op == "-":
            total = num_stack.pop() - total

        elif op == "*":
            total*=num_stack.pop()

        elif op == "/":
            total = num_stack.pop()/total

        else:
            print(ERROR)
            break

    return total

print("Reverse Polish Notation Calculator 8-5")
print("<-----------------START--------------<")
# 1 - (2 + 3) * 2
print(reverse_polish_notation([1, 2, 3, '+', 2, '*', '-']))
# -9
print("<-----------------END--------------<")

#Hi, here's your problem today.
# This problem was recently asked by Google:

#Given a nested dictionary, flatten the dictionary,
# where nested dictionary keys can be represented
# through dot notation.

#Example:
#Input: {
#  'a': 1,
#  'b': {
#    'c': 2,
#    'd': {
#      'e': 3
#    }
#  }
#}
#Output: {
#  'a': 1,
#  'b.c': 2,
#  'b.d.e': 3
#}
#You can assume there will be no arrays,
# and all keys will be strings.
#8/4/20

def flatten_dictionary(d):
    # Fill this in.
    print(d)

d = {
    'a': 1,
    'b': {
        'c': 2,
        'd': {
            'e': 3
        }
    }
}
print("Flatten Dictionary 8-4")
print("<-----------------START--------------<")
print(flatten_dictionary(d))
# {'a': 1, 'b.c': 2, 'b.d.e': 3}
print("<-----------------END--------------<")

#Hi, here's your problem today.
# This problem was recently asked by Google:

#Given two strings, find if there is a one-to-one
# mapping of characters between the two strings.

#Example
#Input: abc, def
#Output: True # a -> d, b -> e, c -> f

#Input: aab, def
#Ouput: False # a can't map to d and e
#8/3/20

def has_character_map(str1, str2):
    # Fill this in.
    print(str1,str2)
    status = False
    str_dict = {}

    if len(str1) == len(str2):
        status = True

        for i in range(len(str1)):
            if str1[i] not in str_dict:
                    if str2[i] not in str_dict.values():
                        str_dict[str1[i]] = str2[i]
                    else:
                        status = False
                        break

            if str1[i] in str_dict:
                if str_dict[str1[i]] != str2[i]:
                    status = False
                    break

    print(str_dict)

    return status
print("Character Map 8-3")
print("<-----------------START--------------<")
print(has_character_map('abc', 'def'))
# True
print(has_character_map('aac', 'def'))
# False
print("<-----------------END--------------<")

#Hi, here's your problem today.
# This problem was recently asked by AirBNB:

#Given a linked list and a number k,
# rotate the linked list by k places.
#8/2/20

class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

    def __str__(self):
        current = self
        ret = ''
        while current:
            ret += str(current.value)
            current = current.next
        return ret

def rotate_list(list, k):
    # Fill this in.
    print("Original: "+str(list))
    i = 0

    while i < k:
        head = list
        while list.next != None:
            prev = list
            list = list.next

        prev.next = None
        list.next = head
        i+=1

    return list

# Order is 1, 2, 3, 4
llist = Node(1, Node(2, Node(3, Node(4))))

print("Rotate Linked List 8-2")
print("<-----------------START--------------<")
# Order should now be 3, 4, 1, 2
print("Rotated: "+str(rotate_list(llist, 2)))
# 3412
print("<-----------------END--------------<")
#Hi, here's your problem today.
# This problem was recently asked by Uber:

#Given a postorder traversal for a binary search tree,
# reconstruct the tree. A postorder traversal is a
# traversal order where the left child always comes
# before the right child, and the right child always comes
# before the parent for all nodes.
#8/1/20

class Node():
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

    def __repr__(self):
        return "(" + str(self.value) + ", " + self.left.__repr__() + ", " + self.right.__repr__() + ")"


def create_tree(postorder):
    # Fill this in.
    print()

print("Postorder Traversal 8-1")
print("<-----------------START--------------<")
# 2 is the root node, with 1 as the left child and 3 as the right child
print(create_tree([1, 3, 2]))
print("<-----------------END--------------<")

#Hi, here's your problem today.
# This problem was recently asked by LinkedIn:

#Given two rectangles, find the area of intersection.

#7/31/20

class Rectangle():
    def __init__(self, min_x=0, min_y=0, max_x=0, max_y=0):
        self.min_x = min_x
        self.min_y = min_y
        self.max_x = max_x
        self.max_y = max_y

def intersection_area(rect1, rect2):
    # Fill this in.
    print()

#  BBB
# AXXB
# AAA
rect1 = Rectangle(0, 0, 3, 2)
rect2 = Rectangle(1, 1, 3, 3)

print("Rectangle Intersection 7-31")
print("<-----------------START--------------<")
print(intersection_area(rect1, rect2))
# 2
print("<-----------------END--------------<")

#Hi, here's your problem today.
# This problem was recently asked by Twitter:

#Given a tree, find if the binary tree is
# height balanced or not. A height balanced
# binary tree is a tree where every node's 2 subtree
# do not differ in height by more than 1.
#7/30/20

class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

def is_height_balanced(tree):
    # Fill this in.
    print()

#     1
#    / \
#   2   3
#  /
# 4
n4 = Node(4)
n3 = Node(3)
n2 = Node(2, n4)
n1 = Node(1, n2, n3)

print("Determine Height Balanced Binary Tree 7-30")
print("<-----------------START--------------<")
print(is_height_balanced(n1))
# True

#     1
#    /
#   2
#  /
# 4
n1 = Node(1, n2)
print(is_height_balanced(n1))
# False
print("<-----------------END--------------<")

#Hi, here's your problem today.
# This problem was recently asked by Twitter:

#Given a list of numbers, find the smallest window
# to sort such that the whole list will be sorted.
# If the list is already sorted return (0, 0).
# You can assume there will be no duplicate numbers.

#Example:
#Input: [2, 4, 7, 5, 6, 8, 9]
#Output: (2, 4)
#Explanation: Sorting the window (2, 4)
# which is [7, 5, 6] will also means that the whole list is sorted.
#7/29/30

def min_window_to_sort(nums):
    # Fill this in.
    print(nums)

print("Sorting Window Range 7-29")
print("<-----------------START--------------<")
print(min_window_to_sort([2, 4, 7, 5, 6, 8, 9]))
# (2, 4)
print("<-----------------END--------------<")


#Hi, here's your problem today.
# This problem was recently asked by Apple:

#Given a binary tree, return the list of node
# values in zigzag order traversal. Here's an example

# Input:
#         1
#       /   \
#      2     3
#     / \   / \
#    4   5 6   7
#
# Output: [1, 3, 2, 4, 5, 6, 7]
#7/28/20

class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

def zigzag_order(tree):
    # Fill this in.
    output = []

    return output

n4 = Node(4)
n5 = Node(5)
n6 = Node(6)
n7 = Node(7)
n2 = Node(2, n4, n5)
n3 = Node(3, n6, n7)
n1 = Node(1, n2, n3)


print("ZigZag Binary Tree 7-28")
print("<-----------------START--------------<")
print(zigzag_order(n1))
# [1, 3, 2, 4, 5, 6, 7]
print("<-----------------END--------------<")


#Hi, here's your problem today.
# This problem was recently asked by Apple:

#A fixed point in a list is where the
# value is equal to its index. So for example the
# list [-5, 1, 3, 4], 1 is a fixed point in the
# list since the index and value is the same.
# Find a fixed point (there can be many, just return 1)
# in a sorted list of distinct elements, or return
# None if it doesn't exist.
#7/27/20

def find_fixed_point(nums):
    # Fill this in.
    print(nums)

    for i in range(len(nums)):
        if i == nums[i]:
            return i
    return None

print("Fixed Point 7-27")
print("<-----------------START--------------<")
print(find_fixed_point([-5, 1, 3, 4]))
# 1
print("<-----------------END--------------<")

#Hi, here's your problem today.
# This problem was recently asked by Microsoft:

#A UTF-8 character encoding is a variable width character
# encoding that can vary from 1 to 4 bytes depending on the character.
# The structure of the encoding is as follows:
#1 byte:  0xxxxxxx
#2 bytes: 110xxxxx 10xxxxxx
#3 bytes: 1110xxxx 10xxxxxx 10xxxxxx
#4 bytes: 11110xxx 10xxxxxx 10xxxxxx 10xxxxxx
#For more information, you can read up on the Wikipedia Page.

#Given a list of integers where each integer
# represents 1 byte, return whether or not the list
# of integers is a valid UTF-8 encoding.
#7/26/20

BYTE_MASKS = [
    None,
    0b10000000,
    0b11100000,
    0b11110000,
    0b11111000,
]
BYTE_EQUAL = [
    None,
    0b00000000,
    0b11000000,
    0b11100000,
    0b11110000,
]

def utf8_validator(bytes):
    # Fill this in.
    print(bytes)

print("UTF-8 Validator 7-26")
print("<-----------------START--------------<")
print(utf8_validator([0b00000000]))
# True
print(utf8_validator([0b00000000, 10000000]))
# False
print(utf8_validator([0b11000000, 10000000]))
# True
print("<-----------------END--------------<")

#Hi, here's your problem today.
# This problem was recently asked by Amazon:

#Given a number n, generate all binary search
# trees that can be constructed with nodes 1 to n.
#7/25/20

class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

    def __str__(self):
        result = str(self.value)
        if self.left:
            result = result + str(self.left)
        if self.right:
            result = result + str(self.right)
        return result

def generate_bst(n):
    # Fill this in.
    print()


print("Generate Binary Search Trees 7-25")
print("<-----------------START--------------<")

'''for tree in generate_bst(3):
    print(tree)'''
print("<-----------------END--------------<")
# Pre-order traversals of binary trees from 1 to n.
# 123
# 132
# 213
# 312
# 321

#   1      1      2      3      3
#    \      \    / \    /      /
#     2      3  1   3  1      2
#      \    /           \    /
#       3  2             2  1

#Hi, here's your problem today.
# This problem was recently asked by Amazon:

#Given a binary tree and a given node value,
# return all of the node's cousins. Two nodes are
# considered cousins if they are on the same
# level of the tree with different parents.
# You can assume that all nodes will have their own unique value.
#7/24/20

class Node(object):
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

class Solution(object):
    def list_cousins(self, tree, val):
        # Fill this in.
        print()
#     1
#    / \
#   2   3
#  / \   \
# 4   6   5
root = Node(1)
root.left = Node(2)
root.left.left = Node(4)
root.left.right = Node(6)
root.right = Node(3)
root.right.right = Node(5)

print("Number of Cousins 7-24")
print("<-----------------START--------------<")
print(Solution().list_cousins(root, 5))
# [4, 6]
print("<-----------------END--------------<")


#Hi, here's your problem today.
# This problem was recently asked by Facebook:

#Given a list of building in the form of
# (left, right, height), return what the
# skyline should look like. The skyline should
# be in the form of a list of (x-axis, height),
# where x-axis is the next point where there is a
# change in height starting from 0, and height
# is the new height starting from the x-axis.
#7/23/20

def generate_skyline(buildings):
    # Fill this in.
    print()

#            2 2 2
#            2 2 2
#        1 1 2 2 2 1 1
#        1 1 2 2 2 1 1
#        1 1 2 2 2 1 1
# pos: 1 2 3 4 5 6 7 8 9

print("City Skyline 7-23")
print("<-----------------START--------------<")
print(generate_skyline([(2, 8, 3), (4, 6, 5)]))
# [(2, 3), (4, 5), (7, 3), (9, 0)]
print("<-----------------END--------------<")


#Hi, here's your problem today.
# This problem was recently asked by Facebook:

#Kaprekar's Constant is the number 6174.
# This number is special because it has the
# property where for any 4-digit number that
# has 2 or more unique digits, if you repeatedly
# apply a certain function it always reaches the number 6174.

#This certain function is as follows:
#- Order the number in ascending form and descending form to create 2 numbers.
#- Pad the descending number with zeros until it is 4 digits in length.
#- Subtract the ascending number from the descending number.
#- Repeat.

#Given a number n, find the number of times the function needs
# to be applied to reach Kaprekar's constant. Here's some starter code:
#7/22/20

KAPREKAR_CONSTANT = 6174

def num_kaprekar_iterations(n):
    # Fill this in.
    print()

print("Kaprekar's Constant 7-22")
print("<-----------------START--------------<")
print(num_kaprekar_iterations(123))
# 3
# Explanation:
#  3210 - 123 = 3087
#  8730 - 0378 = 8352
#  8532 - 2358 = 6174 (3 iterations)
print("<-----------------END--------------<")

#Hi, here's your problem today.
# This problem was recently asked by Google:

#Given a sorted list, create a height
# balanced binary search tree, meaning
# the height differences of each node can only
# differ by at most 1.
#7/21/20

class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

    def __str__(self):
        answer = str(self.value)
        if self.left:
            answer += str(self.left)
        if self.right:
            answer += str(self.right)
        return answer

def create_height_balanced_bst(nums):
    # Fill this in.
    print(nums)

print("Making a Height Balanced Binary Search Tree 7-21")
print("<-----------------START--------------<")
tree = create_height_balanced_bst([1, 2, 3, 4, 5, 6, 7, 8])
# 53214768
#  (pre-order traversal)
#       5
#      / \
#     3    7
#    / \  / \
#   2   4 6  8
#  /
# 1
print("<-----------------END--------------<")

#Hi, here's your problem today.
# This problem was recently asked by Google:

#A chess board is an 8x8 grid. Given a knight
# at any position (x, y) and a number of moves
# k, we want to figure out after k random moves
# by a knight, the probability that the knight
# will still be on the chessboard. Once the knight
# leaves the board it cannot move again and will be
# considered off the board.
#7/20/20

def is_knight_on_board(x, y, k, cache={}):
    # Fill this in.
    print()

print("Staying on a Chess Board 7-20")
print("<-----------------START--------------<")
print(is_knight_on_board(0, 0, 1))
# 0.25
print("<-----------------END--------------<")


#Hi, here's your problem today.
# This problem was recently asked by AirBNB:

#We have a list of tasks to perform,
# with a cooldown period. We can do multiple
# of these at the same time, but we cannot run
# the same task simultaneously.

#Given a list of tasks, find how long it will take to
# complete the tasks in the order they are input.
#tasks = [1, 1, 2, 1]
#cooldown = 2
#output: 7 (order is 1 _ _ 1 2 _ 1)
#7/19/20


def findTime(arr, cooldown):
    # Fill this in.
    print(arr)
    task_dict = {}
    prev_task = arr[0]
    time = 1

    task_dict[arr[0]] = 1

    for i in range(1,len(arr)):
        if prev_task == arr[i]:
            time += cooldown +1
            task_dict[prev_task] += 1

        elif arr[i] in task_dict:
            time +=(1+int(cooldown/2))
            task_dict[arr[i]] += 1


        else:
            time += 1
            task_dict[arr[i]] = 1


        prev_task = arr[i]
    return time

print("Multitasking 7-19")
print("<-----------------START--------------<")
print(findTime([1, 1, 2, 1], 2))
# 7
print("<-----------------END--------------<")

#Hi, here's your problem today.
# This problem was recently asked by Uber:

#You are given a list of n numbers,
# where every number is at most k indexes
# away from its properly sorted index.
# Write a sorting algorithm (that will be given the number k)
# for this list that can solve this in O(n log k)

#Example:
#Input: [3, 2, 6, 5, 4], k=2
#Output: [2, 3, 4, 5, 6]
#As seen above, every number is at most 2
# indexes away from its proper sorted index.
#7/18/20

def sort_partially_sorted(nums, k):
    # Fill this in.
    print(nums)

    for i in range(len(nums)-1):
        cur = nums[i]
        inserted = False

        if i > 1:
            x = 2
            while x > 0:
               if(cur < nums[i-x]):
                   nums.pop(i)
                   nums.insert((i-x),cur)
                   inserted = True
                   break
               x-=1

        if not inserted:
            x = 1
            while x <=2:
                if(cur < nums[i+x]):
                    nums.pop(i)
                    nums.insert((i+x-1),cur)
                    inserted = True
                    break
                x+=1

        if not inserted:
            nums.pop(i)
            nums.insert(i+x,cur)



    return nums

print("Sort a Partially Sorted List 7-18")
print("<-----------------START--------------<")
print(sort_partially_sorted([3, 2, 6, 5, 4], 2))
# [2, 3, 4, 5, 6]
print("<-----------------END--------------<")


#Hi, here's your problem today.
# This problem was recently asked by LinkedIn:

#Given a binary tree, find the most frequent subtree sum.

#Example:

#   3
#  / \
# 1   -3

#The above tree has 3 subtrees. The root node with 3, and the 2 leaf nodes, which gives us a total of 3 subtree sums. The root node has a sum of 1 (3 + 1 + -3), the left leaf node has a sum of 1, and the right leaf node has a sum of -3. Therefore the most frequent subtree sum is 1.

#If there is a tie between the most frequent sum, you can return any one of them.
#7/17/20

class Node():
    def __init__(self, value, left=None, right=None):
        self.val = value
        self.left = left
        self.right = right

def most_freq_subtree_sum(root):
    # fill this in.
    return  ""
root = Node(3, Node(1), Node(-3))

print("Most Frequent Subtree Sum 7-17")
print("<-----------------START--------------<")
print(most_freq_subtree_sum(root))
# 1
print("<-----------------END--------------<")

#Hi, here's your problem today.
# This problem was recently asked by Twitter:

#Given a string with only ( and ), find the minimum number of characters to add or subtract to fix the string such that the brackets are balanced.

#Example:
#Input: '(()()'
#Output: 1
#Explanation:

#The fixed string could either be ()()
# by deleting the first bracket, or (()())
# by adding a bracket. These are not the only ways of
# fixing the string, there are many other ways by adding
# it in different positions!
#7/16/20

def fix_brackets(s):
    # Fill this in.
    print(s)
    stack = []
    removed = False

    for c in s:
        if c == "(":
            stack.append(c)
        elif c == ")":
            for i in range(len(stack)):
                if stack[-1] == "(":
                    stack.pop()
                    removed = True
                    break

            if not removed:
                stack.append(c)
            removed = False

    return(len(stack))


print("Fix Brackets 7-16")
print("<-----------------START--------------<")
print(fix_brackets('(()()'))

# 1
print("<-----------------START--------------<")


#Hi, here's your problem today.
# This problem was recently asked by Twitter:

#Given an integer, check if that integer is a palindrome.
# For this problem do not convert the integer to a
# string to check if it is a palindrome.
#7/15/20

import math

def is_palindrome(n):
    # Fill this in.
    print(n)
    num = []

    while n > 0:
        num.append(n%10)
        n = int(n/10)

    for i in range(len(num)):
        if num[i] != num[len(num)-1-i]:
            return False

    return True


print("Palindrome Integers 7-15")
print("<-----------------START--------------<")
print(is_palindrome(1234321))
# True
print(is_palindrome(1234322))
# False
print("<-----------------END--------------<")

#Hi, here's your problem today.
# This problem was recently asked by Apple:

#You are given a tree, and your job is to
# print it level-by-level with linebreaks.

#    a
#   / \
#  b   c
# / \ / \
#d  e f  g

#The output should be
#a
#bc
#defg
#7/14/20

from collections import deque

class Node(object):
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

    def __str__(self):
        # Fill this in.
        output = ""

        if self is None:
            return
        q = []

        q.append(self)

        while q:
            count = len(q)

            while count > 0:
                temp = q.pop(0)
                print(temp.val, end='')
                output += (temp.val)#, end=' ')
                if temp.left:
                    q.append(temp.left)
                if temp.right:
                    q.append(temp.right)

                count -= 1
            print(' ')

        return ""


tree = Node('a')
tree.left = Node('b')
tree.right = Node('c')
tree.left.left = Node('d')
tree.left.right = Node('e')
tree.right.left = Node('f')
tree.right.right = Node('g')

print("Print a tree level-by-level, with line-breaks 7-14")
print("<-----------------START--------------<")
print(tree)
# a
# bc
# defg
print("<-----------------END--------------<")


#Hi, here's your problem today.
# This problem was recently asked by Apple:

#In many spreadsheet applications,
# the columns are marked with letters.
# From the 1st to the 26th column the
# letters are A to Z. Then starting from
# the 27th column it uses AA, AB, ..., ZZ, AAA, etc.

#Given a number n, find the n-th column name.
#7/13/20

def column_name(n):
    # Fill this in.
    print(n)
    output_str = ""

    if n > 26:
        while n > 0:
            temp = (n % 26)
            #print(temp)
            n = int(n / 26)
            output_str += str(intToChar(temp))
    else:
        output_str = str(intToChar(n))

    return output_str[::-1]


def intToChar(c):
    if c == 1:
        return "A"
    if c == 2:
        return "B"
    if c == 3:
        return "C"
    if c == 4:
        return "D"
    if c == 5:
        return "E"
    if c == 6:
        return "F"
    if c == 7:
        return "G"
    if c == 8:
        return "H"
    if c == 9:
        return "I"
    if c == 10:
        return "J"
    if c == 11:
        return "K"
    if c == 12:
        return "L"
    if c == 13:
        return "M"
    if c == 14:
        return "N"
    if c == 15:
        return "O"
    if c == 16:
        return "P"
    if c == 17:
        return "Q"
    if c == 18:
        return "R"
    if c == 19:
        return "S"
    if c == 20:
        return "T"
    if c == 21:
        return "U"
    if c == 22:
        return "V"
    if c == 23:
        return "W"
    if c == 24:
        return "X"
    if c == 25:
        return "Y"
    if c == 26:
        return "Z"

    else:
        return None

print("Spreadsheet Columns 7-13")
print("<-----------------START--------------<")
print(column_name(26))
print(column_name(27))
print(column_name(28))
# Z
# AA
# AB
print("<-----------------END--------------<")

#Hi, here's your problem today.
# This problem was recently asked by Microsoft:

#An IP Address is in the format of A.B.C.D,
# where A, B, C, D are all integers between 0 to 255.

#Given a string of numbers, return the
# possible IP addresses you can make with that string by
# splitting into 4 parts of A, B, C, D.

#Keep in mind that integers can't start with a 0! (Except for 0)

#Example:
#Input: 1592551013
#Output: ['159.255.101.3', '159.255.10.13']
#4/12/20

def ip_addresses(s, ip_parts=[]):
    # Fill this in.
    print(s)
    sz = len(s)

    # Check for string size
    if sz > 12:
        return []
    snew = s

    # Generating different combinations.
    for i in range(1, sz - 2):
        for j in range(i + 1, sz - 1):
            for k in range(j + 1, sz):
                snew = snew[:k] + "." + snew[k:]
                snew = snew[:j] + "." + snew[j:]
                snew = snew[:i] + "." + snew[i:]

                if is_valid(snew):
                    ip_parts.append(snew)
                snew = s

    return ip_parts


def is_valid(ip):
    ip = ip.split(".")

    # Checking for the corner cases
    for i in ip:
        if len(i) > 3 or int(i) < 0 or int(i) > 255:
            return False
        if len(i) > 1 and int(i) == 0:
            return False
        if len(i) > 1 and int(i) != 0 and i[0] == '0':
            return False
    return True



print("Generate All IP Addresses 7-12")
print("<-----------------START--------------<")
print(ip_addresses('1592551013'))
# ['159.255.101.3', '159.255.10.13']
print("<-----------------END---------------<")

#Hi, here's your problem today.
# This problem was recently asked by Microsoft:

#Return the longest run of 1s for a given
# integer n's binary representation.

#Example:
#Input: 242
#Output: 4
#242 in binary is 0b11110010, so the longest run of 1 is 4.
#7/11/20


def longest_run(n):
    # Fill this in.
    print(n)
    print(bin(n)[2:])
    binary_num = bin(n)[2:]

    longest = 0
    count = 0

    for i in range(len(binary_num)):
        if int(binary_num[i]) == 1:
            count += 1
        else:
            if count > longest:
                longest = count
            count = 0

    return longest


print("Consecutive Ones 7-11")
print("<-----------------START---------------<")
print(longest_run(242))
# 4
print("<-----------------END---------------<")

#Hi, here's your problem today.
# This problem was recently asked by Amazon:

#MS Excel column titles have the following pattern:
# A, B, C, ..., Z, AA, AB, ..., AZ, BA, BB, ..., ZZ, AAA,
# AAB, ... etc. In other words, column 1 is named
# "A", column 2 is "B", column 26 is "Z", column 27 is "AA"
# and so forth. Given a positive integer, find its
# corresponding column name.
#Examples:
#Input: 26
#Output: Z

#Input: 51
#Output: AY

#Input: 52
#Output: AZ

#Input: 676
#Output: YZ

#Input: 702
#Output: ZZ

#Input: 704
#Output: AAB
#7/10/20

class Solution:
    def convertToTitle(self, n):
        # Fill this in.
        print(n)
        output_str = ""

        while n > 0:
            temp = (n % 26)
            n = int(n/26)
            output_str += str(Solution.intToChar(self,temp))


        return output_str[::-1]







    def intToChar(self,c):
        if c == 1:
            return "A"
        if c == 2:
            return "B"
        if c == 3:
            return "C"
        if c == 4:
            return "D"
        if c == 5:
            return "E"
        if c == 6:
            return "F"
        if c == 7:
            return "G"
        if c == 8:
            return "H"
        if c == 9:
            return "I"
        if c == 10:
            return "J"
        if c == 11:
            return "K"
        if c == 12:
            return "L"
        if c == 13:
            return "M"
        if c == 14:
            return "N"
        if c == 15:
            return "O"
        if c == 16:
            return "P"
        if c == 17:
            return "Q"
        if c == 18:
            return "R"
        if c == 19:
            return "S"
        if c == 20:
            return "T"
        if c == 21:
            return "U"
        if c == 22:
            return "V"
        if c == 23:
            return "W"
        if c == 24:
            return "X"
        if c == 25:
            return "Y"
        if c == 0:
            return "Z"

        else:
            return None

input1 = 1
input2 = 456976
input3 = 28
print("Spreadsheet Column Title 7-10")
print("<-----------------START---------------<")
print(Solution().convertToTitle(input1))
# A
print(Solution().convertToTitle(input2))
# YYYZ
print(Solution().convertToTitle(input3))
# AB
print("<-----------------END---------------<")


#Hi, here's your problem today.
# This problem was recently asked by Amazon:

#Version numbers are strings that are used to
# identify unique states of software products.
# A version number is in the format a.b.c.d.
# and so on where a, b, etc. are numeric strings
# separated by dots. These generally represent a
# hierarchy from major to minor changes.
# Given two version numbers version1 and version2,
# conclude which is the latest version number.
# Your code should do the following:
#If version1 > version2 return 1.
#If version1 < version2 return -1.
#Otherwise return 0.

#Note that the numeric strings such as a, b, c, d, etc.
# may have leading zeroes, and that the version strings do
# not start or end with dots. Unspecified level revision
# numbers default to 0.

#Example:
#Input:
#version1 = "1.0.33"
#version2 = "1.0.27"
#Output: 1
#version1 > version2

#Input:
#version1 = "0.1"
#version2 = "1.1"
#Output: -1
#version1 < version2

#Input:
#version1 = "1.01"
#version2 = "1.001"
#Output: 0
#ignore leading zeroes, 01 and 001 represent the same number.

#Input:
#version1 = "1.0"
#version2 = "1.0.0"
#Output: 0
#version1 does not have a 3rd level revision number, which
#defaults to "0"
#7/9/20

class Solution:
    def compareVersion(self, version1, version2):
        # Fill this in.
        print("Version1: "+ version1)
        print("Version2: "+ version2)

        solution = 0

        v1 = version1.split(".")
        v2 = version2.split(".")

        while int(v1[-1]) == 0:
            v1.pop()

        while int(v2[-1]) == 0:
            v2.pop()

        if len(v1) == len(v2):
            length = len(v1)

        elif len(v1) > len(v2):
            length = len(v2)
            solution = 1

        else:
            length = len(v1)
            solution = -1

        for i in range(length):
            temp = int(v1[i])-int(v2[i])

            if temp < 0:
                solution = -1
                break

            elif temp > 0:
                solution = 1
                break

        return solution



version1 = "1.0.1"
version2 = "1"

print("Compare Version Numbers 7-9")
print("<-----------------START---------------<")
print(Solution().compareVersion(version1, version2))
# 1
print("<-----------------END---------------<")



#Hi, here's your problem today.
# This problem was recently asked by Facebook:

#Given a directed graph, reverse the directed
# graph so all directed edges are reversed.

#Example:
#Input:
#A -> B, B -> C, A ->C

#Output:
#B->A, C -> B, C -> A
#7/8/20

from collections import defaultdict

class Node:
    def __init__(self, value):
        self.adjacent = []
        self.value = value

def reverse_graph(graph):
    # Fill this in.


    return graph

a = Node('a')
b = Node('b')
c = Node('c')

a.adjacent += [b, c]
b.adjacent += [c]

graph = {
    a.value: a,
    b.value: b,
    c.value: c,
}

print("Reverse a Directed Graph 7-8")
print("<-----------------START---------------<")
for _, val in reverse_graph(graph).items():
  print(val.adjacent)
# []
# ['a', 'b']
# ['a']
print("<-----------------END---------------<")

#Hi, here's your problem today.
# This problem was recently asked by Facebook:

#Given a file path with folder names, '..'
# (Parent directory), and '.' (Current directory),
# return the shortest possible file path (Eliminate all the '..' and '.').

#Example
#Input: '/Users/Joma/Documents/../Desktop/./../'
#Output: '/Users/Joma/'
#7/7/20

def shortest_path(file_path):
    # Fill this in.
    print(file_path)
    path = ""

    for i in range(len(file_path)-1):
        if file_path[i] == "." and file_path[i+1] == ".":
            path = go_back(path)
            break
        path+=file_path[i]

    return path

def go_back(path):
    count = 0

    for i in range(len(path)):
        if path[len(path)-1-i] == "/":
            count +=1

        if count == 2:
            break



    return path[:(len(path)-i)]


print("Absolute Path 7-7")
print("<-----------------START---------------<")
print(shortest_path('/Users/Joma/Documents/../Desktop/./../'))
# /Users/Joma/
print("<-----------------END---------------<")


#Hi, here's your problem today.
# This problem was recently asked by Google:

#Design a Tic-Tac-Toe game played between two
# players on an n x n grid. A move is guaranteed
# to be valid, and a valid move is one placed on
# an empty block in the grid. A player who succeeds
# in placing n of their marks in a horizontal, diagonal,
# or vertical row wins the game. Once a winning condition
# is reached, the game ends and no more moves are allowed.
# Below is an example game which ends in a winning condition:

#Given n = 3, assume that player 1 is "X" and player 2 is "O"
#board = TicTacToe(3);

#board.move(0, 0, 1); -> Returns 0 (no one wins)
#|X| | |
#| | | |    // Player 1 makes a move at (0, 0).
#| | | |

#board.move(0, 2, 2); -> Returns 0 (no one wins)
#|X| |O|
#| | | |    // Player 2 makes a move at (0, 2).
#| | | |

#board.move(2, 2, 1); -> Returns 0 (no one wins)
#|X| |O|
#| | | |    // Player 1 makes a move at (2, 2).
#| | |X|

#board.move(1, 1, 2); -> Returns 0 (no one wins)
#|X| |O|
#| |O| |    // Player 2 makes a move at (1, 1).
#| | |X|

#board.move(2, 0, 1); -> Returns 0 (no one wins)
#|X| |O|
#| |O| |    // Player 1 makes a move at (2, 0).
#|X| |X|

#board.move(1, 0, 2); -> Returns 0 (no one wins)
#|X| |O|
#|O|O| |    // Player 2 makes a move at (1, 0).
#|X| |X|

#board.move(2, 1, 1); -> Returns 1 (player 1 wins)
#|X| |O|
#|O|O| |    // Player 1 makes a move at (2, 1).
#|X|X|X|

#7/6/20

class TicTacToe(object):

    def __init__(self, n):
        # Fill this in.
        self.board = [["-" for x in range(n)] for y in range(n)]
        self.print_board()

    def move(self, row, col, player):
        # Fill this in.
        if player == 1:
            c = "X"
        else:
            c = "O"

        grid = self.board
        grid[row][col] = c
        self.print_board()

        if self.check_for_winner(row,col,c):
            return ("Player "+ str(player)+" is the winner: "+ c)

    def print_board(self):
        board = self.board
        for i in range(len(board)):
            print(board[i])
        print()

    def check_for_winner(self,r,c,p):
        winner = False
        count = 0

        for i in range(len(self.board)): # works for horizontal
            if self.board[r][i] == p:
                count+=1
            else:
                count = 0

            if count == len(self.board):
                winner = True
                break


        if not winner:
            count = 0
            for i in range(len(self.board)): # works for vertical
                if self.board[i][c] == p:
                    count+=1
                else:
                    count = 0

                if count == len(self.board):
                    winner = True
                    break


        if not winner:
            count = 0

            for i in range(len(self.board)): # works for diagonal right
                if self.board[i][i] == p:
                    count +=1
                else:
                    count = 0

                if count == len(self.board):
                    winner = True
                    break

        if not winner:
            count = 0

            for i in range(len(self.board)):  # works for diagonal left
                if self.board[i][len(self.board)-1-i] == p:
                    count += 1
                else:
                    count = 0

                if count == len(self.board):
                    winner = True
                    break

        return winner

print("Design Tic-Tac-Toe 7-6")
print("<-----------------START---------------<")
board = TicTacToe(3)
board.move(0, 0, 1)
board.move(0, 2, 2)
board.move(2, 2, 1)
board.move(1, 1, 2)
board.move(2, 0, 1)
board.move(1, 0, 2)
print(board.move(2, 1, 1))
print("<-----------------END---------------<")


#Hi, here's your problem today.
# This problem was recently asked by AirBNB:

#Given a non-empty list of words,
# return the k most frequent words.
# The output should be sorted from
# highest to lowest frequency, and
# if two words have the same frequency,
# the word with lower alphabetical order
# comes first. Input will contain only
# lower-case letters.

#Example:
#Input: ["daily", "interview", "pro", "pro",
#"for", "daily", "pro", "problems"], k = 2
#Output: ["pro", "daily"]
#7/5/20

class Solution(object):
    def topKFrequent(self, words, k):
        # Fill this in.
        print(words)
        temp_list = []
        output_list = []
        my_dict = {}

        for w in words:
            if w in my_dict:
                my_dict[w] += 1
            else:
                my_dict[w] = 1

        greatest = 0

        for x in my_dict:
            if my_dict[x] > greatest:
                greatest = my_dict[x]

        i=0

        while i < k:
            for x in my_dict:
                if my_dict[x] == greatest:
                    temp_list.append(x)
            greatest -= 1
            output_list += sorted(temp_list)
            temp_list.clear()
            i+=1

        return output_list

words = ["daily", "interview", "pro", "pro", "for", "daily", "pro", "problems"]
k = 2

print("Top K Frequent words 7-5")
print("<-----------------START---------------<")
print(Solution().topKFrequent(words, k))
# ['pro', 'daily']
print("<-----------------END---------------<")



#Hi, here's your problem today.
# This problem was recently asked by Uber:

#Given a linked list, determine if the linked list
# has a cycle in it. For notation purposes, we use
# an integer pos which represents the zero-indexed
# position where the tail connects to.

#Example:
#Input: head = [4,3,2,1,0], pos = 1.
#Output: true
#The example indicates a list where the tail
# connects to the second node.
#7/4/20

class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def hasCycle(self, head):
        # Fill this in.
        node_dict = {}

        while head:
            if head in node_dict:
                return True

            node_dict[head] = 0
            head = head.next

        return False


testHead = ListNode(4)
node1 = ListNode(3)
testHead.next = node1
node2 = ListNode(2)
node1.next = node2
node3 = ListNode(1)
node2.next = node3
testTail = ListNode(0)
node3.next = testTail
testTail.next = node1

print("Detect Linked List Cycle 7-4")
print("<-----------------START---------------<")
print(Solution().hasCycle(testHead))
# True
print("<-----------------END---------------<")

#Hi, here's your problem today.
# This problem was recently asked by LinkedIn:

#Given a non-empty array where each element
# represents a digit of a non-negative integer,
# add one to the integer. The most significant
# digit is at the front of the array and each
# element in the array contains only one digit.
# Furthermore, the integer does not have leading
# zeros, except in the case of the number '0'.

#Example:
#Input: [2,3,4]
#Output: [2,3,5]
#7/3/20

class Solution():
    def plusOne(self, digits):
        # Fill this in.
        print(digits)
        carry = 1
        total = []

        for i in range(len(digits)):
            temp = digits[len(digits)-1-i] + carry
            carry = int(temp/10)
            temp = temp%10
            total.insert(0,temp)

        return total

        ''' different solution is here
        nums = ""
        for n in digits:
            nums += str(n)

        output = []
        temp = int(nums) +1
        nums = str(temp)
        
        for c in nums:
            output.append(int(c))

        return output
        different solution ends here'''

num = [2, 9, 9]

print("Plus One 7-3")
print("<-----------------START---------------<")
print(Solution().plusOne(num))
# [3, 0, 0]
print("<-----------------END---------------<")



#Hi, here's your problem today.
# This problem was recently asked by Twitter:

#Given an array of integers of size n,
# where all elements are between 1 and n inclusive,
# find all of the elements of [1, n] that do not
# appear in the array. Some numbers may appear more than once.

#Example:
#Input: [4,5,2,6,8,2,1,5]
#Output: [3,7]
#For this problem, you can assume that you can mutate the input array.
#7/2/20

class Solution(object):
    def findDisappearedNumbers(self, nums):
        # Fill this in.
        print(nums)

        output = []
        my_dict = {}

        for i in range(1,(len(nums)+1)):
            my_dict[i] = 0

        for i in range(len(nums)):
            if nums[i] in my_dict:
                my_dict[nums[i]] += 1

        for x in my_dict:
            if my_dict[x] == 0:
                output.append(x)

        return output

nums = [4, 6, 2, 6, 7, 2, 1]
print("Find Missing Numbers in an Array 7-2")
print("<-----------------START---------------<")
print(Solution().findDisappearedNumbers(nums))
# [3, 5]
print("<-----------------END---------------<")

#Hi, here's your problem today.
# This problem was recently asked by Twitter:

#You are given the root of a binary tree.
# Find the level for the binary tree with
# the minimum sum, and return that value.

#For instance, in the example below,
# the sums of the trees are 10, 2 + 8 = 10,
# and 4 + 1 + 2 = 7. So, the answer here should be 7.
#7/1/20

class Node:
    def __init__(self, value, left=None, right=None):
        self.val = value
        self.left = left
        self.right = right

def minimum_level_sum(root):
    # Fill this in.
    print()

#     10
#    /  \
#   2    8
#  / \    \
# 4   1    2
node = Node(10)
node.left = Node(2)
node.right = Node(8)
node.left.left = Node(4)
node.left.right = Node(1)
node.right.right = Node(2)

print("Binary Tree Level with Minimum Sum 7-1")
print("<-----------------START---------------<")
print(minimum_level_sum(node))
print("<-----------------END---------------<")

#Hi, here's your problem today.
# This problem was recently asked by Apple:

#You are given the root of a binary tree, along
# with two nodes, A and B. Find and return the
# lowest common ancestor of A and B. For this problem,
# you can assume that each node also has a
# pointer to its parent, along with its left and right child.
#6/30/20

class TreeNode:
    def __init__(self, val):
        self.left = None
        self.right = None
        self.parent = None
        self.val = val


def lowestCommonAncestor(root, a, b):
    # Fill this in.

    if a.parent == b.parent:
        return a.parent


    return None
#   a
#  / \
# b   c
#    / \
#   d*  e*
root = TreeNode('a')
root.left = TreeNode('b')
root.left.parent = root
root.right = TreeNode('c')
root.right.parent = root
a = root.right.left = TreeNode('d')
root.right.left.parent = root.right
b = root.right.right = TreeNode('e')
root.right.right.parent = root.right
print("Lowest Common Ancestor of 2 Nodes in Binary Tree 6-30")
print("<-----------------START---------------<")
print(lowestCommonAncestor(root, a, b).val)
# c
print("<-----------------END---------------<")
#Hi, here's your problem today.
# This problem was recently asked by Apple:

#You are given two strings, A and B.
# Return whether A can be shifted some number of times to get B.

#Eg. A = abcde, B = cdeab should return true because
# A can be shifted 3 times to the right to get B.
# A = abc and B= acb should return false.
#6/29/20

def shift(str):
    first_letter = str[0]
    temp = str[1:] + first_letter
    return temp

def is_shifted(a, b):
    # Fill this in.
    print(a + " "+ b)
    status = False
    if len(a) == len(b):
        i = 0
        while a != b or i <= len(a):
            a = shift(a)
            i += 1
    if a == b:
        status = True
        print(a + " = " + b)
    return status

print("Shifted String 6-29")
print("<-----------------START---------------<")
print(is_shifted('abcde', 'cdeab'))
# True
print("<-----------------END---------------<")

#Hi, here's your problem today.
# This problem was recently asked by Microsoft:

#Given the root of a binary tree,
# print its level-order traversal.
# For example:

#  1
# / \
#2   3
#   / \
#  4   5

#The following tree should output 1, 2, 3, 4, 5.
#6/28/20

class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def print_level_order(root):
    # Fill this in.
    print()

root = Node(1, Node(2), Node(3, Node(4), Node(5)))
print("Level Order Traversal of Binary Tree 6-28")
print("<-----------------START---------------<")
print_level_order(root)
# 1 2 3 4 5
print("<-----------------END---------------<")

#Hi, here's your problem today.
# This problem was recently asked by Microsoft:

#You are given a doubly linked list.
# Determine if it is a palindrome.

#Can you do this for a singly linked list?
# 6/27/20

class Node(object):
    def __init__(self, val):
        self.val = val
        self.next = None
        self.prev = None

def is_palindrome(node):
    # Fill this in.
    print()

node = Node('a')
node.next = Node('b')
node.next.prev = node
node.next.next = Node('b')
node.next.next.prev = node.next
node.next.next.next = Node('a')
node.next.next.next.prev = node.next.next

print("Determine If Linked List is Palindrome 6-27")
print("<-----------------START---------------<")
print(is_palindrome(node))
# True
print("<-----------------END---------------<")

#Hi, here's your problem today.
# This problem was recently asked by Amazon:

#You are given an array of integers,
# and an integer K. Return the subarray
# which sums to K. You can assume that a
# solution will always exist.
#Can you do this in linear time?
#6/26/20

def find_continuous_k(list, k):
    # Fill this in.
    print(list,k)
    temp = set()
    output_list = []
    sum = 0

    for i in range(len(list)):
        sum += list[i]

        if sum == k or sum in temp:
            output_list.append(list[i])
        temp.add(sum)

    return output_list


print("Subarray with Target Sum 6-26")
print("<-----------------START---------------<")
print(find_continuous_k([1, 3, 2, 5, 7, 2], 14))
# [2, 5, 7]
print("<-----------------END---------------<")

#Hi, here's your problem today.
# This problem was recently asked by Amazon:

#You are given an array of integers.
# Return the length of the longest consecutive
# elements sequence in the array.

#For example, the input array [100, 4, 200, 1, 3, 2]
# has the longest consecutive sequence 1, 2, 3, 4,
# and thus, you should return its length, 4.
#Can you do this in linear time?
#6/25/20

def longest_consecutive(nums):
    # Fill this in.
    print(nums)

print("Longest Consecutive Sequence 6-25")
print("<-----------------START---------------<")
print(longest_consecutive([100, 4, 200, 1, 3, 2]))
# 4
print("<-----------------END---------------<")

#Hi, here's your problem today.
# This problem was recently asked by Facebook:
#6/24/20

#You are given an array of integers.
# Return all the permutations of this array.

def permute(nums):
    # Fill this in.
    print(nums)

print("Permutations of Numbers 6-24")
print("<-----------------START---------------<")
print(permute([1, 2, 3]))
# [[1, 2, 3], [2, 1, 3], [2, 3, 1], [1, 3, 2], [3, 1, 2], [3, 2, 1]]
print("<-----------------END---------------<")

#Hi, here's your problem today.
# This problem was recently asked by Facebook:

#You are given the root of a binary tree.
# Find the path between 2 nodes that maximizes
# the sum of all the nodes in the path, and
# return the sum. The path does not necessarily
# need to go through the root.
#6/23/20

class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def findMaxUtil(root):
	if root is None:
		return 0

	l = findMaxUtil(root.left)
	r = findMaxUtil(root.right)
	max_single = max(max(l, r) + root.val, root.val)
	max_top = max(max_single, l+r+ root.val)
	findMaxUtil.res = max(findMaxUtil.res, max_top)

	return max_single


def maxPathSum(root):
    findMaxUtil.res = float("-inf")

    findMaxUtil(root)
    return findMaxUtil.res

# (* denotes the max path)
#       *10
#       /  \
#     *2   *10
#     / \     \
#   *20  1    -25
#             /  \
#            3    4
root = Node(10)
root.left = Node(2)
root.right = Node(10)
root.left.left = Node(20)
root.left.right = Node(1)
root.right.right = Node(-25)
root.right.right.left = Node(3)
root.right.right.right = Node(4)
print("Maximum Path Sum in Binary 6-23")
print("<-----------------START---------------<")
print(maxPathSum(root))
# 42
print("<-----------------END---------------<")


#Hi, here's your problem today.
# This problem was recently asked by AirBNB:

#Given a sorted list of positive numbers,
# find the smallest positive number that cannot
# be a sum of any subset in the list.

#Example:
#Input: [1, 2, 3, 8, 9, 10]
#Output: 7
#Numbers 1 to 6 can all be summed by a subset
# of the list of numbers, but 7 cannot.
#6/22/20

def findSmallest(nums):
    # Fill this in.
    print(nums)
    smal_num = nums[0]+1

    for i in range(1,len(nums)):
        if nums[i] == smal_num or inSubSet(nums,i,smal_num):
            smal_num+=1
        else:
            break

    return smal_num



def inSubSet(nums,i,smal_num):
    status = False

    for x in range(i):
        for y in range(1,i):
            if smal_num == (nums[x] + nums[y]):
                status = True
                break
        if status:
            break

    return status

print("Smallest Number that is not a Sum of a Subset of List 6-22")
print("<-----------------START---------------<")
print(findSmallest([1, 2, 3, 8, 9, 10]))
# 7
print("<-----------------END---------------<")




#Hi, here's your problem today. This problem was recently asked by Uber:

#Given a number of integers, combine
# them so it would create the largest number.

#Example:
#Input:  [17, 7, 2, 45, 72]
#Output:  77245217
#6/21/20


def largestNum(nums):
    # Fill this in.
    print(nums)
    output = []
    greater = True
    appended = False

    for n in nums:
        if len(output) == 0:
            output.append(n)
            appended = True
        else:
            for i in range(len(output)):
                out = str(output[i])
                cur = str(n)

                for x in range(len(cur)):
                    if int(cur[x]) < int(out[0]):
                        if len(cur)> 1 and cur[0]>out[0]:
                            greater = True
                        else:
                            greater = False

                if greater:
                    output.insert(i,int(cur))
                    appended = True
                    break
                greater = True

        if not appended:
            output.append(int(cur))
            greater = True


    output_string = ""
    for n in output:
        output_string += str(n)
    return output_string



print("Make the Largest Number 6-21")
print("<-----------------START---------------<")
print(largestNum([17, 7, 2, 45, 72]))
# 77245217
print("<-----------------END---------------<")

#Hi, here's your problem today.
# This problem was recently asked by LinkedIn:

#Given a string, rearrange the string so that
# no character next to each other are the same.
# If no such arrangement is possible, then return None.

#Example:
#Input: abbccc
#Output: cbcbca
#6/20/20

def rearrangeString(s):
    # Fill this in.
    print(s)
    output = ""
    inserted = False
    status = False

    for c in s:
        if len(output) == 0:
            output += c

        else:
            if output[0] != c:
                temp = output
                output = ""
                output = c + temp
                inserted = True

            for i in range(len(output)-1):
                if output[i]!= c and output[i+1] != c and not inserted:
                    output = insertLetter(output,i,c)
                    inserted = True
                    break

            if not inserted:
                output += c

            else:
                inserted = False

    prev = ""
    for c in output:
        if prev == c:
            status = True
            break
        prev = c

    if status == True:
        return None

    return output


def insertLetter(s,i,l):
    x = 0
    str = ""
    while x <= i:
        str += s[x]
        x+=1

    str += l

    i +=1
    while i < len(s):
        str+= s[i]
        i+=1

    return str

print("No Adjacent Repeating Characters 6-20")
print("<-----------------START---------------<")
print(rearrangeString('abbccc'))
# cbcabc
print("<-----------------END---------------<")



#Hi, here's your problem today.
# This problem was recently asked by Twitter:

#Given an array of characters with repeats,
# compress it in place. The length after
# compression should be less than or equal to the
# original array.

#Example:
#Input: ['a', 'a', 'b', 'c', 'c', 'c']
#Output: ['a', '2', 'b', 'c', '3']
#6/19/20

class Solution(object):
    def compress(self, chars):
        # Fill this in.
        print("Original:     "+str(chars))
        count = 1
        compressed = []
        temp = ""

        for c in chars:
            if temp == "":
                temp = c
                compressed.append(temp)

            elif temp == c:
                count+=1

            else:
                if count !=1:
                    compressed.append(str(count))
                temp = c
                compressed.append(temp)
                count = 1

        if count != 1:
            compressed.append(str(count))


        Solution().deCompress(compressed)
        return compressed


    def deCompress(self, chars):
        de_comp = []
        count  = 1

        for c in chars:
            if c.isdigit():
                count = int(c)-1
            else:
                temp = c


            i = 0
            while i < count:
                de_comp.append(temp)
                i+=1

            count = 1

        return de_comp


print("String Compression 6-19")
print("<-----------------START---------------<")
comp = Solution().compress(['a', 'a', 'b', 'c', 'c', 'c'])
print("Compressed:   "+str(comp))
deComp = Solution().deCompress(comp)
print("DeCompressed: "+ str(deComp))

# ['a', '2', 'b', 'c', '3']
print("<-----------------END---------------<")




#Hi, here's your problem today.
# This problem was recently asked by Twitter:

#Given a Roman numeral, find the corresponding
# decimal value. Inputs will be between 1 and 3999.

#Example:
#Input: IX
#Output: 9

#Input: VII
#Output: 7

#Input: MCMIV
#Output: 1904
#Roman numerals are based on the following symbols:
#I     1
#IV    4
#V     5
#IX    9
#X     10
#XL    40
#L     50
#XC    90
#C     100
#CD    400
#D     500
#CM    900
#M     1000
#Numbers are strings of these symbols in descending order.
# In some cases, subtractive notation is used to avoid
# repeated characters. The rules are as follows:
#1.) I placed before V or X is one less, so 4 = IV
# (one less than 5), and 9 is IX (one less than 10)
#2.) X placed before L or C indicates ten less,
# so 40 is XL (10 less than 50) and 90 is XC (10 less than 100).
#3.) C placed before D or M indicates 100 less,
# so 400 is CD (100 less than 500), and 900 is CM (100 less than 1000).
#6/18/20

class Solution():
    def romanToInt(self, s):
        #Fill this in.
        print(s)

        total = 0

        for c in s:
            current_Num = Solution().getNum(c)
            if total == 0:
                total += current_Num
            else:
                if prev < current_Num:
                    total -= prev
                    total += (current_Num-prev)
                else:
                    total += current_Num

            prev = current_Num

        return total



    def getNum(self,s):
        num = 0
        if s == 'I':
            num = 1
        elif s == 'V':
            num = 5
        elif s == 'X':
            num = 10
        elif s == 'L':
            num = 50
        elif s == 'C':
            num = 100
        elif s == 'D':
            num = 500
        elif s == 'M':
            num = 1000

        return num


n = 'MCMX'
print("Convert Roman Numerals to Decimal 6-18")
print("<-----------------START---------------<")
print(Solution().romanToInt(n))
# 1910
print("<-----------------END---------------<")

#Hi, here's your problem today.
# This problem was recently asked by Apple:

#Given an array of integers, arr, where
# all numbers occur twice except one number
# which occurs once, find the number. Your
# solution should ideally be O(n) time and use
# constant extra space.

#Example:
#Input: arr = [7, 3, 5, 5, 4, 3, 4, 8, 8]
#Output: 7
#6/17/20

class Solution(object):
    def findSingle(self, nums):
        # Fill this in.
        output = nums[0]

        for i in range(1,len(nums)):
            output = output^nums[i]

        if output == 0:
            output = None
        return output

nums = [1, 1, 3, 4, 4, 5, 6, 5, 6]
print("Find the Single Element in an Array of Duplicates 6-17")
print("<-----------------START---------------<")
print(Solution().findSingle(nums))
# 3
print("<-----------------END---------------<")

#Hi, here's your problem today.
# This problem was recently asked by Apple:

#The Fibonacci sequence is the integer
# sequence defined by the recurrence relation:
# F(n) = F(n-1) + F(n-2), where F(0) = 0 and F(1) = 1.
# In other words, the nth Fibonacci number is the sum
# of the prior two Fibonacci numbers. Below are the
# first few values of the sequence:

#0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144...

#Given a number n, print the n-th Fibonacci Number.
#Examples:
#Input: n = 3
#Output: 2

#Input: n = 7
#Output: 13
#6/16/20


class Solution():
    def fibonacci(self, n):
        # fill this in.

        fib = [0,1,1]
        for i in range(n):
            fib.append(fib[-2] + fib[-1])

        return fib[n]
        #recursive solution
        """
        if n == 1 or n == 2:
            return 1
        else:
            return Solution().fibonacci(n-2) + Solution().fibonacci(n-1)
        """


n =9
print("Nth Fibonacci Number 6-16")
print("<-----------------START---------------<")
print(Solution().fibonacci(n))
# 34
print("<-----------------END---------------<")


#Hi, here's your problem today.
# This problem was recently asked by Microsoft:

#Given a list of numbers of size n, where
# n is greater than 3, find the maximum and
# minimum of the list using less than 2 * (n - 1) comparisons.
#6/15/20

def find_min_max(nums):
    # Fill this in.
    print(nums)
    max = nums[0]
    min = nums[0]

    for i in range(1,len(nums)):
        if nums[i] > max:
            max = nums[i]
        elif nums[i] < min:
            min = nums[i]

    return min,max

print("Max and Min with Limited Comparisons 6-15")
print("<-----------------START---------------<")
print(find_min_max([3, 5, 1, 2, 4, 8]))
# (1, 8)
print("<-----------------END---------------<")

#Hi, here's your problem today.
# This problem was recently asked by Microsoft:

#A k-ary tree is a tree with k-children,
# and a tree is symmetrical if the data of the
# left side of the tree is the same as the right
# side of the tree.

#Here's an example of a symmetrical k-ary tree.
#        4
#     /     \
#    3        3
#  / | \    / | \
#9   4  1  1  4  9
#Given a k-ary tree, figure out if the tree is symmetrical.
#6/14/20

class Node():
    def __init__(self, value, children=[]):
        self.value = value
        self.children = children

def is_symmetric(root):
    # Fill this in.
    status = True

    if len(root.children) == 0:
        return root.value

    else:
        left = root.children[0]
        right = root.children[1]

        if left.value == right.value and len(left.children) == len(right.children):
            length = len(left.children)

            for i in range(length):
                l = is_symmetric(left.children[i])
                r = is_symmetric(right.children[length-1-i])

                if l != r:
                    status = False
        else:
            status = False

    return status


tree = Node(4)
tree.children = [Node(3), Node(3)]
tree.children[0].children = [Node(9), Node(4), Node(1)]
tree.children[1].children = [Node(1), Node(4), Node(9)]
print("Symmetric k-ary Tree 6-14")
print("<-----------------START---------------<")
print(is_symmetric(tree))
# True
print("<-----------------END---------------<")


#Hi, here's your problem today.
# This problem was recently asked by Amazon:

#The h-index is a metric that attempts to
# measure the productivity and citation
# impact of the publication of a scholar.
# The definition of the h-index is if a scholar
# has at least h of their papers cited h times.

#Given a list of publications of the number
# of citations a scholar has, find their h-index.

#Example:
#Input: [3, 5, 0, 1, 3]
#Output: 3
#Explanation:
#There are 3 publications with 3 or more citations,
# hence the h-index is 3.
#6/13/20

def hIndex(publications):
    # Fill this in.
    print(publications)

print("H-Index 6-13")
print("<-----------------START---------------<")
print(hIndex([5, 3, 3, 1, 0]))
# 3
print("<-----------------END---------------<")

#Hi, here's your problem today.
# This problem was recently asked by Facebook:

#Starting at index 0, for an element n at index i,
# you are allowed to jump at most n indexes ahead.
# Given a list of numbers, find the minimum number
# of jumps to reach the end of the list.

#Example:
#Input: [3, 2, 5, 1, 1, 9, 3, 4]
#Output: 2
#Explanation:

#The minimum number of jumps to get to the end of the list is 2:
#3 -> 5 -> 4
#6/12/20

def jumpToEnd(nums):
    # Fill this in.
    print(nums)
    max = 0
    jump = 0
    i = 0

    while i in range(len(nums)):
        allowed_jumps = nums[i]

        if (allowed_jumps+i) < len(nums)-1:
            x = i+1
            allowed_jumps += x

            while x < allowed_jumps:
                if max < nums[x]:
                    max = nums[x]
                    i = x

                x+=1
            max = 0

        else:
            i = len(nums)

        jump += 1


    print("Jumps required:")
    return jump


print("Jump to the End 6-12")
print("<-----------------START---------------<")
print(jumpToEnd([3, 2, 5, 1, 1, 9, 3, 4]))
# 2
print("<-----------------END---------------<")

#Hi, here's your problem today.
# This problem was recently asked by Facebook:

#Two words can be 'chained' if the last character
# of the first word is the same as the first
# character of the second word.

#Given a list of words, determine if there is a
# way to 'chain' all the words in a circle.

#Example:
#Input: ['eggs', 'karat', 'apple', 'snack', 'tuna']
#Output: True
#Explanation:
#The words in the order of
# ['apple', 'eggs', 'snack', 'karat', 'tuna']
# creates a circle of chained words.
#6/11/20

from collections import defaultdict

def chainedWords(words):
    # Fill this in.
    print(words)
    appended = False
    status = False
    list = []

    for w in words:
        if len((list)) == 0:
            list.append(w)
            appended =True
        else:
            for i in range(len(list)):
                if list[-1][-1] == w[0]:
                    list.append(w)
                    appended = True
                    break
                else:
                    if list[i][-1] == w[0]:
                        list.insert(i+1,w)
                        appended = True
                        break
                    elif list[i][0] == w[-1]:
                        list.insert(i,w)
                        appended = True
                        break

        if not appended:
            list.append(w)
        else:
            appended = False

    print(list)


    if list[0][0] == list[-1][-1]:
        status = True
    return status


print("Circle of Chained Words 6-11")
print("<-----------------START---------------<")
print(chainedWords(['apple', 'eggs', 'snack', 'karat', 'tuna']))
# True
print(chainedWords(['eggs', 'karat', 'apple', 'snack', 'tuna']))
# true
print("<-----------------END---------------<")


#Hi, here's your problem today.
# This problem was recently asked by Google:

#Given a string with a certain rule:
# k[string] should be expanded to string k times.
# So for example, 3[abc] should be expanded to
# abcabcabc. Nested expansions can happen,
# so 2[a2[b]c] should be expanded to abbcabbc.

def decodeString(s):
    # Fill this in.
    print(s)
    solution = ""
    temp = ""
    k = []
    inner_str = ""

    for c in s:
        if c.isdigit():
            k.append(c)
        else:
            if c != "]":
                temp += c
            else:
                while temp[-1] != "[":
                    inner_str += temp[-1]
                    temp = temp[:-1]

                inner_str = reverse_string(inner_str)
                if len(k) > 0:
                    inner_str *= int(k[-1])
                    k.pop()

                solution = inner_str
                temp = temp[:-1]
                temp += inner_str
                inner_str = ""

    return solution

def reverse_string(s):
    solution = ""

    for i in range(len(s)):
        solution += s[len(s)-1-i]

    return solution


print("Decode String 6-10")
print("<-----------------START---------------<")
print(decodeString('2[a2[b]c]'))
# abbcabbc
print("<-----------------END---------------<")


#6/10/20
#Hi, here's your problem today.
# This problem was recently asked by Google:

#Given a binary tree, remove the nodes in which
# there is only 1 child, so that the binary
# tree is a full binary tree.

#So leaf nodes with no children should be kept,
# and nodes with 2 children should be kept as well.
#6/9/20
from collections import deque

class Node(object):
    def __init__(self, value, left=None, right=None):
        self.left = left
        self.right = right
        self.value = value
    def __str__(self):
        q = deque()
        q.append(self)
        result = ''
        while len(q):
            num = len(q)
            while num > 0:
                n = q.popleft()
                result += str(n.value)

                if n.left:
                    q.append(n.left)
                if n.right:
                    q.append(n.right)
                num = num - 1

            if len(q):
                result += "\n"

        return result

def fullBinaryTree(node):
    # Fill this in.
    root = node
    left = None
    right = None

    if node == None:
        return None

    elif node.left and node.right:  # node is valid if this is true
        left = fullBinaryTree(node.left)
        right = fullBinaryTree(node.right)

    elif node.left == None and node.right == None:# node is valid if this is true
        return node


    else:
        if node.left:
            return node.left
        else:
            return node.right

    root.left = left
    root.right = right
    return root
# Given this tree:
#     1
#    / \
#   2   3
#  /   / \
# 0   9   4

# We want a tree like:
#     1
#    / \
#   0   3
#      / \
#     9   4

tree = Node(1)
tree.left = Node(2)
tree.right = Node(3)
tree.right.right = Node(4)
tree.right.left = Node(9)
tree.left.left = Node(0)

print("Full Binary Tree 6-09")
print("<-----------------START---------------<")
print(tree)
print("-")
print(fullBinaryTree(tree))
# 1
# 03
# 94
print("<-----------------END---------------<")

#Hi, here's your problem today. This problem was recently asked by Uber:

#Design a simple stack that supports push, pop, top,
# and retrieving the minimum element in constant time.

#push(x) -- Push element x onto stack.
#pop() -- Removes the element on top of the stack.
#top() -- Get the top element.
#getMin() -- Retrieve the minimum element in the stack.

#Note: be sure that pop() and top() handle being called on an empty stack.
#6/8/20

class minStack(object):
    def __init__(self):
        # Fill this in.
        self.stack = []
        self.min = []

    def push(self, x):
        # Fill this in.
        self.stack.append(x)
        if len(self.min) == 0:
            self.min.append(x)
        elif x <= self.min[-1]:
            self.min.append(x)

    def pop(self):
        # Fill this in.
        temp = self.stack[-1]
        self.stack.pop()

        if temp == self.min[-1]:
            self.min.pop()

    def top(self):
        # Fill this in.
        return self.stack[-1]

    def getMin(self):
        # Fill this in.
        return self.min[-1]

print("Min Stack 6-08")
print("<-----------------START---------------<")
x = minStack()
x.push(-2)
x.push(0)
x.push(-3)
print(x.getMin())
# -3
x.pop()
print(x.top())
# 0
print(x.getMin())
# -2
print("<-----------------END---------------<")




#Hi, here's your problem today.
# This problem was recently asked by LinkedIn:

#Write a function that reverses the digits a
# 32-bit signed integer, x. Assume that the environment
# can only store integers within the 32-bit signed
# integer range, [-2^31, 2^31 - 1].
# The function returns 0 when the reversed integer overflows.

#Example:
#Input: 123
#Output: 321
#6/7/20

class Solution:
    def reverse(self, x):
        # Fill this in.
        #rev_num = str(x)[::-1] # can be used to reverse an int into a string

        rev_temp = ""

        while x > 0:
            rev_temp += str(x % 10)
            x /= 10
            x = int(x)

        #rev_temp += str(x)
        rev_num = int(rev_temp)

        bit = bin(rev_num)[2:]
        #bit = bin(int(rev_num))[2:]
        if len(bit) > 32:
            rev_num = 0

        return rev_num

print("Reverse Integer 6-07")
print("<-----------------START---------------<")
print(Solution().reverse(123))
# 321
print(Solution().reverse(2**31))
# 0
print("<-----------------END---------------<")


#Hi, here's your problem today.
# This problem was recently asked by Twitter:

#Given a list of integers, return the bounds of the
# minimum range that must be sorted so that the whole list would be sorted.

#Example:
#Input: [1, 7, 9, 5, 7, 8, 10]
#Output: (1, 5)
#Explanation:
#The numbers between index 1 and 5 are out of order and need to be sorted.
#6/6/20

def findRange(nums):
    # Fill this in.
    start = 0
    end = len(nums) -1

    print(nums)

print("Min Range Needed to Sort 6-06")
print("<-----------------START---------------<")
print(findRange([1, 7, 9, 5, 7, 8, 10]))
# (1, 5)
print("<-----------------END---------------<")


#Hi, here's your problem today.
# This problem was recently asked by Twitter:

#You are the manager of a number of employees
# who all sit in a row. The CEO would like to
# give bonuses to all of your employees, but
# since the company did not perform so well
# this year the CEO would like to keep the
# bonuses to a minimum.

#The rules of giving bonuses is that:
#- Each employee begins with a bonus factor of 1x.
#- For each employee, if they perform better than the
# person sitting next to them, the employee is given +1
# higher bonus (and up to +2 if they perform better
# than both people to their sides).

#Given a list of employee's performance,
# find the bonuses each employee should get.

#Example:
#Input: [1, 2, 3, 2, 3, 5, 1]
#Output: [1, 2, 3, 1, 2, 3, 1]
#6/05/20

def getBonuses(performance):
    # Fill this in.
    bonus = []
    bonus_total = 1
    prev = performance[0]

    for i in range(len(performance)-1):
        next = performance[i+1]

        if performance[i] > prev:
            bonus_total+=1
        if performance[i] > next:
            bonus_total+=1

        bonus.append(bonus_total)
        prev = performance[i]
        bonus_total = 1

    if performance[-1] > prev:
        bonus_total+=1

    bonus.append(bonus_total)

    return bonus
print("Distribute Bonuses 6-05")
print("<-----------------START---------------<")
print(getBonuses([1, 2, 3, 2, 3, 5, 1]))
# [1, 2, 3, 1, 2, 3, 1]
print("<-----------------END---------------<")


#Hi, here's your problem today.
# This problem was recently asked by Apple:

#You are given the root of a binary tree.
# You need to implement 2 functions:

#1. serialize(root) which serializes the tree
# into a string representation
#2. deserialize(s) which deserializes the
# string back to the original tree that it represents

#For this problem, often you will be asked to design
# your own serialization format. However, for simplicity,
# let's use the pre-order traversal of the tree.
#6/04/20

class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __str__(self):
        # pre-order printing of the tree.
        result = ''
        result += str(self.val)
        if self.left:
            result += str(self.left)
        if self.right:
            result += str(self.right)
        return result

def serialize(root):
    # Fill this in.
    print()
def deserialize(data):
    # Fill this in.
    print()

#     1
#    / \
#   3   4
#  / \   \
# 2   5   7
tree = Node(1)
tree.left = Node(3)
tree.left.left = Node(2)
tree.left.right = Node(5)
tree.right = Node(4)
tree.right.right = Node(7)

print("Tree Serialization 6-04")
print("<-----------------START---------------<")
print(serialize(tree))
# 1 3 2 # # 5 # # 4 # 7 # #
print(deserialize('1 3 2 # # 5 # # 4 # 7 # #'))
# 132547
print("<-----------------END---------------<")

#Hi, here's your problem today.
# This problem was recently asked by Apple:

#You are given a binary tree representation
# of an arithmetic expression. In this tree,
# each leaf is an integer value,, and
# a non-leaf node is one of the
# four operations: '+', '-', '*', or '/'.

#Write a function that takes this tree and evaluates the expression.

#Example:

#    *
#   / \
#  +    +
# / \  / \
#3  2  4  5

#This is a representation of the expression (3 + 2) * (4 + 5),
# and should return 45.
#6/03/20


class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

PLUS = "+"
MINUS = "-"
TIMES = "*"
DIVIDE = "/"

def evaluate(root):
    # Fill this in.
    if root.val == None:
        return 0

    if root.val == DIVIDE:
        return evaluate(root.left) / evaluate(root.right)
    if root.val == TIMES:
        return evaluate(root.left) * evaluate(root.right)
    if root.val == PLUS:
        return evaluate(root.left) + evaluate(root.right)
    if root.val == MINUS:
        return evaluate(root.left) - evaluate(root.right)
    else:
        return root.val

tree = Node(TIMES)
tree.left = Node(PLUS)
tree.left.left = Node(3)
tree.left.right = Node(2)
tree.right = Node(PLUS)
tree.right.left = Node(4)
tree.right.right = Node(5)

print("Arithmetic Binary Tree 6-03")
print("<-----------------START---------------<")
print(evaluate(tree))
# 45
print("<-----------------END---------------<")
#Given a time in the format of hour and minute,
# calculate the angle of the hour and minute hand on a clock.
#6/02/20

def calcAngle(h, m):
    # Fill this in.

    h_angle = .5 * (60 * h + m)
    m_angle = 6 * m
    total_angle = abs(h_angle-m_angle)
    total_angle = min(360 - total_angle, total_angle)

    return(int(total_angle))

print("Angles of a Clock 6-02")
print("<-----------------START---------------<")
print(calcAngle(3, 30))
# 75
print(calcAngle(12, 30))
# 165
print("<-----------------END---------------<")

#Hi, here's your problem today.
# This problem was recently asked by Microsoft:

#You are given an array of integers.
# Return the length of the longest increasing
# subsequence (not necessarily contiguous) in the array.

#Example:
#[0, 8, 4, 12, 2, 10, 6, 14, 1, 9, 5, 13, 3, 11, 7, 15]

#The following input should return 6 since the longest
# increasing subsequence is 0, 2, 6, 9 , 11, 15.
#6/01/20

def longest_increasing_subsequence(nums):
    print(nums)

print("Longest Increasing Subsequence 6-01")
print("<-----------------START---------------<")
print(longest_increasing_subsequence([0, 8, 4, 12, 2, 10, 6, 14, 1, 9, 5, 13, 3, 11, 7, 15]))
print("<-----------------END---------------<")


#Hi, here's your problem today.
# This problem was recently asked by Amazon:

#Given two arrays, write a function to compute
# their intersection - the intersection means
# the numbers that are in both arrays.

#Example 1:
#Input: nums1 = [1,2,2,1], nums2 = [2,2]
#Output: [2]
#Example 2:
#Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
#Output: [9,4]
#Note:
#Each element in the result must be unique.
#The result can be in any order.
#5/31/20

class Solution:
    def intersection(self, nums1, nums2):
        # Fill this in.
        print(nums1,nums2)
        my_dict = {}
        output = []

        for n in nums1:
            my_dict[n] = 1

        for n in nums2:
            if n in my_dict:
                output.append(n)
                my_dict.pop(n)

        return output

print("Array Intersection 5-31")
print("<-----------------START---------------<")
print(Solution().intersection([4, 9, 5], [9, 4, 9, 8, 4]))
# [9, 4]
print("<-----------------END---------------<")


#Hi, here's your problem today.
# This problem was recently asked by Amazon:

#You are given an array of integers.
# Return an array of the same size where
# the element at each index is the product
# of all the elements in the original array
# except for the element at that index.

#For example, an input of [1, 2, 3, 4, 5]
# should return [120, 60, 40, 30, 24].

#You cannot use division in this problem.
#5/30/20

def products(nums):
    # Fill this in.
    print(nums)
    product = 1
    product_array = []

    for i in range(len(nums)):
        for n in range(len(nums)):
            if i != n:
                product *= nums[n]

        product_array.append(product)
        product = 1
    return product_array

print("Product of Array Except Self 5-30")
print("<-----------------START---------------<")
print(products([1, 2, 3, 4, 5]))
# [120, 60, 40, 30, 24]
print("<-----------------END---------------<")
#Daily Interview Pro
#Hi, here's your problem today. This problem
# was recently asked by Facebook:

#Given a sorted list of numbers,
# return a list of strings that represent
# all of the consecutive numbers.

#Example:
#Input: [0, 1, 2, 5, 7, 8, 9, 9, 10, 11, 15]
#Output: ['0->2', '5->5', '7->11', '15->15']
#Assume that all numbers will be greater
# than or equal to 0, and each element can repeat.
#5/29/20

def findRanges(nums):
    #Fill this in.
    print(nums)
    output = []
    prev = str(nums[0])
    range = ""

    for n in nums:
        n = str(n)

        if len(range) == 0:
            range += prev
            range += "->"

        if (int(prev) + 1) == int(n) or prev == n:
            prev = n

        else:
            range += prev
            prev = n
            output.append(range)
            range = ""

    if len(range) == 0:
        range += n
        range += "->"
    range += n

    output.append(range)
    return output


print("Merge List of Number Into Ranges 5-29")
print("<-----------------START---------------<")
print(findRanges([0, 1, 2, 5, 7, 8, 9, 9, 10, 11, 15]))
# ['0->2', '5->5', '7->11', '15->15']
print("<-----------------END---------------<")


#Given a string, you need to reverse the
# order of characters in each word within
# a sentence while still preserving whitespace
# and initial word order.

#Example 1:
#Input: "The cat in the hat"
#Output: "ehT tac ni eht tah"
#Note: In the string, each word is separated by single
# space and there will not be any extra space in the string.
#5/28/20

class Solution:
    def reverseWords(self, str):
        # Fill this in.
        rw = ""
        r_str = ""
        print(str)

        for s in str:
            if s == " ":
                rw = Solution().rev(rw)
                r_str += rw
                r_str += s
                rw = ""
            else:
                rw += s

        rw = Solution().rev(rw)
        r_str += rw
        return r_str

    def rev(self,str):
        r = ""
        for i in range(len(str)):
            r += str[len(str)-1-i]
        return r

print("Reverse Words in a String 5-28")
print("<-----------------START---------------<")
print(Solution().reverseWords("The cat in the hat"))
# ehT tac ni eht tah
print("<-----------------END---------------<")
#You are given an array of tuples (start, end)
# representing time intervals for lectures.
# The intervals may be overlapping. Return
# the number of rooms that are required.

#For example. [(30, 75), (0, 50), (60, 150)] should return 2.
#5/27/20
def room_scheduling(arr):
    rooms = []
    temp = []
    inserted = False


    for i in range(len(arr)): #sorting list of tuples on start times
        if i ==0:
            rooms.append(arr[i])
        else:
            for x in range(len(rooms)):
                if rooms[x][0] >= arr[i][0]:
                    rooms.insert(x,arr[i])
                    inserted = True
                    break
            if not inserted:
                rooms.append(arr[i])
            inserted = False
    #rooms is sorted by start times

    i = 0
    while i in range(len(rooms)):
        start = rooms[i][0]
        end = rooms[i][1]
        for t in rooms:
            if end < t[0]:
                end = t[1]
                rooms.remove((t))


        temp.append((start,end))
        i+=1

    rooms = temp
    print(rooms)

    return len(temp)

print("Room Scheduling 5-27")
print("<-----------------START---------------<")
print(room_scheduling([(30, 75), (0, 50), (60, 150)]))
print("<-----------------END---------------<")

#You are given a stream of numbers.
# Compute the median for each new element .

#Eg. Given [2, 1, 4, 7, 2, 0, 5], the
# algorithm should output [2, 1.5, 2, 3.0, 2, 2, 2]
#5/26/20

def running_median(stream):
    # Fill this in.
    list = []
    print(stream)
    for i in range(len(stream)):
        list.append(stream[i])
        list.sort()
        len_of_list = len(list)
        pos = int(len_of_list/2)

        if len(list) % 2 != 0:
            med = list[pos]
        else:
            med = (list[pos-1] + list[pos])/2

        print(med)
print("Running Median 5-26")
print("<-----------------START---------------<")
running_median([2, 1, 4, 7, 2, 0, 5])
# 2 1.5 2 3.0 2 2.0 2
print("<-----------------END---------------<")
#Given a list of words, group the words that are
# anagrams of each other. (An anagram are words
# made up of the same letters).

#Example:

#Input: ['abc', 'bcd', 'cba', 'cbd', 'efg']
#Output: [['abc', 'cba'], ['bcd', 'cbd'], ['efg']]
#5/25/20

import collections

def groupAnagramWords(strs):
    # Fill this in.
    output = []
    temp = []
    status = True

    print(strs)
    for w in strs:
        temp.append(w)
        for s in strs: # if anagram appen to temp then remove anagram from strs
            if len(temp[0]) == len(s):
                for i in range(len(s)):
                    if temp[0][i] not in s:
                        status = False
                if status and temp[0] != s:
                    temp.append(s)
                    strs.remove(s)
                status = True

        output.insert(0,temp.copy())
        temp.clear()

    return output


print("Group Words that are Anagrams 5-25")
print("<-----------------START---------------<")
print(groupAnagramWords(['abc', 'bcd', 'cba', 'cbd', 'efg']))
# [['efg'], ['bcd', 'cbd'], ['abc', 'cba']]
print("<-----------------END---------------<")

#You are given a string of parenthesis.
# Return the minimum number of parenthesis
# that would need to be removed in order to
# make the string valid. "Valid" means that
# each open parenthesis has a matching closed parenthesis.

#Example:

#"()())()"

#The following input should return 1.

#")("
#5/24/20

def count_invalid_parenthesis(string):
    # Fill this in.
    list = []

    for c in string:
        if c == '(':
            list.append(c)
        elif c == ')' and len(list) >0:
            if list[-1] == '(':
                list.pop()
        else:
            list.append(c)

    return len(list)

print("Minimum Removals for Valid Parenthesis 5-24")
print("<-----------------START---------------<")
print(count_invalid_parenthesis("()())()"))
# 1
print("<-----------------END---------------<")


#Given a 2-dimensional grid consisting of 1's (land blocks)
# and 0's (water blocks), count the number of islands
# present in the grid. The definition of an island is as follows:
#1.) Must be surrounded by water blocks.
#2.) Consists of land blocks (1's) connected to adjacent land blocks (either vertically or horizontally).
#Assume all edges outside of the grid are water.
#Example:
#Input:
#10001
#11000
#10110
#00000

#Output: 3
#5/23/20

class Solution(object):
    def inRange(self, grid, r, c):
        numRow, numCol = len(grid), len(grid[0])

        if r < 0 or c < 0 or r >= numRow or c >= numCol:
            return False
        return True

    def numIslands(self, grid):
        # Fill this in.
        island_count = 0

        return island_count
grid = [[1, 1, 0, 0, 0],
        [0, 1, 0, 0, 1],
        [1, 0, 0, 1, 1],
        [0, 0, 0, 0, 0]]

print("Find the Number of Islands 5-23")
print("<-----------------START---------------<")
print(Solution().numIslands(grid))
# 3
print("<-----------------END---------------<")

#You are given the root of a binary tree. Find and return
# the largest subtree of that tree, which is a valid binary search tree.
#5/22/20
class TreeNode:
  def __init__(self, key):
    self.left = None
    self.right = None
    self.key = key

  def __str__(self):
    # preorder traversal
    answer = str(self.key)
    if self.left:
      answer += str(self.left)
    if self.right:
      answer += str(self.right)
    return answer

def largest_bst_subtree(root):
    # Fill this in.
    print()

#     5
#    / \
#   6   7
#  /   / \
# 2   4   9
node = TreeNode(5)
node.left = TreeNode(6)
node.right = TreeNode(7)
node.left.left = TreeNode(2)
node.right.left = TreeNode(4)
node.right.right = TreeNode(9)
print("Largest BST in a Binary Tree 5-22")
print("<-----------------START---------------<")
print(largest_bst_subtree(node))
#749
print("<-----------------END---------------<")
#Given an array, nums, of n integers, find all unique triplets
# (three numbers, a, b, & c) in nums such that a + b + c = 0.
# Note that there may not be any triplets that sum to zero
# in nums, and that the triplets must not be duplicates.
#Example:
#Input: nums = [0, -1, 2, -3, 1]
#Output: [0, -1, 1], [2, -3, 1]
#5/21/20

class Solution(object):
    def threeSum(self, nums):
        # Fill this in.
        print()

# Test Program
nums = [1, -2, 1, 0, 5]
print("3 Sum 5-21")
print("<-----------------START---------------<")
print(Solution().threeSum(nums))
# [[-2, 1, 1]]
print("<-----------------END---------------<")


#Given a list of words, and an arbitrary alphabetical order,
# verify that the words are in order of the alphabetical order.

#Example:
#Input:
#words = ["abcd", "efgh"], order="zyxwvutsrqponmlkjihgfedcba"

#Output: False
#Explanation: 'e' comes before 'a' so 'efgh' should come before 'abcd'

#Example 2:
#Input:
#words = ["zyx", "zyxw", "zyxwy"],
#order="zyxwvutsrqponmlkjihgfedcba"

#Output: True
#Explanation: The words are in increasing alphabetical order
#5/20/20

def isSorted(words, order):
    # Fill this in.
    status = True
    count_one = 0
    count_two = 0

    for i in range(len(words)-1):
        if len(words[i]) > len(words[i+1]):
            status = False
            break
        else:
            for x in range(len(words[i])):
                for c in range(len(order)):
                    if words[i][x] != order[c]:
                        count_one += 1
                    else:
                        temp = c
                        break

                for temp in range(len(order)):
                    if words[i+1][x] != order[c]:
                        count_two += 1
                    else:
                        break

                if count_one > count_two and words[i+1][x] in order:
                    status = False
                    break
                else:
                    count_one = 0
                    count_two = 0


    return status

print("Word Ordering in a Different Alphabetical Order 5-20")
print("<-----------------START---------------<")
print(isSorted(["abcd", "efgh"], "zyxwvutsrqponmlkjihgfedcba"))
# False
print(isSorted(["zyx", "zyxw", "zyxwy"],
               "zyxwvutsrqponmlkjihgfedcba"))
# True
print("<-----------------END---------------<")

#Given an array with n objects colored red,
# white or blue, sort them in-place so that
# objects of the same color are adjacent,
# with the colors in the order red, white and blue.

#Here, we will use the integers 0, 1,
# and 2 to represent the color red, white,
# and blue respectively.

#Note: You are not suppose to use the
# library’s sort function for this problem.

#Can you do this in a single pass?

#Example:
#Input: [2,0,2,1,1,0]
#Output: [0,0,1,1,2,2]

#5/19/20

class Solution:
  def sortColors(self, nums):
      # Fill this in.
      ''' red = []
      white = []
      blue = []

      for n in nums:
          if n == 0:
              red.append(0)
          elif n == 1:
              white.append(1)
          elif n == 2:
              blue.append(2)
          else:
              print(str(n) + " is not red, white, or blue.")

      nums.clear()

      for i in range(len(red)):
          nums.append(red[i])
      for i in range(len(white)):
          nums.append(white[i])
      for i in range(len(blue)):
          nums.append(blue[i])
      '''
      lo = 0
      hi = len(nums) - 1
      mid = 0
      while mid <= hi:
          if nums[mid] == 0:
              nums[lo], nums[mid] = nums[mid], nums[lo]
              lo += 1
              mid += 1
          elif nums[mid] == 1:
              mid = mid + 1
          else:
              nums[mid], nums[hi] = nums[hi], nums[mid]
              hi -= 1


print("Sort Colors 5-19")
print("<-----------------START---------------<")
nums = [0, 1, 2, 2, 1, 1, 2, 2, 0, 0, 0, 0, 2, 1]
print("Before Sort: ")
print(nums)
# [0, 1, 2, 2, 1, 1, 2, 2, 0, 0, 0, 0, 2, 1]

Solution().sortColors(nums)
print("After Sort: ")
print(nums)
# [0, 0, 0, 0, 0, 1, 1, 1, 1, 2, 2, 2, 2, 2]
print("<-----------------END---------------<")

#You are given the preorder and inorder traversals of a binary tree in the form of arrays. Write a function that reconstructs the tree represented by these traversals.

#Example:
#Preorder: [a, b, d, e, c, f, g]
#Inorder: [d, b, e, a, f, c, g]

#The tree that should be constructed from these traversals is:
#    a
#   / \
#  b   c
# / \ / \
#d  e f  g
#5/18/20

from collections import deque

class Node(object):
  def __init__(self, val):
    self.val = val
    self.left = None
    self.right = None

  def __str__(self):
    q = deque()
    q.append(self)
    result = ''
    while len(q):
      n = q.popleft()
      result += n.val
      if n.left:
        q.append(n.left)
      if n.right:
        q.append(n.right)

    return result


def reconstruct(preorder, inorder):
    # Fill this in.
    print()

tree = reconstruct(['a', 'b', 'd', 'e', 'c', 'f', 'g'],
                   ['d', 'b', 'e', 'a', 'f', 'c', 'g'])

print("Reconstrunct Binary Tree from Preorder and Inorder Traversals 5-18")
print("<-----------------START---------------<")
print(tree)
# abcdefg
print("<-----------------END---------------<")


#A unival tree is a tree where all the nodes
# have the same value. Given a binary tree,
# return the number of unival subtrees in the tree.

#For example, the following tree should return 5:
#5/17/20

class Node(object):
  def __init__(self, val):
    self.val = val
    self.left = None
    self.right = None

def count_unival_subtrees(root):
    # Fill this in.
    print()

a = Node(0)
a.left = Node(1)
a.right = Node(0)
a.right.left = Node(1)
a.right.right = Node(0)
a.right.left.left = Node(1)
a.right.left.right = Node(1)

print("Count Number of Unival Subtrees 5-17")
print("<-----------------START---------------<")
print(count_unival_subtrees(a))
# 5
print("<-----------------END---------------<")

#You are given a string s, and an integer k.
# Return the length of the longest substring in s
# that contains at most k distinct characters.

#For instance, given the string:
#aabcdefff and k = 3, then the longest
# substring with 3 distinct characters would
# be defff. The answer should be 5.
#5/16/20

def longest_substring_with_k_distinct_characters(s, k):
    # Fill this in.
    my_list = []
    output_list = []
    count = 0
    longest = 0
    temp = 0

    for c in s:
        if count < k or c in my_list:
            if c not in my_list:
                count += 1

            my_list.append(c)
            temp += 1

        else:
            if temp > longest:
                longest = temp
                temp = 0
                count = 1
                output_list = my_list.copy()
                my_list.clear()
                my_list.append(c)
                temp += 1

            else:
                my_list.clear()
                my_list.append(c)
                temp += 1

    if temp > longest:
        output_list = my_list.copy()

    #for c in output_list:
        #print(c)

    return len(output_list)

print("Longest Substring With K Distinct Characters 5-16")
print("<-----------------START---------------<")
print(longest_substring_with_k_distinct_characters('aabcdefff', 3))
#print(longest_substring_with_k_distinct_characters('defffaabc', 3))
# 5 (because 'defff' has length 5 with 3 characters)
print("<-----------------END---------------<")


#Given a binary tree, return all values given a certain height h.
#5/15/20
class Node():
  def __init__(self, value, left=None, right=None):
    self.value = value
    self.left = left
    self.right = right

def valuesAtHeight(root, height):
    # Fill this in.
    print()

#     1
#    / \
#   2   3
#  / \   \
# 4   5   7

a = Node(1)
a.left = Node(2)
a.right = Node(3)
a.left.left = Node(4)
a.left.right = Node(5)
a.right.right = Node(7)
print("Get all Values at a Certain Height in a Binary Tree 5-15")
print("<-----------------START---------------<")
print(valuesAtHeight(a, 3))
# [4, 5, 7]
print("<-----------------END---------------<")



#You are given the root of a binary search tree.
# Return true if it is a valid binary search
# tree, and false otherwise. Recall that a
# binary search tree has the property that
# all values in the left subtree are less
# than or equal to the root, and all values
# in the right subtree are greater than or equal to the root.
#5/14/20

class TreeNode:
  def __init__(self, key):
    self.left = None
    self.right = None
    self.key = key

def is_bst(root):
    # Fill this in.
    if root == None:
        return None




a = TreeNode(5)
a.left = TreeNode(3)
a.right = TreeNode(7)
a.left.left = TreeNode(1)
a.left.right = TreeNode(4)
a.right.left = TreeNode(6)

print("Validate Binary Search Tree 5-14")
print("<-----------------START---------------<")
print(is_bst(a))

#    5
#   / \
#  3   7
# / \ /
#1  4 6
print("<-----------------END---------------<")






#You are given an array of integers. Return the
# smallest positive integer that is not present
# in the array. The array may contain duplicate entries.

#For example, the input [3, 4, -1, 1] should
# return 2 because it is the smallest positive
# integer that doesn't exist in the array.

#Your solution should run in linear time and use constant space.
#5/13/20

def first_missing_positive(nums):
    # Fill this in.
    print()

print("First Missing Positive Integer 5-13")
print("<-----------------START---------------<@@@@@@@@@@@@@@@@@@@@@@@@@@")
print(first_missing_positive([3, 4, -1, 1]))
print(first_missing_positive([1,2,4]))
# 2
print("<-----------------END---------------<")

#A look-and-say sequence is defined as the integer
# sequence beginning with a single digit in which
# the next term is obtained by describing the previous
# term. An example is easier to understand:

#Each consecutive value describes the prior value.

#1      #
#11     # one 1's
#21     # two 1's
#1211   # one 2, and one 1.
#111221 # #one 1, one 2, and two 1's.

#Your task is, return the nth term of this sequence.

def lookSay(list ,n):

    if n == 1:
        list.append(1)
        return list
    if n == 2:
        list.append(11)
        return list
    else:
        count = 0
        return lookSay(list,n-1)



print("Look and Say 5-12")
print("<-----------------START---------------<")
print(lookSay([],4))#input("Enter look/say number: ")))
# (d, 3)
print("<-----------------END---------------<")


#You are given the root of a binary tree. Return the deepest node (the furthest node from the root).

#Example:

#    a
#   / \
#  b   c
# /
#d

#The deepest node in this tree is d at depth 3.
#4/11/20

class Node(object):
  def __init__(self, val):
    self.val = val
    self.left = None
    self.right = None

  def __repr__(self):
    # string representation
    return self.val


def deepest(node):
    # Fill this in.
    count = 0
    last = None
    while node:
        count +=1
        if node.left != None:
            node = node.left

        elif node.right != None:
            node = node.right

        else:
            last = node
            node = None



    tup = (last,count)
    return tup


root = Node('a')
root.left = Node('b')
root.left.left = Node('d')
root.right = Node('c')

print("Deepest Node in a Binary Tree 5-11")
print("<-----------------START---------------<")
print(deepest(root))
# (d, 3)
print("<-----------------END---------------<")


#Given two strings A and B of lowercase letters,
# return true if and only if we can swap two
# letters in A so that the result equals B.

#Example 1:
#Input: A = "ab", B = "ba"
#Output: true
#Example 2:

#Input: A = "ab", B = "ab"
#Output: false
#Example 3:
#Input: A = "aa", B = "aa"
#Output: true
#Example 4:
#Input: A = "aaaaaaabc", B = "aaaaaaacb"
#Output: true
#Example 5:
#Input: A = "", B = "aa"
#Output: false
#5/10/20

class Solution:
  def buddyStrings(self, A, B):
      # Fill this in.
      status = True
      swap_count = 0

      if len(A) == len(B):
          for i in range(len(A)):
              if A[i] != B[i]:
                  A = swap(A,B[i],i)
                  swap_count+=1

      else:
          status = False

      if swap_count > 1:
          status = False

      return status

def swap(a_string, b_val, index_to_chage):
    new_str = ""
    temp = a_string[index_to_chage]
    found = index_to_chage+1

    while found < len(a_string):
        if a_string[found] == b_val:
            break
        found+=1

    if found >= len(a_string):
        found = len(a_string)-1

    new_str = a_string[:index_to_chage] + b_val + a_string[(index_to_chage+1):found] + temp + a_string[found+1:]
    #print(new_str + str(len(new_str)))

    return new_str


print("Buddy Strings Tree 5-10")
print("<-----------------START---------------<")
print(Solution().buddyStrings('aaaaaaabc', 'aaaaaaacb'))
# True
print(Solution().buddyStrings('aaaaaabbc', 'aaaaaaacb'))
# False
print("<-----------------END---------------<")

#You have a landscape, in which puddles can form.
# You are given an array of non-negative integers
# representing the elevation at each location.
# Return the amount of water that would accumulate if it rains.

#For example: [0,1,0,2,1,0,1,3,2,1,2,1] should
# return 6 because 6 units of water can get trapped here.

#       X
#   X███XX█X
# X█XX█XXXXXX
# [0,1,0,2,1,0,1,3,2,1,2,1]
#4/9/20

def capacity(arr):
    # Fill this in.
    diff = 0

    for i in range(1, len(arr)):

        left = arr[i]
        for j in range(i):
            left = max(left, arr[j])

        right = arr[i]

        for j in range(i + 1, len(arr)):
            right = max(right, arr[j])

        diff = diff + (min(left, right) - arr[i])

    return diff


print("Trapping Rainwater 5-09")
print("<-----------------START---------------<")
print(capacity([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]))
# 6
print("<-----------------END---------------<")


#Given a sorted list of numbers, change it
# into a balanced binary search tree.
# You can assume there will be no duplicate numbers in the list.
#5/8/20

from collections import deque

class Node:
  def __init__(self, value, left=None, right=None):
    self.value = value
    self.left = left
    self.right = right

  def __str__(self):
    # level-by-level pretty-printer
    nodes = deque([self])
    answer = ''
    while len(nodes):
      node = nodes.popleft()
      if not node:
        continue
      answer += str(node.value)
      nodes.append(node.left)
      nodes.append(node.right)

    return answer


def createBalancedBST(nums):
    # Fill this in.
    if not nums:
         return None

    mid = int(len(nums)/2)
    root = Node(nums[mid])


    root.left = createBalancedBST(nums[:mid])
    root.right = createBalancedBST(nums[mid+1:])

    return root


print("Create a Balanced Binary Search Tree 5-08")
print("<-----------------START---------------<")
tree = createBalancedBST([1, 2, 3, 4, 5, 6, 7])
print(createBalancedBST([1, 2, 3, 4, 5, 6, 7]))
#print(tree)

# 4261357
#   4
#  / \
# 2   6
#/ \ / \
#1 3 5 7
print("<-----------------END---------------<")





#You are given an array of k sorted singly
# linked lists. Merge the linked lists into
# a single sorted linked list and return it.
#5/7/20

class Node(object):
  def __init__(self, val, next=None):
    self.val = val
    self.next = next

  def __str__(self):
    c = self
    answer = ""
    while c:
      answer += str(c.val) if c.val else ""
      c = c.next
    return answer

def merge(lists):
    # Fill this in.
    locator = None
    a = lists[0]
    b = lists[1]

    if a.val < b.val:
        root = a
        a = a.next

    else:
        root = b
        b = b.next

    locator = root

    while a and b:
        if a.val < b.val:
            root.next = a
            a = a.next
            root = root.next

        else:
            root.next = b
            b = b.next
            root = root.next

    while a:
        root.next = a
        a = a.next
        root = root.next

    while b:
        root.next = b
        b = b.next
        root = root.next

    return locator

a = Node(1, Node(3, Node(5)))
b = Node(2, Node(4, Node(6)))

print("Merge K Sorted Linked Lists 5-07")
print("<-----------------START---------------<")
print(merge([a, b]))
# 123456
print("<-----------------END---------------<")


#You are given an array of integers.
# Find the maximum sum of all possible
# contiguous subarrays of the array.
#Example:
#[34, -50, 42, 14, -5, 86]
#Given this input array, the output should be 137.
# The contiguous subarray with the largest sum is [42, 14, -5, 86].
#Your solution should run in linear time.
#5/6/20

def max_subarray_sum(arr):
    # Fill this in.
    max_sum = 0
    output = []

    for n in arr:
        if len(output) == 0 and n > 0:
            output.append(n)

        elif (output[-1]+n) < 0:
            output.clear()

        else:
            output.append(output[-1]+n)

    if len(output) == 0:
        output.append(0)

    return max(output)

print("Contiguous Subarray with Maximum Sum 5-06")
print("<-----------------START---------------<")
print(max_subarray_sum([34, -50, 42, 14, -5, 86, -100]))
# 137
print("<-----------------END---------------<")


#Implement a queue class using two stacks.
# A queue is a data structure that supports
# the FIFO protocol (First in = first out).
# Your class should support the enqueue and
# dequeue methods like a standard queue.
#5/5/20

class Queue:

    def __init__(self):
        #Fill this in.
        self.list = []


    def enqueue(self, val):
        #Fill this in.
        self.list.append(val)


    def dequeue(self):
        #Fill this in.
        data = self.list[0]
        self.list.pop(0)

        return data


q = Queue()
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)


print("Queue Using Two Stacks 5-05")
print("<-----------------START---------------<")
print(q.dequeue())
print(q.dequeue())
print(q.dequeue())
# 1 2 3
print("<-----------------END---------------<")


#You are given an array. Each element represents
# the price of a stock on that particular day.
# Calculate and return the maximum profit you
# can make from buying and selling that stock only once.
#For example: [9, 11, 8, 5, 7, 10]
#Here, the optimal trade is to buy when the price is 5,
# and sell when it is 10, so the return value should be 5
# (profit = 10 - 5 = 5).
#5/4/20

def buy_and_sell(arr):
    #Fill this in.
    buy = arr[0]
    diff = 0
    profit_list = []

    for i in range(len(arr)):
        sell = arr[i]

        if buy > arr[i]:
            buy = arr[i]
            diff = 0

        if sell > buy:
            sell = arr[i]
            diff += sell - buy
            profit_list.append(diff)
            diff = 0


    return max(profit_list)

print("Maximum Profit From Stocks 5-04")
print("<-----------------START---------------<")
print(buy_and_sell([9, 11, 8, 5, 7, 10]))
# 5
print("<-----------------END---------------<")


#You are given an array of intervals - that is,
# an array of tuples (start, end). The array may
# not be sorted, and could contain overlapping
# intervals. Return another array where the
# overlapping intervals are merged.
#For example:
#[(1, 3), (5, 8), (4, 10), (20, 25)]
#This input should return
# [(1, 3), (4, 10), (20, 25)]
# since (5, 8) and (4, 10) can be merged into (4, 10).
#5/3/20

def merge(intervals):
    #Fill this in.
    output = []
    appended = False
    temp = intervals[0]
    output.append(temp)

    for n in intervals:
        start = n[0]
        end = n[1]


        for i in intervals:
            if start > i[0] and end < i[1]:
                start = i[0]
                end = i[1]
                output.append(i)
                appended = True
                break

        if not appended:
            if start != output[len(output)-1][0] and end != output[len(output)-1][1]:
                output.append(n)
                appended = False

        else:
            appended = False

    return output




print("Merge Overlapping Intervals 5-03")
print("<-----------------START---------------<")
print(merge([(1, 3), (5, 8), (4, 10), (20, 25)]))
# [(1, 3), (4, 10), (20, 25)]
print("<-----------------END---------------<")



#You are given an array of integers. Return the
# largest product that can be made by multiplying
# any 3 integers in the array.
#Example:
#[-4, -4, 2, 8] should return 128 as the largest
# product can be made by multiplying -4 * -4 * 8 = 128.
#5/2/20

def maximum_product_of_three(lst):
    # Fill this in.
    one = 0
    two = 0
    three = 0

    for i in range(len(lst)):
        value = abs(lst[i])

        if value > one:
            three = two
            two = one
            one = value

        elif value > two:
            three = two
            two = value

        elif value > three:
            three = value


    return one*two*three


print("Largest Product of 3 Elements 5-02")
print("<-----------------START---------------<")
print(maximum_product_of_three([-4, -4, 2, 8]))
# 128
print("<-----------------END---------------<")


#You are given a 2D array of integers.
# Print out the clockwise spiral traversal of the matrix.
#Example:
#grid = [[1,  2,  3,  4,  5],
#        [6,  7,  8,  9,  10],
#        [11, 12, 13, 14, 15],
#        [16, 17, 18, 19, 20]]
#The clockwise spiral traversal of this array is:
#1, 2, 3, 4, 5, 10, 15, 20, 19, 18, 17, 16, 11, 6, 7, 8, 9, 14, 13, 12
#5/01/20

def matrix_spiral_print(M):
    #Fill this in.
    trav_list = []
    flag = False

    vertical = len(M)-1
    horizontal = len(M[0])-1
    row = 0
    colum = 0

    while horizontal >= 0 and vertical >= 0:
        if horizontal == 0:
            horizontal = 1

        if row >=0 and colum >=0:
            for i in range(horizontal): # horizontal right
                trav_list.append(M[row][colum])
                colum += 1

                if horizontal == 1 and flag:
                    horizontal = 0

            row = colum - horizontal

        if row >=0 and colum >=0:
            for i in range(vertical): # vertical down
                trav_list.append(M[row][colum])
                row += 1


        if row >= 0 and colum >= 0:
            for i in range(horizontal): # horizontal left
                #print(M[row][colum])
                trav_list.append(M[row][colum])
                colum -= 1


        if row >= 0 and colum >= 0:
            for i in range(vertical): # vertical up
                trav_list.append(M[row][colum])
                row -= 1


        row += 1
        colum += 1
        vertical -= colum
        horizontal -= row
        vertical-=1
        horizontal-=1
        flag = True

    print(trav_list)


print("Spiral Traversal of Grid 5-01")
print("<-----------------START---------------<")
grid = [[1,  2,  3,  4,  5],
        [6,  7,  8,  9,  10],
        [11, 12, 13, 14, 15],
        [16, 17, 18, 19, 20]]
matrix_spiral_print(grid)

grid = [[1,2,3],
        [4,5,6],
        [7,8,9]]
matrix_spiral_print(grid)
# 1 2 3 4 5 10 15 20 19 18 17 16 11 6 7 8 9 14 13 12
print("<-----------------END---------------<")


#Given a list, find the k-th largest element in the list.
#Input: list = [3, 5, 2, 4, 6, 8], k = 3
#Output: 5
#4/30/20

def findKthLargest(nums, k):
    # Fill this in.
    largest = 0
    index = 0

    while index <= k:
        if nums[index] > largest:
            largest = nums[index]

        index += 1

    return largest


print("k-th largest element 4-30")
print("<-----------------START---------------<")
print(findKthLargest([3, 5, 2, 4, 6, 8], 3))
# 5
print("<-----------------END---------------<")

#Given an array nums, write a function to move all 0's
# to the end of it while maintaining the relative order
# of the non-zero elements.
#Example:
#Input: [0,1,0,3,12]
#Output: [1,3,12,0,0]
#You must do this in-place without making a copy of the array.
#Minimize the total number of operations.
#4/29/20

class Solution:
    def moveZeros(self, nums):
        # Fill this in.
        temp = 0

        for i in range(len(nums)):
            if nums[i] != 0:
                temp = nums[i]
                for n in range(len(nums)):
                    if(nums[n] == 0):
                        nums[i] = nums[n]
                        nums[n] = temp
                        break



nums = [0, 0, 0, 2, 0, 1, 3, 4, 0, 0]
print("Move Zeros 4-29")
print("<-----------------START---------------<")
print("pre-> "+str(nums))
Solution().moveZeros(nums)
print("post-> "+str(nums))
# [2, 1, 3, 4, 0, 0, 0, 0, 0, 0]
print("<-----------------END---------------<")

#You are given a hash table where the key is a course code,
# and the value is a list of all the course codes that are
# prerequisites for the key. Return a valid ordering in which
# we can complete the courses. If no such ordering exists, return NULL.
#Example:
#{
#  'CSC300': ['CSC100', 'CSC200'],
#  'CSC200': ['CSC100'],
#  'CSC100': []
#}
#This input should return the order that we need to take these courses:
# ['CSC100', 'CSC200', 'CSCS300']
#4/28/20

def courses_to_take(course_to_prereqs):
    # Fill this in.
    class_order_list = []
    is_inserted = False
    fatal = False

    for course, req in course_to_prereqs.items():
        if len(class_order_list) == 0:
            class_order_list.append(course)
            #print("empty list appending -> "+ str(course))

        elif len(req) == 0:
            class_order_list.insert(0,course)
            #print("Front append -> "+ str(course))

        else:
            for i in range(len(class_order_list)):
                for r in course_to_prereqs[class_order_list[i]]:
                    if r == course and not is_inserted:
                        for w in req:
                            if w == class_order_list[i]:
                                print("invalid course list")
                                fatal = True

                        class_order_list.insert(i,course)
                        #print("inserting -> "+ str(i) + " "+ str(course))
                        is_inserted = True
                        break

                if is_inserted:
                    is_inserted = False
                    break

                elif not is_inserted and i == len(class_order_list) -1:
                    class_order_list.append(course)
                    #print("appending at end -> "+ str(course))


    if fatal:
        class_order_list.clear()


    return class_order_list

courses = {
  'CSC300': ['CSC100', 'CSC200'],
  'CSC200': ['CSC100'],
  'CSC100': []
}
print("Course Prerequisites 4-28")
print("<-----------------START---------------<")
print(courses_to_take(courses))
# ['CSC100', 'CSC200', 'CSC300']
print("<-----------------END---------------<")

#There are n people lined up, and each have a
# height represented as an integer. A murder
# has happened right in front of them, and only
# people who are taller than everyone in front of
# them are able to see what has happened. How many witnesses are there?
#4/27/20

def witnesses(heights):
    #Fill this in.
    w_list = []
    w_list.append(0)

    for i in range(len(heights)):
        if w_list[len(w_list) - 1] == heights[i]:
            w_list.pop

        elif w_list[len(w_list) - 1] < heights[i]:
            while w_list[len(w_list) - 1] < heights[i]:
                w_list.pop()
                if len(w_list) == 0 or w_list[len(w_list) - 1] > heights[i]:
                    w_list.append(heights[i])


        else:
            w_list.append(heights[i])


    print("Every actual witnness -> "+ str(w_list))

    return len(w_list)



print("Witness of The Tall People 4-27")
print("<-----------------START---------------<")
print("Everyone at the murder-> "+str([3, 6, 3, 4, 1]))
print("Total witnesses count -> "+ str(witnesses([3, 6, 3, 4, 1])))
# 3
print("<-----------------END---------------<")


#You are given a singly linked list and an integer k.
# Return the linked list, removing the k-th last element from the list.
#Try to do it in a single pass and using constant space.

class Node:
  def __init__(self, val, next=None):
    self.val = val
    self.next = next

  def __str__(self):
    current_node = self
    result = []
    while current_node:
      result.append(current_node.val)
      current_node = current_node.next
    return str(result)

def remove_kth_from_linked_list(head, k):
    # Fill this in
    cur = head
    prev = head
    output = prev

    while head:
        if head.val == k:
            if prev.val == k:
                prev = head.next
                cur = head.next
                output = prev

            else:
                prev.next = cur.next

        else:
            prev = cur
            cur = head.next

        head = head.next

    return output


print("Remove k-th Last Element From Linked List 4-26")
print("<-----------------START---------------<")
head = Node(1, Node(2, Node(3, Node(4, Node(5)))))
print(head)
# [1, 2, 3, 4, 5]
head = remove_kth_from_linked_list(head, 3)
print(head)
# [1, 2, 4, 5]
print("<-----------------END---------------<")


#Given a linked list of integers, remove all consecutive nodes that sum up to 0.
#Example:
#Input: 10 -> 5 -> -3 -> -3 -> 1 -> 4 -> -4
#Output: 10
#The consecutive nodes 5 -> -3 -> -3 -> 1 sums up to 0
# so that sequence should be removed. 4 -> -4 also sums
# up to 0 too so that sequence should also be removed.
# 4/25/20

class Node:
  def __init__(self, value, next=None):
    self.value = value
    self.next = next

def removeConsecutiveSumTo0(node):
    # Fill this in.
    head = node

    my_dict = {}
    sum = 0

    while node:
        temp =0
        sum += node.value

        if sum in my_dict:
            remove = my_dict[sum].next
            temp = sum

            while remove != node:
                temp += remove.value
                my_dict.pop(temp)
                remove = remove.next

            my_dict[sum].next = node.next


        else:
            my_dict[sum] = node

        node = node.next

    return head

node = Node(10)
node.next = Node(5)
node.next.next = Node(-3)
node.next.next.next = Node(-3)
node.next.next.next.next = Node(1)
node.next.next.next.next.next = Node(4)
node.next.next.next.next.next.next = Node(-4)
node = removeConsecutiveSumTo0(node)

print("Remove Consecutive Nodes that sum to 0 4-24")
print("<-----------------START---------------<")
while node:
  print(node.value)
  node = node.next
# 10
print("<-----------------END---------------<")

#Given a string with the initial condition of dominoes, where:

#. represents that the domino is standing still
#L represents that the domino is falling to the left side
#R represents that the domino is falling to the right side

#Figure out the final position of the dominoes.
# If there are dominoes that get pushed on both ends,
# the force cancels out and that domino remains upright.

#Example:
#Input:  ..R...L..R.
#Output: ..RR.LL..RR
#4/24/20

class Solution(object):
  def pushDominoes(self, dominoes):
      # Fill this in.
      output = []
      modified = False

      for c in dominoes:
          if len(output) == 0:
              output.append(c)

          elif c == '.':
              if output[len(output)-1] == 'R'and not modified:
                  output.append('R')
                  modified = True

              else:
                  output.append(c)
                  modified = False

          elif c == 'R':
                  output.append(c)
                  modified = False


          elif c == 'L':

              if output[len(output)-1] == '.' and not modified:
                 output.pop()
                 output.append(c)
                 output.append(c)
                 modified = False

              elif output[len(output) - 1] == 'R' and not modified:
                  output.pop()
                  output.append('.')
                  output.append('.')
                  modified = True

              elif modified:
                  output.append('.')
                  modified = True

      solution = ""

      for i in range(len(output)):
          solution+=output[i]

      return solution


print("Falling Dominoes 4-24")
print("<-----------------START---------------<")
print(Solution().pushDominoes('..R...L..R.'))
# ..RR.LL..RR
print("<-----------------END---------------<")


#You are given two singly linked lists.
# The lists intersect at some node. Find,
# and return the node. Note: the lists are non-cyclical.
#4/23/20

def intersection(a, b):
    # fill this in.
    a_dict = {}
    current = None


    while a:
        a_dict[a.val] = a
        a = a.next

    while b:
        if b.val in a_dict:
            if current == None:
                current = a_dict[b.val]
                head = current
            else:
                current = a_dict[b.val]

        b = b.next


    return head



class Node(object):
  def __init__(self, val):
    self.val = val
    self.next = None

  def prettyPrint(self):
    c = self
    while c:
      print(c.val)
      c = c.next

a = Node(1)
a.next = Node(2)
a.next.next = Node(3)
a.next.next.next = Node(4)

b = Node(6)
b.next = a.next.next

print("Intersection of Linked List 4-23")
print("<-----------------START---------------<")
c = intersection(a, b)
c.prettyPrint()
# 3 4
print("<-----------------END---------------<")



#You 2 integers n and m representing an n by m grid,
# determine the number of ways you can get from the
# top-left to the bottom-right of the matrix y going
# only right or down.
#4/22/20

def num_ways(n,m):
    #Fill this in.
    num_of_ways = 0
    grid = [[0]*n]*m

    for i in range(m):
        grid[i][0] = 1

    for i in range(n):
        grid[0][i] = 1

    for i in range(1,m):
        for x in range(1,n):
            grid[i][x] = grid[i-1][x] + grid[i][x-1]

    num_of_ways = grid[m-1][n-1]

    return num_of_ways

print("Ways to Traverse a Grid 4-22")
print("<-----------------START---------------<")
print(num_ways(2,2))
print("<-----------------END---------------<")


#Given an array of n positive integers and a positive integer s,
# find the minimal length of a contiguous subarray of which the
# sum ≥ s. If there isn't one, return 0 instead.
#Example:
#Input: s = 7, nums = [2,3,1,2,4,3]
#Output: 2
#Explanation: the subarray [4,3]
# has the minimal length under the problem constraint.
#4/21/20

class Solution:
  def minSubArrayLen(self, nums, s):
      #Fill this in
      sum = 0
      temp =0
      short_length = len(nums)


      for i in range(len(nums)):
          sum += nums[i]
          temp += 1

          if sum == s:
              if temp < short_length:
                  short_length = temp
                  temp = 1
                  sum = nums[i]

          elif sum > s:
              if(sum - s) < nums[i]:
                sum = nums[i-1] + nums[i]
                temp = 2
              else:
                  sum = nums[i]
                  temp = 1

      if short_length == len(nums):
          short_length = 0

      return short_length


print("Minimum Size Subarray Sum 4-21")
print("<-----------------START---------------<")
print(Solution().minSubArrayLen([2, 3, 1, 2, 4, 3], 7))
# 2
print("<-----------------END---------------<")

#You are given a 2D array of characters, and a target string.
# Return whether or not the word target word exists in the matrix.
# Unlike a standard word search, the word must be either
# going left-to-right, or top-to-bottom in the matrix.
# 4/20/20

def word_search(matrix, word):
    #Fill this in.
    status = False
    h_count = 0
    v_count = 0

    for i in range(len(matrix)):
        for x in range(len(matrix[i])):
            if word[x] == matrix[i][x]:
                h_count += 1

            if word[x] == matrix[x][i]:
                v_count += 1

        if h_count == len(word) or v_count == len(word):
            status = True
            break

        h_count = 0
        v_count = 0

    return status

matrix = [
    ['F', 'A', 'C', 'I'],
    ['O', 'B', 'Q', 'P'],
    ['A', 'N', 'O', 'B'],
    ['M', 'A', 'S', 'S'],]

print("Word search 4-20")
print("<-----------------START---------------<")
print(word_search(matrix, 'FOAM'))
print("<-----------------END---------------<")

# True

#Given an undirected graph, determine if a cycle exists in the graph.
# 4/19/20

def find_cycle(graph):
    #Fill this in.
    print()
graph = {
  'a': {'a2':{}, 'a3':{} },
  'b': {'b2':{}},
  'c': {}
}
print("Find Cycles in a Graph 4-19")
print("<-----------------START---------------<")
print(find_cycle(graph))
# False
graph['c'] = graph
print(find_cycle(graph))
# True
print("<-----------------END---------------<")




#Given a mathematical expression with just single digits,
# plus signs, negative signs, and brackets, evaluate the
# expression. Assume the expression is properly formed.
#Example:
#Input: - ( 3 + ( 2 - 1 ) )
#Output: -4
# 4/18/20
def reverse(str):
    r = ""
    for i in range(len(str)):
        if str[len(str) - 1 - i] != " ":
            r += str[len(str) - 1 - i]
    return r

def eval(expression):
    # Fill this in.
    stack = []
    total = 0
    exp = ""
    add = False
    subtract = False


    for op in expression:
        if op == ')':
            i=0
            while stack[len(stack)-1-i] != '(':
                exp += stack[len(stack)-1-i]
                stack.pop()

            exp = reverse(exp)
            for i in range(len(exp)):
                if exp[i] == "+":
                    add = True

                elif exp[i] == "-":
                    subtract = True

                elif total == 0:
                    total = int(exp[i])

                elif add:
                    total += int(exp[i])
                    add = False
                elif subtract:
                    total -= int(exp[i])
                    subtract = False

                else:
                    total += int(exp[i])

            exp =""
            stack.pop()


        else:
            stack.append(op)

    if stack[0] == "-":
        total *= -1

    return total


print("Simple Calculator 4-18")
print("<-----------------START---------------<")
print(eval('- (3 + ( 2 - 1 ) )'))
# -4
print("<-----------------END---------------<")


#Given two strings, determine the edit distance
# between them. The edit distance is defined as
# the minimum number of edits
# (insertion, deletion, or substitution)
# needed to change one string to the other.
#For example, "biting" and "sitting" have an
# edit distance of 2 (substitute b for s, and insert a t).
# 4/17/20

def distance(s1, s2):
    # Fill this in.
    count = 0
    index = 0

    return count

print("Edit distance 4-17")
print("<-----------------START---------------<*****************************")
print(distance('biting', 'sitting'))
# 2
print("<-----------------END---------------<")




#Given a list of numbers, find if there exists a
# pythagorean triplet in that list.
# A pythagorean triplet is 3 variables a, b, c where a2 + b2 = c2
# 4/16/20

def findPythagoreanTriplets(nums):
    # Fill this in.
    status = False
    my_dict = {}
    a = 0
    b = 0

    for n in nums:
        a = n
        for i in range(1,len(nums)):
            b = nums[i]
            total = a**2 + b**2
            my_dict[total] = 1

    for n in nums:
        if n**2 in my_dict:
            status = True

    return status




print("Find Pythagorean Triplets  4-16")
print("<-----------------START---------------<")
print(findPythagoreanTriplets([3, 12, 5, 13]))
# True
print("<-----------------END---------------<")



#You are given a positive integer N which
#represents the number of steps in a staircase.
#You can either climb 1 or 2 steps at a time.
# Write a function that returns the number of unique
# ways to climb the stairs.
# Can you find a solution in O(n) time?
# 4/15/20

def staircase(n):

    total_comb = 1
    x = 2

    for _ in range(n - 1):
        total_comb, x = x, total_comb + x


    return total_comb


# Fill this in.
print("Staircase  4-15")
print("<-----------------START---------------<")
print(staircase(4))
# 5
print(staircase(5))
# 8
print("<-----------------END---------------<")



#Implement a class for a stack that supports all
# the regular functions (push, pop) and an additional
# function of max() which returns the maximum element
# in the stack (return None if the stack is empty).
# Each method should run in constant time.
# 4/14/20

class MaxStack:

    def __init__(self):
        # Fill this in.
        self.items = []
        self.maximum = []

    def push(self, val):
        # Fill this in.
        self.items.append(val)
        length_of_list = len(self.maximum)

        if not self.maximum:
            self.maximum.append(val)

        elif val > self.maximum[length_of_list-1]:
            self.maximum.append(val)


    def pop(self):
        # Fill this in.
        temp = self.items.pop()



    def max(self):
        # Fill this in.
        if not self.items:
            return None
        else:
            temp = self.maximum.pop()

        return temp


print("Max in Stack 4-14")
print("<-----------------START---------------<")
s = MaxStack()

s.push(1)
s.push(2)
s.push(3)
s.push(2)
print(s.max())
# 3
s.pop()
s.pop()
print(s.max())
# 2
print("<-----------------END---------------<")


#You are given the root of a binary tree.
# all left children should become right children,
# and all right children should become left children.
# Invert the binary tree in place. That is,
# 4/13/20

class Node:
  def __init__(self, value):
    self.left = None
    self.right = None
    self.value = value

  def preorder(self):
    print(self.value)
    if self.left: self.left.preorder()
    if self.right: self.right.preorder()

def invert(node):
    # Fill this in.
    if node == None:
        return None

    else:
        temp_node = None

        invert(node.left)
        invert(node.right)

        temp_node = node.left
        node.left = node.right
        node.right = temp_node


root = Node('a')
root.left = Node('b')
root.right = Node('c')
root.left.left = Node('d')
root.left.right = Node('e')
root.right.left = Node('f')


print("Inverted Binary Tree 4-13")
print("<-----------------START---------------<")
root.preorder()

# a b d e c f

print("\n")
invert(root)
root.preorder()
# a c f b e d
print(">-----------------END--------------->")



#Given an integer k and a binary search tree,
# find the floor (less than or equal to) of k,
# and the ceiling (larger than or equal to) of k.
# If either does not exist, then print them as None.
# 4/12/20

class Node:
    def __init__(self, value):
        self.left = None
        self.right = None
        self.value = value


def findCeilingFloor(root_node, k, floor=None, ceil=None):
    #Fill this in.
    if root_node == None:
        return -1
    if root_node.value == k:
        return k
    if root_node.value < k:
        return findCeilingFloor(root_node.right,k,floor,ceil)

    ceil = findCeilingFloor(root_node.left,k,floor,ceil)
    floor = root_node.left
    return (floor.value,ceil) if ceil >= k else root_node.value




root = Node(8)
root.left = Node(4)
root.right = Node(12)

root.left.left = Node(2)
root.left.right = Node(6)

root.right.left = Node(10)
root.right.right = Node(14)


print("Binary Tree floor and ceiling find 4-12")
print("<-----------------START---------------<")
print(findCeilingFloor(root, 5))
# (4, 6)
print(">-----------------END--------------->")



#You are given an array of integers in an arbitrary order.
# Return whether or not it is possible to make the array
# non-decreasing by modifying at most 1 element to any value.
#We define an array is non-decreasing if
# array[i] <= array[i + 1] holds for every i (1 <= i < n).
#Example:
# [13, 4, 7] should return true, since we can modify 13 to any value 4 or less, to make it non-decreasing.
#[13, 4, 1] however, should return false, since there is no way to modify just one element to make the array non-decreasing.
#4/11/20

def check(num_array):
    # Fill this in.
    status = True
    flag = 0

    for i in range(len(num_array)-1):
            if num_array[i] > num_array[i+1]:
                flag += 1

    if flag > 1:
        status = False

    return status

print("INTERGERS IN AN ARBITRARY ORDER 4-11")
print("<-----------------START---------------<")
print([13, 4, 1])
print(check([13, 4, 1]))
# False
print([1, 4, 7])
print(check([1, 4, 7]))
# True
print([13, 4, 7])
print(check([13, 4, 7]))
# True
print([5,1,3,2,5])
print(check([5,1,3,2,5]))
# False
print(">-----------------END--------------->")


#Given a list of numbers, where every number shows up
# twice except for one number, find that one number.
#Example:
#Input: [4, 3, 2, 4, 1, 3, 2]
#Output: 1
#4/10/20

def singleNumber(nums):
    num_dict = {nums[0]: 0}
    index = 0

    for i in range(len(nums)):
        if nums[i] in num_dict:
            temp = nums[i]
            num_dict[temp] = num_dict.get(nums[i]) + 1
            index = i
        else:
            temp = nums[i]
            num_dict[temp] = 1

    #for key, value in num_dict.items():
    #    print(key, value)
    key_list = list(num_dict.keys())
    value_list = list(num_dict.values())

    print("This number appears only once: ")# + str(key_list[value_list.index(1)]))

    return key_list[value_list.index(1)]



print("SINGLE NUMBER SHOW-UP 4-10")
print("<-----------------START---------------<")
print([4, 3, 2, 4, 1, 3, 2])
print(singleNumber([4, 3, 2, 4, 1, 3, 2]))
#1
print(">-----------------END--------------->")



#You are given a list of numbers, and a target number k.
# Return whether or not there are two numbers in the list
# that add up to k.
#Example:
#Given [4, 7, 1 , -3, 2] and k = 5,
#return true since 4 + 1 = 5.
#4/9/20

def two_sum(list, k):
    # Fill this in.
    status = False
    sum_list = {}

    for i in list:
        if i < k:
            sum_list[i] = k-i

    for x in sum_list.values():
          if x in sum_list:
            status = True
            break


    return status

print("Number in List that Adds to Target Numbers 4-9")
print("<-----------------START---------------<")
print(two_sum([4,7,1,-3,2], 5))
# True
print("<-----------------START---------------<")


#Given a list of numbers with only 3 unique
# numbers (1, 2, 3), sort the list in O(n) time.
#Example 1:
#Input: [3, 3, 2, 1, 3, 2, 1]
#Output: [1, 1, 2, 2, 3, 3, 3]
#4/8/20


def sortNums(nums):
    # Fill this in.
    one = []
    two = []
    three = []

    for i in nums:
        if i == 1:
            one.append(i)
        if i == 2:
            two.append(i)
        if i == 3:
            three.append(i)

    results = one+two+three

    return results

print("Sort a List 4-8")
print("<-----------------START---------------<")
print(sortNums([3, 3, 2, 1, 3, 2, 1]))
# [1, 1, 2, 2, 3, 3, 3]
print("<-----------------END---------------<")


# Given a singly-linked list, reverse the list. This can be done
# iteratively or recursively. Can you get both solutions?
# Input: 4 -> 3 -> 2 -> 1 -> 0 -> NULL
# Output: 0 -> 1 -> 2 -> 3 -> 4 -> NULL
# 4/7/20

class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

    # Function to print the list
    def printList(self):
        node = self
        output = ''

        while node != None:
            output += str(node.val)
            output += " "
            node = node.next
        print(output)

    # Iterative Solution
    def reverseIteratively(self, head):
        # Implement this.
        prev = None
        current = self

        while current is not None:
            next = current.next
            current.next = prev
            prev = current
            current = next
        self = prev
       

    # Recursive Solution
    def reverseRecursively(self, head):
        # Implement this.
        print("")


# Test Program
# Initialize the test list:
testHead = ListNode(4)
node1 = ListNode(3)
testHead.next = node1
node2 = ListNode(2)
node1.next = node2
node3 = ListNode(1)
node2.next = node3
testTail = ListNode(0)
node3.next = testTail

print("Reverse the List Question 4-7")
print("<-----------------START---------------<")
print("Initial list: ")
testHead.printList()
# 4 3 2 1 0
testHead.reverseIteratively(testHead)
testHead.reverseRecursively(testHead)
print("List after reversal: ")
testTail.printList()
# 0 1 2 3 4
print("<-----------------END---------------<")


#Given a sorted array, A, with possibly duplicated elements,
# find the indices of the first and last occurrences of a
# target element, x. Return -1 if the target is not found.
# Input: A = [1,3,3,5,7,8,9,9,9,15], target = 9
# Output: [6,8]
#
# Input: A = [100, 150, 150, 153], target = 150
# Output: [1,2]
#
# Input: A = [1,2,3,4,5,6,10], target = 9
# Output: [-1, -1]
#4/6/20

class Solution:
  def getRange(self, arr, target):
      # Fill this in.
      first = None
      last = None

      for i in range(len(arr)):
          if arr[i] == target:
              if first == None:
                  first = i
              else:
                  last = i




      return first,last


# Test program
arr = [1, 2, 2, 2, 2, 3, 4, 7, 8, 8]
x = 2

print("First and Last Occurrences of Target Element 4-6")
print("<-----------------START---------------<")
print(Solution().getRange(arr, x))
# [1, 4]
print("<-----------------END---------------<")


#Imagine you are building a compiler. Before running any code,
# the compiler must check that the parentheses in the program
# are balanced. Every opening bracket must have a corresponding
# closing bracket. We can approximate this using strings.
#Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
#An input string is valid if:
#- Open brackets are closed by the same type of brackets.
#- Open brackets are closed in the correct order.
#- Note that an empty string is also considered valid.
# 4/5/20

class Solution:
  def isValid(self, s):
      # Fill this in.
      brackets = []
      status = False

      for c in s:
          if c == '(':
              brackets.append(c)

          elif c == '{':
              brackets.append(c)

          elif c == '[':
              brackets.append(c)

          elif c == ')' and len(brackets) > 0:
              if brackets[len(brackets)-1] == '(':
                  brackets.pop()

          elif c == '}' and len(brackets) > 0:
              if brackets[len(brackets) - 1] == '{':
                  brackets.pop()

          elif c == ']' and len(brackets) > 0:
              if brackets[len(brackets) - 1] == '[':
                  brackets.pop()


      if len(brackets) == 0:
          status = True

      return status
# Test Program
print("Corresponding Brackets Question 4-5")
print("<-----------------START---------------<")
s = "()(){(())"
# should return False
print(Solution().isValid(s))

s = ""
# should return True
print(Solution().isValid(s))
s = "([{}])()"
# should return True
print(Solution().isValid(s))
print("<-----------------END---------------<")

#A palindrome is a sequence of characters that reads
# the same backwards and forwards. Given a string, s,
# find the longest palindromic substring in s.
# 4/4/20

class Solution:
    def longestPalindrome(self, s):
        # Fill this in.
        found = False
        start_of_pal = 0
        end_of_pal = 0
        output_list = []

        for i in range(len(s)):
            if not found:
                for n in range(len(s)):
                    end = (len(s)-1) - n
                    if s[i] == s[end] and i != end:
                        found = Solution.pal_check(self, i,end,s)
                        if found:
                            start_of_pal = i
                            end_of_pal = end
                            break
            else:
                break

        while start_of_pal <= end:
            output_list.append(s[start_of_pal])
            start_of_pal += 1

        return output_list


    def pal_check(self, start, end,s):
        status = True

        while start < end:
            if s[start] != s[end]:
                status = False

            start +=1
            end -= 1

        return status




print("Longest Palindromic Substring 4-4")
print("<-----------------START---------------<")
# Test program
   # 0123456789
s = "tracecars"
print(str(Solution().longestPalindrome(s)))
# racecar

# find the longest palindromic substring in s.
print("<-----------------End---------------<")



#Given a string, find the length of the longest substring
# without repeating characters.
# 4/3/20

class Solution:
  def lengthOfLongestSubstring(self, s):
    # Fill this in.
    count = 0
    long_count = 0
    my_dict = {}

    for i in range(len(s)):
        if s[i] in my_dict:
            if count > long_count:
                long_count = count
                my_dict.clear()
            count = 0
        else:
            char = s[i]
            my_dict[char] = 1
            count += 1

    return long_count

print("Longest Substring Question4-3")
print("<-----------------START---------------<")
print(Solution().lengthOfLongestSubstring('abrkaabcdefghijjxxx'))
# 10
print("<-----------------END---------------<")



#You are given two linked-lists representing two
#non-negative integers. The digits are stored in
#reverse order and each of their nodes contain a
#single digit. Add the two numbers and return it as a linked list.
#Input: (2-> 4 ->3) + (5 -> 6 -> 4)
#Output: 7 -> 0 -> 8
#Explanation: 342 + 465 = 807
#4/2/20

# Definition for singly-linked list.
class ListNode(object):
  def __init__(self, x):
    self.val = x
    self.next = None

class Solution:
    def addTwoNumbers(self, l1, l2, c = 0):
        # Fill this in.
        new_list = None


        while l1 is not None:
            total = l1.val + l2.val+ c

            if total >= 10:
                total = total % 10
                c = 1

            if new_list is None:
                new_list = ListNode(total)
                head = new_list

            else:
                new_list.next = ListNode(total)
                new_list = new_list.next

            l1 = l1.next
            l2 = l2.next


        return head

l1 = ListNode(2)
l1.next = ListNode(4)
l1.next.next = ListNode(3)

l2 = ListNode(5)
l2.next = ListNode(6)
l2.next.next = ListNode(4)

result = Solution().addTwoNumbers(l1, l2)

print("Adding Linked list Question 4-2")
print("<-----------------START---------------<")

while result:
    print(result.val)
    result = result.next
    # 7 0 8

print("<-----------------END---------------<")

