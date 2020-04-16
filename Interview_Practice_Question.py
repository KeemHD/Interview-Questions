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
    print("")
  # Fill this in.


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
    root = Node(8)
    root.left = Node(4)
    root.right = Node(12)

    root.left.left = Node(2)
    root.left.right = Node(6)

    root.right.left = Node(10)
    root.right.right = Node(14)

print("<-----------------START---------------<")
print("Binary Tree floor and ceiling find 4-12")
#print(findCeilingFloor(root, 5)
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

    for i in range(len(num_array)):

        if i != (len(num_array) -1):
            if num_array[i] > num_array[i+1]:
                flag = flag + 1

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
    print("")

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
    print("")

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
        print("")

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
# testHead.reverseRecursively(testHead)
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
    print("")

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
    print("")

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
      for i in range(len(s)):
          print(s[i])


print("Longest Palindromic Substring 4-4")
print("<-----------------START---------------<")
# Test program
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
            elif new_list.next is None:
                new_list.next = ListNode(total)
            else:
                new_list.next.next = ListNode(total)

            l1 = l1.next
            l2 = l2.next

        return new_list

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

