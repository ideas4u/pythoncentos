"""

>>>is_palindrome_v3('noon')
True
>>> is_palindrome_v3('racecar')
True
>>> is_palindrome_v3('dented')
False

"""
def is_palindrome_v3(s):
	i = 0
	j = len(s) - 1
	while i < j and s[i] == s[j]:
		i = i + 1
		j = j - 1
	return j <= i
print is_palindrome_v3('noon')
print is_palindrome_v3('racecar')
print is_palindrome_v3('dentedn')
