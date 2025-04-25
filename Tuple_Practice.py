# %% [markdown]
# ### Tuple Review ###

# %%
t = ()
t

# %%
len(t)

# %%
t1 = (10, 20, 30, 40, 50) # tuple
t1

# %%
t2 = ('a', 'z', 'm', 'n') # tuple
t2

# %%
t2.count('z') # count the number of occurrences of 'z' in t2

# %%
t2.index('a') # find the index of 'a' in t2

# %%
t1

# %%
t1[0] # access the first element of t1

# %%
t1[0:3] # access the first three elements of t1

# %%
t1[0] =100 # tuples are immutable, so this will raise an error

# %%
t1 

# %%
icic = (1234, '4th apr 1990', 1234, 'cizp346878')
icic

# %%
icic[0] =  980 # tuples are immutable, so this will raise an error
# Tuple formats are used in many places, such as in banking, insurance, and other industries
# to store customer information, transaction details, etc.
# where the data is not expected to change frequently like client information, transaction history, etc.

# %%
t1

# %%
t3 = t1 * 3 # repeat the tuple t1 three times
t3
# t3 is a new tuple that contains the elements of t1 repeated three times
# This is useful when you want to create a larger tuple with the same elements
# for example, if you want to create a tuple with the same values for testing or demonstration purposes
# or if you want to create a tuple with the same values for a specific purpose
# like creating a tuple with the same values for a specific calculation or operation



# %% [markdown]
# ##### Tuple is completed ####

# %% [markdown]
# 


