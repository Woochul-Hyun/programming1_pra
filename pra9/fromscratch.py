import os, shutil

print("Current Directory: ", os.getcwd())
os.chdir('FilesToSort')

for file in os.listdir('.'):
    file_name, file_extension = os.path.splitext(file)
    extension = file_extension.replace(".", "")
    print(extension)
    os.mkdir(extension)

os.mkdir('doc')
