'''
This file will be handling all operations about naming our main folder of data, and our
json file. It will also do all the saving and retrieving from the config file 
'''

import os
import datetime
import json
import pandas as pd
from pathlib import Path
import shutil

# this function will rename our csv file


def renaming(directory, ext):
    path, dirs, files = next(os.walk(directory))
    Current_Date = datetime.datetime.today().strftime('%d_%b_%Y_%H_%M_%S')
    # print(len(files))
    for file in os.listdir(directory):
        if(file.endswith(ext)):
            src = (directory + "/" + file)
            name = file.split('.')[0]
            dst = (directory + "/" + name + '_' + Current_Date + ext)
            os.rename(src, dst)

    return len(files)

# this function will save all of the form data to our config file


def save_to_config_form(request, form, conf):
    curr = os.getcwd() + "/downloadable/"
    f = open(curr + conf, 'r+')
    js = json.load(f)

    for key, value in form.cleaned_data.items():
        if value.isnumeric():
            value = int(value)
            if key == "choice":
                choices = {
                    1: "One CSV",
                    2: "Multiple CSVs",
                    3: "One Json",
                    4: "Multiple Jsons",
                    5: "Images with their CSV",
                    6: "Images with their Json",
                    7: "Images with their txt",
                    8: "Images with their XML"
                }
                js["format"] = choices[value]
            elif key == "referred":
                referred = {
                    1: "CNN",
                    2: "ANN",
                    3: "Linear Regression",
                    4: "Logistic Regression",
                    5: "Any"
                }
                js["preferred model"] = referred[value]
            elif key == "probtype":
                js["problem type"] = "Regression" if value == 1 else "Classification"
        elif key == "project_name":
            js["project name"] = value
        else:
            js[key] = value

    data = json.dumps(js, indent=4)

    with open(curr + conf, 'w') as outfile:
        outfile.write(data)


# this function will save to our config file everything calculated (file cnt, lines cnt, etc..)
def save_to_config_func(data, categ, conf):
    curr = os.getcwd() + "/downloadable/"
    # print(curr)
    f = open(curr + conf)
    dt = json.load(f)
    dt[categ] = data

    with open(curr + conf, 'w') as fp:
        json.dump(dt, fp)
    # print(categ)


# this function will get us the actual saved value within a specific item of the config
def get_data(categ, conf):
    curr = os.getcwd() + "/downloadable/"
    # print(curr)
    f = open(curr + conf)
    dt = json.load(f)

    return dt[categ]


# this function will serve to rename our config file for a certain user in a certain format
def rename_conf(directory, conf, name):
    current_Date = datetime.datetime.today().strftime('%d_%b_%Y_%H_%M_%S')
    conf = conf + name
    conf = conf + '_' + current_Date + '.json'
    return conf


# this function will initialize our configuration file by loading in it our template
def init_conf(conf):
    # print(os.getcwd())
    f = open('template.json',)
    curr = os.getcwd() + "/downloadable/"
    # print(curr)
    js = json.load(f)

    with open(curr + conf, 'w') as fp:
        json.dump(js, fp)


# this function will return our config file name
def get_config(directory):
    for file in os.listdir(directory):
        if file.endswith('.json') and not file.endswith('template.json'):
            return file



# this function will delete the config file after the user downloads it and exits the website
def delete(directory, conf):
    p = Path(directory)
    name = get_data("project name", conf)
    for file in os.listdir(directory):
        if file == name:
            q = p / file
            shutil.rmtree(q)
        if file.endswith('.json') and not file.endswith('template.json'):
            os.remove(file)



# gets the csv path by taking its name from our config file
def get_csvpath(directory, conf):
    name = get_data("project name", conf)



# cleans our downloadable folder once it reaches the end of the plateform
def cleanfiles(directory):
    p = Path(directory)
    for file in os.listdir(directory):
        os.remove(file)

# def getdtdic(value):
# 	l = len(value)
# 	return value[2:l - 3]
