List Searching
==============
In this module, students should be able to give the time complexity and space complexity of their function. They should also be able to improve on functions that operate in greater than linear time.   

##Goals##

* Familiarization with searching lists given criteria
* Comfort with using list syntax on paper
* List syntax fluency & built-in method memorization
	* len()
	* .append() / .extend()
	* List Slicing
	* reverse()
	* map() and set()
	* x in l / x not in l
* Beginning Big O Notation
* Whiteboarding
	* Iterating on a whiteboard solution
	* Refactoring a whiteboard solution


##Missing Number##
###Exercise###
Write a function that takes a list as input. It is given that the list will contain every integer from 0..n+1, unordered, except one random integer. Return the missing integer.

Examples:  
`[0,4,2,1]` -> `3`  
`[2,0,3]` -> `1`  
`[0,1,2,3,5,7,6]` -> `4`  


Solutions:  
```python
x = 5
```

##Highest Int##
###Exercise###
Given an unordered list of integers, return the highest value.

Examples:  
`[5,4]` -> `5`  
`[4,5,-1,0,3,-15,12]` -> `12`  
`[0,-1,-1,-3,-2,0,-1]` -> `0`  

Solutions:  
```python
x = 5
```

##Highly Divisible##
###Exercise###
Given an ordered list of integers, find the integer that is divisible by the most other integers in the list. 

Examples:  
`[1,2,3,4,5,6,7]` -> `6`  
Because 6 can be divided by 2 and 3, which is the highest count of unique integers (2)  
`[1,2,3,4,5,6,7,8,9,10,11,12]` -> `12`  
Because 12 is divisible by 2,3,4,6, (4 unique integers) while everything else is only divisible by 2 unique integers found in the list.  

Solutions:  
```python
x = 5
```

##Binary Search##
###Exercise###
Given an ordered list of integers, and an integer to search for, return the index of the requested integer. Do this in sub-linear time.


Examples:  
`[1,2,3,4,5,6,7,8], 4` -> `3`  
`[5,10,15,20,25,30], 10` -> `1`  
`[3,6,9,12,15,18,21,24,27], 24` -> `7`  


Solutions:  
```python
x = 5
```

