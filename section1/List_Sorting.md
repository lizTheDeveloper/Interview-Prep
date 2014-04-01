List Sorting
==============
Students should be able to implement several sorting algorithms, and be able to explain the time and space complexity of each sort.  

##Goals##

* Familiarization with sorting algorithms
* Comfort writing and mentally testing algorithms
* More Advanced Big O Notation

##Resources##
http://stackoverflow.com/questions/471199/what-is-the-difference-between-n-and-on  

##Bubble Sort##
###Exercise###
Given an unordered list of integers, implement Bubble Sort, return the sorted list.
What is the time complexity?
What is the space complexity?

Advanced:
What is Big Omega?
What is Big Theta?

Examples:  
`[0,2,1,3,5]` -> `[0,1,2,3,5]`
`[5,4,3,2,1]` -> `[1,2,3,4,5]`
`[1,2,3,4,5]` -> `[1,2,3,4,5]`


Solutions:  
```python
x = 5
```

##Merge Sort##
###Exercise###
Given an unordered list of integers, implement Merge Sort, return the sorted list.

Examples:  
`[0,2,1,3,5]` -> `[0,1,2,3,5]`
`[5,4,3,2,1]` -> `[1,2,3,4,5]`
`[1,2,3,4,5]` -> `[1,2,3,4,5]`

Solutions:  
```python
x = 5
```

##Quicksort##
###Exercise###
Given an unordered list of integers, implement QuickSort, return the sorted list.

Examples:  
`[0,2,1,3,5]` -> `[0,1,2,3,5]`
`[5,4,3,2,1]` -> `[1,2,3,4,5]`
`[1,2,3,4,5]` -> `[1,2,3,4,5]`

Solutions:  
```python
x = 5
```

##Top 10##
###Exercise###
Given an unordered list of integers, return the 10 highest integers.


Examples:  
`[2,9,88,8,24,27,4,6,63,1,34,6,48,9,55,2,21,25,52,75,80,50,56,86,25,9,68,86,32,742,6732,753,13,6,4,32,5,65,3,2]` -> `[65, 68, 75, 80, 86, 86, 88, 742, 753, 6732]`
`[random.randint(1,10000000) for x in range(1,10000)]` -> `[9986018, 9988159, 9988505, 9989092, 9990058, 9991213, 9992473, 9993935, 9995767]`
Note: you won't get these exact numbers

Solutions:  
```python
x = 5
```

##Pivot##
###Exercise###
Given an unordered list of integers, find the center integer. Then, move all integers higher than the center integer to an index position higher than the center integer's position, and all integers lower than the center integer to an index position lower than the center integer's position.


Examples:  
[0,2,1,3,5] -> [0,1,2,3,5]
[5,4,3,2,1] -> [1,2,3,4,5]
[1,2,3,4,5] -> [1,2,3,4,5] 


Solutions:  
```python
x = 5
```
