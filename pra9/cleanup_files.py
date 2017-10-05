import os, shutil
from re import findall

__author__ = 'Lindsay Ward'

print("Current directory is", os.getcwd())

os.chdir('Lyrics')

def normal_formatting(string):
    return string.replace(" ", "_")


def no_space_formatting(string):
    formatted = None
    for each in findall('[A-Z][^A-Z]', string.split('.')[0]):
        if not formatted:
            formatted = each
        else:
            formatted += "_" + each
    return formatted


def get_dirs():
    dirs = []
    for name in os.listdir('.'):
        if os.path.isdir(name):
            dirs.append(name)
    return dirs

dirs = get_dirs()

for dir in dirs:
    for filename in os.listdir('./' + dir):
        filename = str(filename.split('.')[0])
        if not os.path.isdir(filename) and not "None":
            if filename.islower():
                pass
            elif " " in filename:
                filename = normal_formatting(filename)
            else:
                filename = no_space_formatting(filename)
            filename.title()
            filename += ".txt"
            print(filename)
