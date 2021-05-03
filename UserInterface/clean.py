'''
In this py file, we will be handling the missing values according to the user's choice
'''

import pandas as pd
from .datafr import readcsv
from .files import save_to_config_func

#So far, we only handled the drop case
def handlemiss(choice, directory):
    df = readcsv(directory)
    if(choice == "drop"):
        df.dropna(axis = 0, how='any', inplace = True)
        return df


#TODO Handle the other cases (Mean, min, max) with categorical values and for every categegory