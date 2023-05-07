from ast import Not

from pyparsing import line


# def linear_Search(list, target):
#     for i in range(0, len(list)):
#         if list[i] == target:
#             return i
#     return None
# def linear_Search(list, target):
#     for i, j in enumerate(list):
#         if j == target:
#             return i
#     return None


# def verify(index):
#     if index is not None:
#         print('Target found at index: ', index)
#     else:
#         print("Target not found in list")

# numbers = [1,2,3,4,5,6,7,8,9]
# result = linear_Search(numbers, 12)
# verify(result)
# result = linear_Search(numbers, 6)
# verify(result)


# %%
#binary search
# def binary_Search(list, target):
#     first = 0
#     last = len(list) - 1

#     while first <= last:
#         midpoint = (first + last)//2
#         if list[midpoint] == target:
#             return midpoint
#         elif list[midpoint] < target:
#             first = midpoint + 1
#         else:
#             last = midpoint - 1

#     return None
            
# def verify(index):
#     if index is not None:
#         print('Target found at index: ', index)
#     else:
#         print("Target not found in list")

# numbers = [1,2,3,4,5,6,7,8,9]
# result = binary_Search(numbers, 12)
# verify(result)
# result = binary_Search(numbers, 6)
# verify(result)
# %%
# def recursive_binary_search(list, target):
#     if len(list) == 0:
#         return False
#     else:
#         midpoint = (len(list))//2

#         if list[midpoint] == target:
#             return True
#         else:
#             if list[midpoint] < target:
#                 return recursive_binary_search(list[midpoint+1:], target)
#             else:
#                 return recursive_binary_search(list[:midpoint], target)

# def verify(result):
#     print("Target found: ", result)
# numbers = [1,2,3,4,5,6,7,8,9]
# result = recursive_binary_search(numbers, 12)
# verify(result)
# result = recursive_binary_search(numbers, 6)
# verify(result)
# %%
# linked list.py
# class Node:
#     """
#     An object for storing a single node of a linked list.
#     Models two attributes - data and the link to the next node in the list

#     """
#     data = None
#     next_node = None
#     def __init__(self, data) -> None:
#         self.data = data
#     def __repr__(self) -> str:
#         return "<Node data: %s>" % self.data

    

# class LinkedList:
#     """
#     Singly linked list
#     """
#     def __init__(self):
#         self.head = None
#         # Maintaining a count attribute allows for len() to be implemented in
#         # constant time
#         self.__count = 0

#     def is_empty(self):
#         return self.head == None

#     def size(self):
#         """
#         the size of the list

#         Returns:
#             int: returns the number of nodes in the list
#             Takes O(n) time
#         """
#         current = self.head
        
#         count = 0

#         while current:
#             count += 1
#             current = current.next_node

#         return count

#     def add(self, data):
#         """
#         Adds new Node containing data to head of the list
#         Also called prepend
#         Takes O(1) time
#         Args:
#             data (int): value to be added
#         """
#         new_head = Node(data, next_node=self.head)
#         self.head = new_head
#         self.__count += 1

#     def search(self, key):
#         """
#         Search for the first node containing data that matches the key
#         Returns the node or `None` if not found
#         Takes O(n) time
#         """

#         current = self.head

#         while current:
#             if current.data == key:
#                 return current
#             else:
#                 current = current.next_node
                
#         return None

    

#     def insert(self, data, index):
#         """
#         Inserts a new Node containing data at index position
#         Insertion takes O(1) time but finding node at insertion point takes
#         O(n) time.
#         Takes overall O(n) time.
#         """

#         if index >= self.__count:
#             raise IndexError('index out of range')

#         if index == 0:
#             self.add(data)
#             return
#         if index > 0:
#             new = Node(data)
#             position = index
#             current = self.head

#             while position > 1:
#                 current = current.next_node
#                 position -= 1
                

#             prev_node = current
#             next_node = current.next_node

#             prev_node.next_node = new
#             new.next_node = next_node

#         self.__count += 1
        

    # def __len__(self):



    #     """
    #     Returns the length of the linked list
    #     Takesn O(1) time
    #     """

    #     return self.__count

    # def node_at_index(self, index):
    #     """
    #     Returns the Node at specified index
    #     Takes O(n) time
    #     """

    #     if index >= self.__count:
    #         raise IndexError('index out of range')

    #     if index == 0:
    #         return self.head

    #     current = self.head
    #     position = 0

    #     while position < index:
    #         current = current.next_node
    #         position += 1

    #     return current



#     def remove(self, key):
#             """
#             Removes Node containing data that matches the key
#             Returns the node or `None` if key doesn't exist
#             Takes O(n) time
#             """

