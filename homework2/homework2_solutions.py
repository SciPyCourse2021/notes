## Problem 1:

# append to a list with a for loop:
def norm(vals):
    """Return values normalized by the sum of the values"""
    s = sum(vals)
    out = []
    for val in vals:
        out.append(val / s)
    return out

# list comprehension:
def norm(vals):
    """Return values normalized by the sum of the values"""
    s = sum(vals)
    return [ val/s for val in vals ]

# norm() works just as well for tuple input as list input

# to return a tuple instead of a list:
    return tuple(out)
    return tuple([ val/s for val in vals ])
    return tuple( val/s for val in vals )


## Problem 2:

data = [[9.1, 2.1, 0.9, 1.5, 1.1],
        [4.4, 2.2, 3.3, 5.5, 6.6],
        [0.1, 0.2, 0.3, 0.4, 0.5]]

# append to a list with a for loop:
normdata = []
for row in data:
    normdata.append(norm(row))


# list comprehension:
normdata = [ norm(row) for row in data ]

'''
In [58]: normdata
Out[58]:
[[0.6190476190476191,
  0.14285714285714288,
  0.06122448979591837,
  0.10204081632653061,
  0.07482993197278913],
 [0.2, 0.1, 0.15, 0.25, 0.3],
 [0.06666666666666667,
  0.13333333333333333,
  0.19999999999999998,
  0.26666666666666666,
  0.3333333333333333]]
'''

# check each row is indeed normalized:
# with a for loop:
for row in normdata:
    print(sum(row))

# with list comprehension:
[ sum(row) for row in normdata ]

'''
Out[175]: [1.0, 1.0, 1.0]
'''

## Problem 3:

x = [2, 3, 4, 5, 0, 0, 0, 2, 2, 0]
y = [0, 4, 2, 4, 5, 1, 0, 5, 3, 5]

# append to a list with a for loop:
def vectorsum(x, y):
    """Return vector sum of x and y"""
    s = []
    for xx, yy in zip(x, y):
        s.append(xx + yy)
    return s

# list comprehension:
def vectorsum(x, y):
    """Return vector sum of x and y"""
    return [ sum(vec) for vec in zip(x, y) ]

# zip() stops iterating once it reaches the end of the shorter list


## Problem 4:

# list
def norm(vals):
    """Return values normalized by the sum of the values"""
    s = sum(vals)
    out = []
    for val in vals:
        out.append(val / s)
    return out

# dictionary
def normd(keyvals):
    """Return dict of key:value pairs normalized by the sum of the values"""
    s = sum(keyvals.values())
    out = {}
    for key, val in keyvals.items():
        out[key] = val / s
    return out


# list comprehension:
def norm(vals):
    """Return values normalized by the sum of the values"""
    s = sum(vals)
    return [ val/s for val in vals ]


# with dict comprehension:
def normd(keyvals):
    """Return dict of key:value pairs normalized by the sum of the values"""
    s = sum(keyvals.values())
    return { key:val/s for key, val in keyvals.items() }
