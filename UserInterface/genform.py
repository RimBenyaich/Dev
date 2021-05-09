import os

def generateform(arr, target):
    out = 'class DropFeat(forms.Form):\n'
    for key, value in arr.items():
        if(key != target):
            out += '\t%s = forms.BooleanField(required = False, label = \"%.4f\")\n' % (key, value)

    return out

#this function will create the models.py and fill it with the right model for our df
def genere(func):
    os.chdir("./UserInterface")
    f = open("forms.py","a")
    f.write("\n")
    # f.write("from djongo import models\n\n")
    f.write(func)
    f.close()
