"""

>>>is_palindrome_vl('noon')
True
>>> is_palindrome_vl('racecar')
True
>>> is_palindrome_vl('dented')
False

"""
def is_palindrome_vl(s):
	return reverse(s) == s
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
print is_palindrome_vl('noon')
print is_palindrome_vl('racecar')
print is_palindrome_vl('dentedn')

