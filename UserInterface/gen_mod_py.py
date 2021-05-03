'''
this python file will handle everything that has do to with generating the models.py file and
filling it with the right models
'''
from djongo import models
import os

#this function will create the models.py and fill it with the right model for our df
def generate(func):
    os.chdir("./UserInterface")
    f = open("models.py","a")
    f.write("\n")
    # f.write("from djongo import models\n\n")
    f.write(func)
    f.close()
