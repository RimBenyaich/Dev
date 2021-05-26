'''
This file has a function that will generate the df form and another one for saving it in 
the desired directory
'''

import os

#This form will serve to generate the form to drop features
def generateform(arr, target):
    out = 'class DropFeat(forms.Form):\n'
    for key, value in arr.items():
        if(key != target):
            out += '\t%s = forms.BooleanField(required = False, label=\"%s - %.4f\",initial = False)\n' % (key, key, value)
            # , label = \"%.4f\" , value
    return out

#This form will serve to handle missing values depending on their datatype
def gencleanform(arr, dts):
    out = 'class DropFeat(forms.Form):\n'
    for key, value in arr.items():
        out += '\t%s = forms.BooleanField(required = False, label=\"%s - %.4f\",initial = False)\n' % (key, key, value)

#this function will save our form with the others
def genere(func):
    os.chdir("./UserInterface")
    f = open("views.py","a")
    f.write("\n")
    # f.write("from djongo import models\n\n")
    f.write(func)
    f.close()

