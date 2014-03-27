Reverse
=======
##Goals##
* Familiarization with coding on paper
* Being comfortable with different solutions
* Ability to complete this task in less than 2 minutes
* Comfort solving problems on the board

##Exercise##
Write a function that accepts a string as input. It should return that string, reversed. You are not allowed to use inbuilt methods.

Examples:
"abc" -> "cba"
"cats" -> "stac"

Solutions:

```python
def reverse(s):
	new_str = ""
	for i in range(len(s)):
		new_str += s[i*-1]
	return new_str

```
