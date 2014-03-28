String Parsing
=======
##Goals##
* Familiarization with coding on paper
* Being comfortable with different solutions
* Ability to complete these tasks in less than 5 minutes each
* Comfort solving problems on the board


##Reverse##

###Exercise###
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

##Palindromes##
###Exercise###
Write a function that accepts a string as input. It should return a boolean. True, if the string is a Palindrome. False, if the string is not. A Palindrome is the same string backwards and forwards, independent of case or spaces.


Examples:  
"A Toyotas a Toyota" -> True  
"otto" -> True  
"Godzilla!" -> False  
"Hostess" -> False  

Solutions:
```python
def palindrome(s):
    clean_string = s.lower().replace(" ", "")
    if clean_string == clean_string[::-1]:
        return True
    return False
```


##Substr##
###Exercise###
Write a function that accepts 2 strings as input. The function should search the first string for any occurrence of the second string.  
The function should return the index of the first occurrence of the second string within the first string. If the string has no occurrences, the function should return -1.  

Examples:  
"abcdef", "de" -> 3  
"quartz crystals", "z c" -> 5  
"Spanish Inquisition", "Nobody expects" -> -1  

Solutions:  
```python

```

##Split##
###Exercise###
Write a function that accepts 2 strings as input. The function should return a list based on dividing the first string by the second string. It should mimic the behavior of str.split(). If no character is passed in, the function should return the string divided by each character (ie, a list version of the string.)

Examples:  
"Hello my name is Liz", " " -> ["Hello", "my", "name", "is", "Liz"]  
"'Holy Smurf!' said Poppa Smurf, because the Smurfberries were gone!", "Smurf" -> ["'Holy ", "!' said Poppa", ", because the ", "berries were gone!"]  
"abcd" -> ["a", "b", "c", "d"]  
"hello all you happy people", "droopy" -> ["hello all you happy people"]  

Solutions:  
```python

```