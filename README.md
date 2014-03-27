#Interview Prep#
  

Basic functions
================

##Exercises##
1. String Parsing
	1. Reverse
	2. Palindromes
	3. Substr
2. List Searching
	1. Missing Number
	2. Highest Int
	3. Highly Divisible
	4. Binary Search (and others)
3. List Sorting
	1. Sorts
		1. bubble
		2. merge
		3. quick
	2. Partial Sorts
		1. find top ten
		2. pivot
4. Math Things
	1. Prime Numbers
		1. return the nth prime
	2. Factorials
		1. what is n!
		2. largest common factor of two numbers
	3. Fib
		1. fib recursive
		2. fib non recursive
		3. fib with caching?

##Concepts##
1. Big O Notation  
2. Whiteboarding Strategies  
	1. Start at the top
	2. Write down the problem
	3. Problem Solving Out Loud - Keep talking
	4. Don't try to come up with the right answer first, just one that works
	5. How to ask clarifying questions
3. Basic Logic
4. Problem Structure  

##Unit Design##
Students are given a number of minutes (decreasing each day) to complete several problems on paper in the lecture hall. After that number of minutes elapses, students who have completed their questions are asked to demonstrate it on the board. Lecturers go over the different strategies used, and critique the efficiency and effectiveness of the solution. TAs are needed to check the validity of student's work, as it is on paper. Lecturers should strive to talk over the skills covered by each exercise, because some solutions to come problems may miss key concepts.  
  
