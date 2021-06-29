## images

# NOTE: you might have to run `pip install imagecodecs` in order for skimage to be able
# to ready .tif files

import matplotlib.pyplot as plt
from skimage import io
data = io.imread('nissl.tif') # load the image
data.shape # (2048, 2048, 3)
data.dtype # uint8
f1, ax1 = plt.subplots()
ax1.imshow(data)

(data[:, :, 0] != 0).any() # False: no signal in red channel
(data[:, :, 1] != 0).any() # True: signal in green channel
(data[:, :, 2] != 0).any() # False: no signal in blue channel

green = data[:, :, 1]
green.shape # (2048, 2048)

inv = 255 - green # maximum uint8 value is 255

subsampled = inv[::2, ::2]
subsampled.shape # (1024, 1024)

f2, ax2 = plt.subplots()
ax2.imshow(subsampled, cmap='gray')

io.imsave('nissl_gray.png', subsampled)


## pandas

import pandas as pd
data = pd.read_csv('stroop_data.csv')
len(data) # 1953 trials

description = data.groupby('subject').describe()
len(description) # 22 subjects
# this is also valid, sort of manually accomplishes what groupby() does automatically:
stroop['subject'].nunique() # 22 subjects

description['reaction_time']['mean'].mean() # 1644.6076765320759
# faster alternative without calcuating everything in `.describe()`:
data.groupby('subject')['reaction_time'].mean().mean() # 1644.6076765320759

# plot reaction time distribution:
f, ax = plt.subplots()
nbins = 30
ax.hist(data['reaction_time'], bins=nbins) # not very normal looking
ax.set_xlabel('Reaction time (ms)')
ax.set_ylabel('Trial count')
f.canvas.set_window_title('Reaction time distribution')

# plot log reaction time distribution:
f2, ax2 = plt.subplots()
edges = np.logspace(2, 4, nbins+1) # num edges is always 1 more than number of desired bins
ax2.hist(data['reaction_time'], bins=edges)
ax2.set_xscale('log')
ax2.set_xlabel('Log Reaction time (ms)')
ax2.set_ylabel('Trial count')
f2.canvas.set_window_title('Log Reaction time distribution')
# looks like a bimodal distribution, perhaps the very fast reaction times are outliers