#             current = self.head
#             previous = None
#             found = False

#             while current and not found:
#                 if current.data == key and current is self.head:
#                     found = True
#                     self.head = current.next_node
#                     self.__count -= 1
#                     return current
#                 elif current.data == key:
#                     found = True
#                     previous.next_node = current.next_node
#                     self.__count -= 1
#                     return current
#                 else:
#                     previous = current
#                     current = current.next_node

#             return None
#     def __repr__(self):
#         """
#         Return a string representation of the list.
#         Takes O(n) time.
#         """
#         nodes = []
#         current = self.head
#         while current:
        
#             if current is self.head:
#                 nodes.append("[Head: %s]" % current.data)
#             elif current.next_node is None:
#                 nodes.append("[Tail: %s]" % current.data)
#             else:
#                 nodes.append("[%s]" % current.data)
#             current = current.next_node
#         return  '-> '.join(nodes)



# %%
# merge sort
 # Let's define a recursive merge sort function. As usual, it takes the
# list or sub-list that we want it to sort.
def merge_sort(values):
  # Our base case is the same as with Quicksort. If the list has zero or one
  # values, there's nothing to sort, so we return it as-is.
  if len(values) <= 1:
    return values
  # If we didn't return, it means we're in the recursive case. So first we need
  # to split the list in half. We need to know the index we should split on,
  # so we get the length of the list and divide it by 2. So for example if
  # there are 8 items in the list, we'll want an index of 4. But what if there
  # were an odd number of items in the list, like 7? We can't have an index of
  # 3.5, so we'll need to round down in that case. Since we're working in
  # Python currently, we can take advantage of a special Python operator that
  # divides and rounds the result down: the floor division operator. It
  # consists of a double slash.
  middle_index = len(values) // 2
  # Now we'll use the Python slice syntax to get the left half of the list.
  # We'll pass that list to a recursive call to the merge_sort function.
  left_values = merge_sort(values[:middle_index])
  # We'll also use slice syntax to get the right half of the list, and pass
  # that to merge_sort as well.
  right_values = merge_sort(values[middle_index:])
  # Now we need to merge the two halves together, and sort them as we do it.
  # We'll create a list to hold the sorted values.
  sorted_values = []
  # Now we get to the complicated part - merging the two halves together and
  # sorting them as we do it.
  # We'll be moving from left to right through the left half of the list,
  # copying values over to the sorted_values list as we go. This left_index
  # variable will help us keep track of our position.
  left_index = 0
  # At the same time, we'll also be moving from left to right through the right
  # half of the list and copying values over, so we need a separate
  # right_index variable to track that position as well.
  right_index = 0
  # We'll keep looping until we've processed all of the values in both halves
  # of the list.
  while left_index < len(left_values) and right_index < len(right_values):
    # We're looking to copy over the lowest values first. So first we test
    # whether the current value on the left side is less than the value on the
    # right side.
    if left_values[left_index] < right_values[right_index]:
      # If the left side value is less, that's what we'll copy to the sorted
      # list.
      sorted_values.append(left_values[left_index])
      # And then we'll move to the next value in the left half of the list.
      left_index += 1
    # Otherwise, the current value from the right half must have been lower.
    else:
      # So we'll copy that value to the sorted list instead.
      sorted_values.append(right_values[right_index])
      # And then we'll move to the next value in the right half of the list.
      right_index += 1
  # At this point one of the two unsorted halves still has a value remaining,
  # and the other is empty. We won't waste time checking which is which.
  # We'll just copy the remainder of both lists over to the sorted list.
  # The one with a value left will add that value, and the empty one will add
  # nothing.
  sorted_values += left_values[left_index:]
  sorted_values += right_values[right_index:]
  # All the numbers from both halves should now be copied to the sorted list,
  # so we can return it.
  return sorted_values

list = [ 10, 23, 33, 33, 747, 5885, 824,]
l = merge_sort(list)
print(l) 
def verify_sorted(list):
    n = len(list)
    if n == 0 or n == 1:
        return True

    return list[0] < list[1] and verify_sorted(list[1:])

# %%
 #The function that randomizes the order of the list is kept in the
# "random" module, so we need to import that here.
import random
# The sys.argv list gives us the command line arguments to the
# script. To use it, we also need to import the "sys" module.
import sys
# Here's where we import the load_numbers function from above.
from load import load_numbers

# And here, we pass the first command line argument (which should be
# the path to a file) to load_numbers, and store the returned list of
# numbers in a variable.
numbers = load_numbers(sys.argv[1])

