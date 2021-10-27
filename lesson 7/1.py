import os

main_dir = os.getcwd()
project_name = "my_project"
dirs = ["settings", "mainapp", "adminapp", "authapp"]
while True:
    try:
        for dir in dirs:
            path = os.path.join(main_dir, project_name, dir)
            os.makedirs(path)
        break
    except FileExistsError:
        print("Проект с таким именем уже существуюет")
        project_name = input("Введите новое имя проекта или оставьте пустым для завершения: ")
        if project_name == '':
            exit()