def is_palindrome(n):
    '''
    Verifies if a given number n is a palindrome
    '''
    if str(n) == str(n)[::-1]:
        return True
    else:
        return False

palins = []
for x in xrange(100, 1000):
    for y in xrange(100, 1000):
        if is_palindrome(x*y):
            palins.append(x*y)

print max(palins)
