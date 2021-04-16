import pandas as pd
from .datafr import readcsv
from .files import save_to_config_func

def handlemiss(choice, directory):
    df = readcsv(directory)

    if(choice == "drop"):
        df.dropna(axis = 0, how='any', inplace = True)

        return df