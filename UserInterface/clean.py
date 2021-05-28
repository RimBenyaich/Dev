'''
In this py file, we will be handling the missing values according to the user's choice
'''

import pandas as pd
from .datafr import readcsv
from .files import save_to_config_func

#So far, we only handled the drop case
def handlemiss(nums, categs, directory):
    df = readcsv(directory, 'none')
    for key in nums:
        if nums[key] == "Drop":
            df.dropna(axis = 0, how = 'any', inplace = True, subset = [key])
        elif nums[key] == 'Mean':
            df[key].fillna(df[key].mean(), inplace=True)
        elif nums[key] == 'Max':
            df[key].fillna(df[key].max(), inplace=True)
        else:
            df[key].fillna(df[key].min(), inplace=True)
    for key in categs:
        if categs[key] == "Drop":
            df.dropna(axis = 0, how = 'any', inplace = True, subset = [key])
        else:
            df = df.fillna(df[key].value_counts().index[0])
    return df
    