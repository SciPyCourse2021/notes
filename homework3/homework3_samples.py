"""Sample solutions from various students"""


## Exercise 2

y = []
for i in range(len(x1)):
    y.append(x1[i] * x2[i])
y = np.array(y)


for i in range(len(x1)):
    y = []
    y.append(x1*x2)
    np.array(y)
    print(y)


y = []
index = 0
for val in x1:
    newvalue = val * x2[index]
    index = index + 1
    y.append(newvalue)
y = np.array(y)


## Exercise 3


y = np.multiply(np.array(x1), np.array(x2))


y1 = np.array([a*b for a, b in zip(x1,x2)])


## Exercise 4

idx = ~(np.isnan(np.array(x1))) & (np.array(x2) != -1)
x1_new = np.array(x1)[idx]
x2_new = np.array(x2)[idx]
t_new = np.array(t)[idx]
len(x1_new) == len(x2_new) == len(t_new)


filterx1 = []
for element in x1:
    if element != np.nan:
        filterx1.append(True)
    else:
        filterx1.append(False)
newx1 = x1[filterx1]
filterx2 = []
for element in x2:
    if element != -1:
        filterx2.append(True)
    else:
        filterx2.append(False)
newx2 = x2[filterx2]


## np.delete is naughty! avoid unless absolutely necessary:
x1 = np.array(x1)
x2 = np.array(x2)
i_1 = np.isnan(x1)
i_2 = x2 == -1
i_g = i_1 + i_2
np.delete(x1, i_g)
np.delete(x2, i_g)
np.delete(t, i_g)


## tries to use integer fancy indexing instead of boolean fancy indexing:
j = np.where(~np.isnan(x1))[0] # positions where valid readings in x1 are
ii = np.where(x2 >= 0) [0] # positions where valid readings in x2 are
t_new = t_array[j & ii] # not sure if this is what we want


## uses integer fancy indexing in combination with np.concatenate and np.unique:
"""Finding out the indices of the invalid values"""
i1 = np.where(np.isnan(x1))
i2 = np.where(x2 < 0)
"""Returns 2 arrays, i1 and i2 with indices of the non valid values"""
d = np.unique(np.concatenate([i1, i2], axis = 1))
"""Remove values at the indices in d from x1, x2 and t"""
x1_new = np.delete(x1, d)
x2_new = np.delete(x2, d)
t_new = np.delete(t, d)


## also uses integer fancy indexing, in combination with only np.concatenate:
# Create boolean mask of invalid samples and remove them from all arrays
mask = np.concatenate((np.where(np.isnan(x1))[0], np.where(x2 == -1)[0]))
x1, x2, t = np.delete(x1,mask), np.delete(x2,mask), np.delete(t,mask)


# trying to delete the np.nan  values
x1clean = np.delete(x1array, np.where[x1 == np.nan]) ## needs np.isnan()!


#points with indexes 3, 12 and 19 need to be removed from all three arrays
indexes = [3, 12, 19]
x1_filtered = [i for j, i in enumerate(x1) if j not in indexes]
x2_filtered = [i for j, i in enumerate(x2) if j not in indexes]
t_filtered = [i for j, i in enumerate(t) if j not in indexes]


## uses np.invert instead of ~:
#Get boolean index of values in x1 that are not nan
nan_index = np.invert(np.isnan(x1))
#Get boolean index of values in x2 that are non-negative
pos_index = x2 >= 0
#Get combined boolean index that filters out corresponding values in t
index = nan_index & pos_index

## uses np.logical_or instead of |:
is_nan = np.isnan(x1)
is_neg = x2 == -1
is_either = np.logical_or(is_nan, is_neg)
x1 = x1[~is_either]
x2 = x2[~is_either]
t = t[~is_either]