# Bogosort just randomly rearranges the list of values over and over,
# so the first thing it's going to need is a function to detect when
# the list is sorted. We'll write an is_sorted function that takes a
# list of values as a parameter. It will return True if the list
# passed in is sorted, or False if it isn't.
def is_sorted(values):
  # We'll loop through the numeric index of each value in the list,
  # from 0 to one less than the length of the list. Like many
  # languages, Python list indexes begin at 0, so a list with a
  # length of 5 has indexes going from 0 through 4.
  for index in range(len(values) - 1):
    # If the list is sorted, then every value in it will be less than
    # the one that comes after it. So we test to see whether the
    # current item is GREATER than the one that follows it.
    if values[index] > values[index + 1]:
      # If it is, it means the whole list is not sorted, so we return
      # False.
      return False
  # If we get down here, it means the loop completed without finding
  # any unsorted values. (Python uses whitespace to mark code blocks,
  # so un-indenting the code like this marks the end of the loop.)
  # Since all the values are sorted, we can return True.
  return True

# Now we need to write the function that will actually do the
# so-called sorting.  The bogo_sort function will also take the list
# of values it's working with as a parameter.
def bogo_sort(values):
  # We'll call our is_sorted function to test whether the list is
  # sorted. We'll keep looping until is_sorted returns True.
  while not is_sorted(values):
    # Python has a ready-made function that randomizes the order of
    # elements in a list. Since the list isn't sorted, we'll call
    # that function here. And since this is inside the loop, it will
    # be randomized over and over until our is_sorted function
    # returns True.
    random.shuffle(values)
  # If the loop exits, it means is_sorted returned True, and the list
  # is sorted.  So we can now return the sorted list.
  return values

# Finally, we need to call our bogo_sort function, pass it the list
# we loaded from the file, and print the sorted list it returns.
print(bogo_sort(numbers))
#%%
# This code here at the top is the same as we saw in the Bogosort
# example. It just loads a Python list of numbers from a file.
import sys
from load import load_numbers

numbers = load_numbers(sys.argv[1])

# Let's implement the function that will do our selection sort.
# We're going to pass in our Python list containing all the unsorted
# numbers.
def selection_sort(values):
  # We'll create an empty list that will hold all our sorted values.
  sorted_list = []
  # We'll loop once for each value in the list.
  for i in range(0, len(values)):
    # We call a function named index_of_min, which we're going to
    # write in just a minute, that find the minimum value in the
    # unsorted list and return its index.
    index_to_move = index_of_min(values)
    # Then we call the "pop" method on the list, and pass it the
    # index of the minimum value. pop will remove that item from the
    # list and return it. We then add that value at the end of the
    # sorted list.
    sorted_list.append(values.pop(index_to_move))
  # Going up a level of indentation signals to Python that we're
  # ending the loop. After the loop finishes, we return the sorted
  # list.
  return sorted_list

# Now we need to write the function that picks out the minimum value.
# We pass in the list we're going to search.
def index_of_min(values):
  # We mark the first value in the list as the minimum. It may or may
  # not be the actual minimum, but it's the smallest we've seen on
  # this pass through the list. (It's also the only value we've seen
  # on this pass through the list so far.)
  min_index = 0
  # Now we loop through the remaining values in the list after the
  # first.
  for i in range(1, len(values)):
    # We test whether the value we're currently looking at is less
    # than the previously recorded minimum.
    if values[i] < values[min_index]:
      # If it is, then we set the current index as the new index of
      # the minimum value.
      min_index = i
  # After we've looped through all the values, we return the index of
  # the smallest value we found.
  return min_index

# Lastly, we need to actually run our selection sort method, and
# print the sorted list it returns.
print(selection_sort(numbers))

#%%
# Again, you can ignore these lines at the top. We're just using them
# to load a file full of numbers into a list.
import sys
from load import load_numbers

numbers = load_numbers(sys.argv[1])

