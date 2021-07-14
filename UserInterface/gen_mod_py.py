'''
this python file will handle everything that has do to with generating the models.py file and
filling it with the right models
'''
import os

#this function will create the models.py and fill it with the right model for our df
def generate(func):
    os.chdir("./UserInterface")
    with open("models.py","a") as f:
        f.write("\n")
        f.write(func)
