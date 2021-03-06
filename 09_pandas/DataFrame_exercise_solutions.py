import pandas as pd

gdf = pd.read_csv('Galton.csv')

# sometimes a useful option to print all rows, resets when you restart Python:
pd.set_option('display.max_rows', None)

# Yes, lots of redundant data. No need to repeatedly report the mother and father's heights
# for each kid, or even the number of kids per family (which can be inferred by counting the
# number of rows for each unique family ID). Ideally, the mother and father's heights and
# the kids count per family should be removed from this table and put in another one
# (maybe call it a "Family" table), that uses the same unique family IDs as the family
# column in this table. Then you can easily cross-reference between the two, while
# removing redundancy, and potentially errors due to redundancy.

nrows = len(gdf) # number of kids in dataset, one row per kid: 898

fam = gdf.groupby('Family') # analyze by family
len(fam) # number of families, i.e. number of unique values in family column: 197
# alternative:
gdf['Family'].nunique() # 197

fam.count() # returns number of rows per family, all columns identical
fam.count()['Kids'] # number of rows, i.e. kids, per family
# count num entries for each family, then sum them up. Could do sum on any of the columns
# and get the same result, doesn't actually care about the values in the 'kids' column:
fam.count()['Kids'].sum() # also 898, just another way of counting rows

# to actually consider the values stored in the kids column and check if they're correct,
# need to reduce the multiple entries per family down to a single number: max, min, mean,
# median, etc, any one of them will do, because we expect the kid count for each entry
# within the same family to be the same:
fam.max()['Kids'].sum() # 899, different result!
fam.min()['Kids'].sum() # 899
fam.mean()['Kids'].sum() # 899
fam.median()['Kids'].sum() # 899
# this does the same, just different order of operations, more efficient, only does
# the reduction (max) calcuation on the column we care about:
fam['Kids'].max().sum()

# something is clearly wrong. Somewhere the number of rows (entries) per family doesn't equal
# the kid count for that family:
fam.count()['Kids'] == fam.max()['Kids']
(fam.count()['Kids'] == fam.max()['Kids']).all() # False, as expected, but where?
np.where(fam.max()['Kids'] != fam.count()['Kids'])[0] # 32, i.e. row 32 has a problem
fam.count().iloc[32] # family 130 has 10 rows, i.e. 10 reported kids in the dataset
# but, the values in the kid column for family 130 say it actually has 11 kids,
# again, max, min, mean, etc. all do the same required reduction in this case:
fam.max().iloc[32]
# so one row (kid) is missing for this family!

# calculate mean child height and plot distribution:
gdf['Height'].mean() # 66.76
ax = gdf['Height'].hist()
ax.set_xlabel('Child height (in)')
ax.set_ylabel('Count')

# remove family 136A:
subset = gdf.loc[gdf['Family'] != '136A'] # now only 890 rows, i.e. kids
len(subset.groupby('Family')) # 196

# mean Father and Mother heights. Need to do 2 reductions, one within family, one across.
# The reduction withing the family can be anything (max/min/mean...) since all the values
# within a family should be the same. The 2nd reduction across families needs to be mean:
fam['Father'].max().mean() # 69.35
fam['Mother'].max().mean() # 63.98

# this results in redundant points plotted on top of each other, though that doesn't
# really make a difference visually:
ax = gdf.plot.scatter('Father', 'Mother')
# this plots each point only once, by grouping by family and including only the father
# and mother heights, reducing them each to a single value per family,
# resulting in a simple 2D Dataframe, from which one can do an ordinary scatter plot:
ax = fam[['Father', 'Mother']].max().plot.scatter('Father', 'Mother')

# full correlation matrix of all columns vs. all columns, but weights families with more
# children more heavily, so incorrect result:
gdf.corr()
# can extract specific columns from a DataFrame by just listing the columns you want,
# in a list or tuple:
gdf[['Father', 'Mother']].corr() # the off diagonal value is what we want
gdf[['Father', 'Mother']].corr().iloc[1, 0] # 0.07366, pretty weak
# but that still doesn't deal with the redundancy. The correct way is to
# again group by family and do a reduction:
fam[['Father', 'Mother']].max().corr().iloc[1, 0] # 0.101, slightly stronger than we thought

# calculate mean child height per family:
mgdf = pd.DataFrame() # create a new empty DataFrame
mgdf['MeanHeight'] = fam['Height'].mean() # add a MeanHeight column
mgdf['Father'] = fam['Father'].max() # add a Father column, any reduction (max, min, etc) works
mgdf['Mother'] = fam['Mother'].max()
ax = mgdf.plot.scatter('Father', 'MeanHeight')
ax = mgdf.plot.scatter('Mother', 'MeanHeight')
# stronger correlations between parents and kids than between parents, Father-kid correlation
# (0.33) is stronger than Mother-kid correlation (0.26):
mgdf.corr()