# The Quicksort algorithm relies on recursion. To implement it, we'll
# write a recursive function. We'll accept the list of numbers to
# sort as a parameter.
def quicksort(values):
  # Quicksort is recursive because it keeps calling itself with
  # smaller and smaller subsets of the list you're trying to
  # sort. We're going to need a base case where the recursion stops,
  # so it doesn't enter an infinite loop.  Lists that are empty don't
  # need to be sorted. And lists with just one element don't need to
  # be sorted, either. In both cases, there's nothing to flip
  # around. So we'll make that our base case; if there are 0 or 1
  # elements in the list passed to the "quicksort" function, we'll
  # return the unaltered list to the caller.
  if len(values) <= 1:
    return values
  # The code from here on out represents the recursive case.  We need
  # to create a list that will hold all the values less than the
  # pivot. That list will be empty at first.
  less_than_pivot = []
  # We do the same for values greater than the pivot.
  greater_than_pivot = []
  # Next we need to choose the pivot value. For now, we just grab the
  # first item from the list.
  pivot = values[0]
  # Then we loop through all the items in the list following the pivot.
  for value in values[1:]:
    # We check to see whether the current value is less than or equal
    # to the pivot.
    if value <= pivot:
      # If it is, we copy it to the sub-list of values less than the
      # pivot.
      less_than_pivot.append(value)
    # Otherwise, the current value must be greater than the pivot...
    else:
      # So we copy it to the other list.
      greater_than_pivot.append(value)
  # This last line is where the recursive magic happens. We call
  # quicksort recursively on the sub-list that's less than the
  # pivot. We do the same for the sub-list that's greater than the
  # pivot. Those two calls will return sorted lists, so we combine
  # the sorted values less than the pivot, the pivot itself, and the
  # sorted values greater than the pivot. That gives us a complete,
  # sorted list, which we return.
  return quicksort(less_than_pivot) + [pivot] + quicksort(greater_than_pivot)

# Lastly, we need to call our quicksort function with our list of
# numbers, and print the list it returns.
sorted_numbers = quicksort(numbers)
print(sorted_numbers)

#%%
# You may recognize this code at the top by now; it just loads a file
# full of numbers into a list.
import sys
from load import load_numbers

numbers = load_numbers(sys.argv[1])

# Let's define a recursive merge sort function. As usual, it takes
# the list or sub-list that we want it to sort.
def merge_sort(values):
  # Our base case is the same as with Quicksort. If the list has zero
  # or one values, there's nothing to sort, so we return it as-is.
  if len(values) <= 1:
    return values
  # If we didn't return, it means we're in the recursive case. So
  # first we need to split the list in half. We need to know the
  # index we should split on, so we get the length of the list and
  # divide it by 2. So for example if there are 8 items in the list,
  # we'll want an index of 4. But what if there were an odd number of
  # items in the list, like 7? We can't have an index of 3.5, so
  # we'll need to round down in that case. Since we're working in
  # Python currently, we can take advantage of a special Python
  # operator that divides and rounds the result down: the floor
  # division operator. It consists of a double slash.
  middle_index = len(values) // 2
  # Now we'll use the Python slice syntax to get the left half of the
  # list.  We'll pass that list to a recursive call to the merge_sort
  # function.
  left_values = merge_sort(values[:middle_index])
  # We'll also use slice syntax to get the right half of the list,
  # and pass that to merge_sort as well.
  right_values = merge_sort(values[middle_index:])
  # Now we need to merge the two halves together, and sort them as we
  # do it.  We'll create a list to hold the sorted values.
  sorted_values = []
  # Now we get to the complicated part - merging the two halves
  # together and sorting them as we do it.  We'll be moving from left
  # to right through the left half of the list, copying values over
  # to the sorted_values list as we go. This left_index variable will
  # help us keep track of our position.
  left_index = 0
  # At the same time, we'll also be moving from left to right through
  # the right half of the list and copying values over, so we need a
  # separate right_index variable to track that position as well.
  right_index = 0
  # We'll keep looping until we've processed all of the values in
  # both halves of the list.
  while left_index < len(left_values) and right_index < len(right_values):
    # We're looking to copy over the lowest values first. So first we
    # test whether the current value on the left side is less than
    # the value on the right side.
    if left_values[left_index] < right_values[right_index]:
      # If the left side value is less, that's what we'll copy to the
      # sorted list.
      sorted_values.append(left_values[left_index])
      # And then we'll move to the next value in the left half of the
      # list.
      left_index += 1
    # Otherwise, the current value from the right half must have been
    # lower.
    else:
      # So we'll copy that value to the sorted list instead.
      sorted_values.append(right_values[right_index])
      # And then we'll move to the next value in the right half of
      # the list.
      right_index += 1
  # At this point one of the two unsorted halves still has a value
  # remaining, and the other is empty. We won't waste time checking
  # which is which.  We'll just copy the remainder of both lists over
  # to the sorted list.  The one with a value left will add that
  # value, and the empty one will add nothing.
  sorted_values += left_values[left_index:]
  sorted_values += right_values[right_index:]
  # All the numbers from both halves should now be copied to the
  # sorted list, so we can return it.
  return sorted_values

# Finally, we need to kick the whole process off. We'll call the
# merge_sort function with the list of numbers we loaded, and print
# the result.
print(merge_sort(numbers))