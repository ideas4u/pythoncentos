"""

>>>is_palindrome_v2('noon')
True
>>> is_palindrome_v2('racecar')
True
>>> is_palindrome_v2('dented')
False

"""
def is_palindrome_v2(s):
	n = len(s)
	return s[ : n//2]  == reverse( s[n - n // 2 : ] )
def reverse(s):
	"""

	>>> reverse('hello')
	'olleh'
	>>> reverse('a')
	'a'
	"""
	rev = ''
	for ch in s:
		rev = ch + rev
	return rev
print is_palindrome_v2('noon')
print is_palindrome_v2('racecar')
print is_palindrome_v2('dentedn')

