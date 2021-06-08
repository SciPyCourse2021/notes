"""Sample snippets from student solutions"""

# no need to manually unzip the .npz and load each file separately, too much work!
# just use np.load() on the .npz file
a = np.load('x.npy')
b = np.load('y.npy')
t = np.load('t.npy')


# no need to iterate over array contents, either with a for loop or with list comprehension,
# use array operations instead:
def absdiff(a, b):
    output = []
    for i in range (len(a)):
        result = a[i]-b[i]
        c = abs(result)
        output.append(c)
    return output

def absdiff(x,y):
    """returns difference of absolute values of x and y"""
    z = []
    for val_x, val_y in zip(x,y):
        z.append(abs(val_x - val_y))
    return np.array(z)

# what's missing from this one?
def absdiff(x, y):
    """function will find absolute difference in corresponding values in sequences x and y"""
    return np.array([a - b for a, b in zip(x, y)])

# do we want to make assumptions about input/output data types for this function?
def absdiff(a,b):
    a = np.int64(a)
    b = np.int64(b)
    return abs(a - b)

# what does this do?
def absdiff(a,b):
    return abs(np.array([a])-np.array([b]))

# is all of this necessary?
def absdiff(a, b):
    """Returns diffrences between two sequences in an array"""
    aa = np.array(a)
    ba = np.array(b)
    c = np.array([])
    c = aa - ba
    return c

# is all of this necessary?
def absdiff(sequence_a, sequence_b):
    """ This function returns the absolute value of the difference between two sequences
    (arrays, lists, or tuples). It is assumed that the two input sequences have the same
    length. """
    #convert sequences to arrays
    a = np.array(sequence_a)
    b = np.array(sequence_b)
    c = np.zeros(len(sequence_a)) #create array
    c = abs(a-b)
    return c

# don't be afraid to overwrite existing variable names if you don't need the original
# values any more:
def absdiff(a, b):
    """returns the absolute value of the difference"""
    c = np.array(a)
    d = np.array(b)
    return c-d

# normally you shouldn't have imports inside of a function, better to do it once outside:
def absdiff(a, b):
    """Returns the absolute values of the difference of two sqeuences a, b"""
    import numpy as np
    x = np.array(a)
    y = np.array(b)
    return(abs(x - y))


# note the difference in binning: do you want the same bins for all 3 distributions,
# or a different set of bins for each distribution?
bins = np.arange(0, 7.5, 0.1)
plt.hist(x, bins=bins, label='x')
plt.hist(y, bins=bins, label='y')
plt.hist(absd, bins=bins, label='absd')

plt.hist(x, bins=30, label='x')
plt.hist(y, bins=30, label='y')
plt.hist(absd, bins=30, label='absd')

# for readability, don't leave spaces around = in kwargs in a function:
plt.hist(a, bins = 30, label = 'a')
plt.hist(b, bins = 30, label = 'b')
plt.hist(absd, bins = 30, label = 'absd')

# what does this do?
np.savez('t_absd.npz', t='t', absd='absd')

# what does this do?
np.savez('t_absd.npz', t, absd)

# what does this do?
np.savez('t_abs.npz', 't', 'absd')

