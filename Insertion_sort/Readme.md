# Insertion Sort
## Introduction

<p>
  A simple sorting algorithm which works on the idea of picking elements from the unsorted part one by one and inserting them into their right positions in the sorted part. 
  The array is virtually divided into 2 parts, a sorted one and an unsorted one. 
  Just like we arrange a group of shuffled pages according to their page numbers, values from unsorted parts are picked and placed at the right positions in the sorted portion.
</p>


![image](https://user-images.githubusercontent.com/74819092/119613948-538bd700-be1b-11eb-8351-dec8333cb436.png)

* As we can see above, we start from the first 2 elements on the left. Comparing them we know that 3 < 4 so we need to position 3 before 4, so we swap their positions. <br>
* Next, 2 becomes the key element which we compare with all elements before it until we find something smaller than 2. Since 2 is smaller than both 3 and 4, we place it at the beginning of the array which is its correct position.
Since 12 is already larger than any element before it, its position is correct (for the current iteration).<br>
* Finally, comparing 9 with its predecessors, we see it's only smaller than 12 so we swap the positions of 9 and 12 to get the fully sorted array.<br>
## Algorithm
For sorting an array of size n in ascending order:

* Start your loop from ```arr[1]``` till ```arr[n]```
* Compare the selected element of the current iteration (key) to the element before it.
* If this key is smaller than its predecessor, compare it to the elements before the predecessor.
* Shift all the greater elements up by one position to make space for the smaller element.

# Complexity Analysis
n is the number of elements in the array.<br>

## Time Complexity:

Best Case: O (n)<br>
Average Case: O (n2)<br>
Worst Case: O (n2)<br>
Space Complexity: O (1)<br>
