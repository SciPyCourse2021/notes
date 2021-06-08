import numpy as np
import matplotlib.pyplot as plt

'''
# code used to generate the data:
t = np.arange(0, 100, 0.1)
x = np.random.normal(loc=5, scale=0.5, size=1000)
y = np.random.normal(loc=3, scale=0.25, size=1000)
np.savez('homework4.npz', t=t, x=x, y=y)
'''

# homework4 solution:

def absdiff(a, b):
    """Return the absolute difference between a and b"""
    a = np.asarray(a)
    b = np.asarray(b)
    return abs(a - b)

# load data:
d = np.load('homework4.npz')
list(d) # return array names (keys) in a list: ['t', 'x', 'y']
d.files # another way to return array names, again in a list
t, x, y = d['t'], d['x'], d['y'] # extract arrays

absd = absdiff(x, y)

# plot time series:
f, ax = plt.subplots()
ax.plot(t, x, marker='', label='x')
ax.plot(t, y, marker='', label='y')
ax.plot(t, absd, marker='', label='absd')
ax.set_xlabel('Time (s)')
ax.set_ylabel('Position (cm)')
ax.set_title('Time series')
ax.legend()
f.savefig('time_series.png')

# plot distributions:
f2, ax2 = plt.subplots()
bins = np.arange(0, 7.5, 0.1)
ax2.hist(x, bins=bins, label='x')
ax2.hist(y, bins=bins, label='y')
ax2.hist(absd, bins=bins, label='absd')
ax2.set_xlabel('Position (cm)')
ax2.set_title('Distributions')
ax2.legend()
f2.savefig('distributions.png')

# save t and absd to disk:
np.savez('t_absd.npz', t=t, absd=absd)
