'''
This file has a function that will generate the df form and another one for saving it in 
the desired directory
'''

import os

#This form will serve to generate the form to drop features
def generateform(arr, target):
    out = 'class DropFeat(forms.Form):\n'
    for key, value in arr.items():
        if key != target:
            out += '\t%s = forms.BooleanField(required = False, label=\"%s - %.4f\",initial = False)\n' % (key, key, value)
            # , label = \"%.4f\" , value
    return out

#This form will serve to handle missing values depending on their datatype
def gencleanform(arr, dts):
    flagn = 0
    flags = 0
    cn = '\tCHOICES1 = [(1,\'Drop\'),(2,\'Mean\'),(3,\'Max\'),(4,\'Min\')]\n'
    cs = '\tCHOICES2 = [(1,\'Drop\'),(2,\'Mode\'),(3,\'Most\'),(4,\'Least\')]\n'
    out = 'class CheckForm(forms.Form):\n'
    for key, value in arr.items():
        if value > 0:
            if dts[key] in ["float64", "int64"]:
                if flagn == 0:
                    flagn = 1
                    out += cn
                out += '\t%s = forms.ChoiceField(label = \'%s has %d missing values\', widget=forms.RadioSelect, choices=CHOICES1)\n' %(key, key, value)
            elif dts[key] == "str":
                if flags == 0:
                    flags = 1
                    out += cs
                out += '\t%s = forms.ChoiceField(label = \'%s has %d missing values\', widget=forms.RadioSelect, choices=CHOICES2)\n' %(key, key, value)

    # out += '\tnametar = forms.CharField(label = \'Please indicate the name of the prediction\')\n'
    return out

#this function will save our form with the others
def genere(func):
    os.chdir("./UserInterface")
    with open("forms.py","a") as f:
        f.write("\n")
        f.write(func)

