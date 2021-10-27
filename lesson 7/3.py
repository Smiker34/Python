import os, shutil
def sort_file(dict):
   for pair in dict.items():
       try:
           os.mkdir(pair[0])
       except FileExistsError:
           pass
       os.chdir(pair[0])
       for file in pair[1]:
            if isinstance(file,str):
                create = open(file, "w")
                create.close()
            else:
                sort_file(file)
       os.chdir("..")


main_dir = os.getcwd()
project_name = "my_project"
dirs_files = {
"settings":
    [
        "__init__.py",
        "dev.py",
        "prod.py"
    ],
"mainapp":
    [
        "__init__.py",
        "models.py",
        "views.py",
        {"templates":
             [{"mainapp":
                 [
                    "base.html",
                    "index.html"
                 ]
             }]

        }
    ],
"authapp":
    [
        "__init__.py",
        "models.py",
        "views.py",
        {"templates":
             [{"authapp":
                  [
                      "base.html",
                      "index.html"
                  ]
             }]

        }
    ]
}


path = os.path.join(main_dir,project_name)
try:
    os.makedirs(path)
except FileExistsError:
    pass

os.chdir(path)
sort_file(dirs_files)
os.chdir("..")

temp_path = os.path.join(path,"templates")
try:
    os.makedirs(temp_path)
except FileExistsError:
    pass
for i in os.walk(path):
    ind = i[0].find('templates')
    if ind != -1:
        if i[0][ind + 10:] != "":
            try:
                shutil.move(i[0],temp_path)
                os.rmdir(i[0][:ind+10])
            except shutil.Error:
                pass