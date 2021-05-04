def vowelcount(s):
    """Count vowels in s"""
    s = s.lower()
    nv = 0
    for v in 'aeiou':
        nv += s.count(v)
    return nv

def metric(x, y):
    """Calculate difference over sum"""
    d = x - y
    s = x + y
    print('difference is %g, sum is %g' % (d, s))
    # optional: handle divide by zero:
    #if s == 0:
    #    return None
    return d / s

def multtable(n):
    """Print multiplication table from 1 to n"""
    for i in range(1, n+1): # rows
        for j in range(1, n+1): # columns
            print(i * j, end=' ')
        print() # move to new line for next row
