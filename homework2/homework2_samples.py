"""Sample solutions from various students"""

## Exercise 1


def norm (x):
    """accepts a list of values of arbitrary length N,
    and returns a list of the normalized values """
    lst=[]
    for i in list(x):
        lst.append(i/sum(x))
    print (lst)


def norm(x):
    """Returns a list with its normalised values"""
    normalised_list = []
    for i in x:
        ii = i /sum(x)
        normalised_list.append(ii)
        return normalised_list


l = []
def norm(l):
    """returns a list of normalized values"""
    norm = [float(i)/sum(l) for i in l]
    return (norm)


def norm(N):
    """Accepts a list of values, returns a list of normalized values"""
    return [ i / sum(N) for i in N ]


def norm(values):
    """Returns a list of the normalized values"""
    return list(i / sum(values) for i in values)



## Exercise 2


def norm(data):
    """accepts a list of lists of arbitrary length N, and returns a list of lists of
    the normalized values (each value divided by the sum of the values of each list)."""
    normdata = []
    normexperiment = []
    for experiment in data:
        for value in experiment:
            normexperiment.append(value/sum(experiment))
        normdata.append(normexperiment)
        normexperiment = []
    return normdata


normdata = [[],[],[]]
for i in range(0,len(data)):
    normdata[i] = norm(data[i])
    print(sum(normdata[i]))
print(normdata)


normdata = [norm(data[0]), norm(data[1]), norm(data[2])]


normdata = [norm(data[ii]) for ii in range(len(data))]


## Exercise 3


def vectorsum(x, y):
    """Returns the sum of the values at corresponding positions in two lists"""
    z = []
    for a,b in zip(x,y):
        z.extend([a+b])
    return z


def vectorsum(x, y):
    """Returns the vector sum of two lists x and y"""
    vec = [sum(i) for i in zip(x, y)]
    return vec


## Exercise 4


def normd(d):
    """ Takes a dict and returns same keys with normalized values in new dict """
    dd = { key: val/sum(d.values()) for (key, val) in d.items() }
    return dd


def normd(d):
    """ Accepts a dictionary of arbitrary length, and returns a dictionary with the same keys, but normalized values"""
    val = list(d.values())
    keys = list(d.keys())
    newval = []
    for i in range(len(val)):
        newval.append(val[i]/sum(val))
    dnormal = dict(zip(keys, newval))
    return dnormal


def normd(d):
    """Return a dictionary with normalized values"""
    s = sum(d.values())
    for key in d:
        d[key] = d[key] / s
    return d


# fancy!
def normd(d):
    """Returns a dictionary with normalized values"""
    return dict(zip(d.keys(), norm(d.values())))

