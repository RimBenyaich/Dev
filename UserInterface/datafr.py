'''
This py file will have all the functions related to the pandas' dataframe
'''
import pandas as pd
import os
from .files import get_data
from .files import save_to_config_func

# this function will read our csv from the given directory
# TODO : use optional args
def readcsv(directory, f):
    if f == 'none':
        for filename in os.listdir(directory):
            if filename.endswith('.csv'):
                df = pd.read_csv(directory + '/' + filename)
                return df
        return None
    else:
        d = directory + '/' + f
        df = pd.read_csv(d)
        return df


# this function will save the categories of our dataset in our config file as well
def get_columns(conf):
    directory = './' + get_data("project name", conf)
    df = readcsv(directory, 'none')
    lst = [col for col in df]
    save_to_config_func(lst, "categories", conf)

    return lst


# this function will get our columns from our df
def getcols(df):
    return list(df.columns)


def get_mod(pref):
    models = {
        1: "CNN",
        2: "ANN",
        3: "Linear Regression",
        4: "Logistric Regression",
    }
    mod = models[pref]


def dropcols(items, df):
    for it in items:
        df.drop(it, axis=1, inplace=True)

    return df


def getdt(df):
    return [type(df[col][1]) for col in df.columns]


def colcnt(df):
    return len(df.columns)


def determine(y):
    s = set(range(1, len(y)))
    return "Regression" if (len(s) / len(y)) > 0.9 else "Classification"
