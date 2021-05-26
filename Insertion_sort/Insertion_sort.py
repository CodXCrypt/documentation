"""
This is a pure Python implementation of the insertion sort algorithm
"""

""" Implementation of the insertion sort algorithm in Python
    :parameter array: A mutable ordered collection with comparable items inside
    
    :return : the same collection ordered by ascending
Input
Enter the size of list:
6
Enter the numbers:
5
0
2
1
4
3
Output
After Insertion sort: 
0   1   2   3   4   5
"""
def insertion_sort(array):
    # Loop from the second element of the array until
    # the last element
    for i in range(1, len(array)):
        # This is the element we want to position in its
        # correct place
        key_item = array[i]

        # Initialize the variable that will be used to
        # find the correct position of the element referenced
        # by `key_item`
        j = i - 1

        # Run through the list of items (the left
        # portion of the array) and find the correct position
        # of the element referenced by `key_item`. Do this only
        # if `key_item` is smaller than its adjacent values.
        while j >= 0 and array[j] > key_item:
            # Shift the value one position to the left
            # and reposition j to point to the next element
            # (from right to left)
            array[j + 1] = array[j]
            j -= 1

        # When you finish shifting the elements, you can position
        # `key_item` in its correct location
        array[j + 1] = key_item

    return array



if __name__ == "__main__":


    user_input = []
    n = int(input("Enter size of array: "))
    print("Enter array elements:\n")
    for i in range(0, n):
      user_input.append(int(input()))
    
    # calling the insertion_sort function
    sorted_collection = insertion_sort(user_input)
    print("After insertion sort")
    print(*sorted_collection, sep=" ")