Exercises are meant to get students comfortable with solving problems without an IDE present, with making mistakes, and with timed problem solving. Social pressure should be applied, but is not the main focus of this unit.  
##Suggested Reading##
###Hackbright Videos###
[Programming Interviews w/Noah Kindler](http://vimeo.com/79718197)  
###Books###
[Programming Interviews Exposed](http://www.amazon.com/Programming-Interviews-Exposed-Secrets-Landing/dp/1118261364/)  
[Cracking The Coding Interview](http://www.amazon.com/Cracking-Coding-Interview-Programming-Questions/dp/098478280X)  

###Relevant Exercises###
[Exercise 1](https://github.com/hackbrightacademy/Hackbright-Curriculum/tree/master/Exercise01)
[Exercise 2](https://github.com/hackbrightacademy/Hackbright-Curriculum/tree/master/Exercise02)
[Exercise 3](https://github.com/hackbrightacademy/Hackbright-Curriculum/tree/master/Exercise03)
[Exercise 4](https://github.com/hackbrightacademy/Hackbright-Curriculum/tree/master/Exercise04)
[Exercise 5](https://github.com/hackbrightacademy/Hackbright-Curriculum/tree/master/Exercise05)
[Exercise 6](https://github.com/hackbrightacademy/Hackbright-Curriculum/tree/master/Exercise06)
[Exercise 7](https://github.com/hackbrightacademy/Hackbright-Curriculum/tree/master/Exercise07)

###Other Resources###
[140 Google Interview Questions](http://www.impactinterview.com/2009/10/140-google-interview-questions/)

Data Structure Enhancements
===========================
##Exercises##
1. The Answer Is Dictionaries
	1. find if there are pairs
	2. Are all the letters from string a in string b?
	3. Roman Numerals
2. How To Write Your Own Hash Map
3. Other Ways To Hold On To Things
	1.Variables
	2. Lists
	3. Dictionaries
	4. Sets
	5. Objects!

##Concepts##
* Data structure as it relates to efficiency
	* Space
	* Time
* Objects

##Unit Design##
These exercises are longer and should be done in breakout sessions on various whiteboards. Emphasis is more on problem solving than speed, and making conceptual leaps out loud. This unit is designed to introduce social pressure while making conceptual leaps. Experimenting with group size should be done to find the right mix of pressure and even coverage of problems to students. Problems should be done in sets of increasing difficulty, so weaker students should attempt the early problems, and stronger students should attempt the later problems. 

Weaker students during this time will get the help they need with problem solving in general, and do not need the additional efficiency and complexity training that stronger students need, as they will typically end up in jobs where completing the problem presented in the interview is sufficient. 

Stronger students should focus their efforts on understanding the efficiency and complexity of problems that "build" on the concepts that the weaker students solve, as they will be more apt to face tougher interview questions with more room to express efficiency and understanding. 

##Suggested Reading##
###Hackbright Videos###

###Books###

###Relevant Exercises###

###Other Resources###

Trees / Linked Lists
====================
1. Linked Lists
	1. Find Tail
	2. Find Loops
	3. Find Kth Element
2. Trees
 	1. DFS
	2. BFS
	3. Binary Search
		a. Largest element
		b. 5th largest
			Efficiency 
	4. Red-Black Trees
	5. Equality
		a. total value of data
		b. actual equality
3. Graphs (optional)

##Concepts##
* Linked Lists
	* Nodes
*Trees
	* Nodes
	* Recursion
* Graphs
* Objects
* Object References
* Diagramming

##Unit Design##
Problems here are designed to reintroduce students to Object Oriented Programming, as they likely have not written much in the way of classes outside of SQLAlchemy. It will remind them that Objects are a data structure unto themselves. It it also meant to introduce students to more complex algorithms, and graph problems. Many students may have tackled graph-style problems in their projects, but have likely used a library that handled data structures for them, so will need to be reintroduced to these concepts.

Weaker students will be mostly focused on understanding the difference between an object and a reference, whereas stronger students will be more focused on complex structures such as red-black trees and graphs.

##Suggested Reading##
###Hackbright Videos###
[Object Oriented Programming Lecture](http://vimeo.com/76652734)
###Books###

###Relevant Exercises###

###Other Resources###
[Trees as a data structure (Wikipedia)](http://en.wikipedia.org/wiki/Tree_(data_structure))

OOP Concepts
============
1. Building
	1. Card games
	2. Chess
2. Vocab
	1. encapsulation
	2. Polymorphism
	3. Inheritance (versus)
	4. Composition
3. Patterns
	1. Inheritence
	2. Composite
	3. Chain of Responsibility
	4. Observer
		
##Concepts##
* Classes
* Object Instantiation
* Syntax
* Program Structure

##Unit Design##
Students by this time should be more comfortable with creating classes and objects, and so should branch out into different patterns of design, and know their names. Though this unit is not extensive enough to have students fully understand every type of OOP pattern, they should be familiar with Inheritence, Composite, potentially Chain of Responsibility and potentially Observer, as both are becoming more widely used in various web frameworks. 

Weaker students may not be able to complete the latter portions of this unit, but should understand how to use classes. 
##Suggested Reading##
###Hackbright Videos###
[Object Oriented Programming Lecture](http://vimeo.com/76652734)
###Books###

###Relevant Exercises###

###Other Resources###
[Design Patterns by Type (Wikipedia)](http://en.wikipedia.org/wiki/Design_Patterns#Patterns_by_Type)

Longer Problems
===============
1. Multiple Functions
	1. Given a set of coin denominators, find the minimum number of coins to give a certain amount of change.
	2. Given an array, i) find the longest continuous increasing subsequence. ii) find the longest increasing subsequence.
	3.Predictive Text / Spell Checker

##Concepts##
* Stubbing Functions
* Problem Solving in Multiple Steps
* Syntax "looseness" for whiteboarding problems

##Unit Design##
By now students typically have difficulty envisioning problems that require more than one function to solve, or don't involve recursion or objects. This section is intended to remind students that composing functions and their use took up the bulk of their work to date, and that frequently whiteboarding problems are easier to solve if they break them down into smaller functions. 
This unit is generally intended to help their whiteboarding strategy and so the placement of this unit is more about where the student is and less about conceptual similarity to other units.

The difficulty of this unit should restore the confidence of students struggling with OOP concepts as well, and should help students who have difficulty breaking down large problems by having them start by deciding which functions they will need to solve the problem. 

This module should also introduce syntax looseness - shortening of variable names, not bothering to write boilerplate code, and should make students comfortable with working through a large problem on a whiteboard by intentionally choosing what to complete, and what to demonstrate mastery of verbally. 
##Suggested Reading##
###Hackbright Videos###
[Some Video](http://vimeo.com/70713816)
###Books###

###Relevant Exercises###

###Other Resources###


Brain Teasers
=============
1. Estimation
	1. How many jelly beans in a jar? in a house? in a 747?
2. Problems that are Programming
	1. 100 story tower, you have two boxes, find the lowest floor you can drop boxes from
	2. 100 bottles of wine, one is poisoned - you have an hour, poison takes an hour, fewest number of servants
3. Other Problems
	1. box with water and a boat, throw something off boat - water level rise or fall or stay the same?
4. Problems in the Real World
		
##Unit Design##
Brain Teasers as a module is designed to familiarize students with the process of solving something that does not involve using code. Problems around estimation, order of magnitude, and problems that involve computer science concepts without computers. Teaching students to spot computer science problems in the real world will help them come across better in interviews, and teach them not to get stuck by problems whose solution is not obvious. The idea of real-world problems being solved mathematically will be best absorbed by students with a strong math background, but all students should be able to benefit from this unit.

##Suggested Reading##
###Hackbright Videos###
[Some Video](http://vimeo.com/70764383)
###Books###

###Relevant Exercises###

###Other Resources###

Kahn Academy
	Basic Algebra
	Linear Algebra
	Applied Math
Vi Hart Videos
	http://www.youtube.com/watch?v=e4MSN6IImpI&list=SPF7CBA45AEBAD18B8
	http://www.youtube.com/watch?v=a-e8fzqv3CE&list=PLC20F52B96F3E8206
		
Pairing - review
================
1. Pairing on code
2. Pairing on TDD
3. Pairing on a codebase

##Unit Design##
This is less a module and more a suggestion to our students to pair with their mentors, and what they should do on their own to study. 

##Suggested Reading##
###Hackbright Videos###
###Books###
###Relevant Exercises###
###Other Resources###
Technology
==========
1. How does the internet work?
	1. DNS, Routers, Hubs, Request/Response, HTTP / TCP/IP (deep as you can get)
2. What is the request / response lifecycle / what happens when you type google.com into a browser?
3. GET v POST
	1. Explain the difference
	2. Know the syntax of an HTTP Request
	3. Understand what a post body looks like / URL Encoding
			
##Suggested Reading##
###Hackbright Videos###
[Some Video](http://vimeo.com/89469263)
###Books###
###Relevant Exercises###
###Other Resources###

Databases
==========
1. Schema Design
2. Write SQL Queries
3. Indexes & Constraints

##Suggested Reading##
###Hackbright Videos###
###Books###
###Relevant Exercises###
###Other Resources###

Software Engineering
====================
1. Explain MVP
2. Explain Functional Programming
3. Explain OOP
4. Explain Dynamic Programming

##Suggested Reading##
###Hackbright Videos###
###Books###
###Relevant Exercises###
###Other Resources###



Resources:
http://www.impactinterview.com/2009/10/140-google-interview-questions/
http://en.wikipedia.org/wiki/Design_Patterns
http://en.wikipedia.org/wiki/Tree_(data_structure)