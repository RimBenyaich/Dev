'''
This py file will have all the functions related to the pandas' dataframe
'''
import pandas as pd
import os
from .files import get_data, save_to_config_func

def readcsv(directory, f=None):
    """read a csv from the given directory, if filename not given it will look for .csv files in the directory"""
    if f:
        d = directory + '/' + f
        df = pd.read_csv(d)
        return df
    else:
        for filename in os.listdir(directory):
            if filename.endswith('.csv'):
                df = pd.read_csv(directory + '/' + filename)
                return df
        return None


# this function will save the categories of our dataset in our config file as well
def get_columns(conf):
    directory = './' + get_data("project name", conf)
    df = readcsv(directory)
    lst = [col for col in df]
    save_to_config_func(lst, "categories", conf)

    return lst


# this function will get our columns from our df
def getcols(df):
    return list(df.columns)



def dropcols(items, df):
    for it in items:
        df.drop(it, axis=1, inplace=True)

    return df


def colcnt(df):
    return len(df.columns)


def determine(y):
    s = set(range(1, len(y)))
    return "Regression" if (len(s) / len(y)) > 0.9 else "Classification"
