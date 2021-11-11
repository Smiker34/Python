import re

class NotIntError(Exception):
    pass


result = []
while True:
    elem = input("Введите число или 'stop' для завершения: ")

    if elem.lower() == "stop":
        print(result)
        break

    if re.search("\D", elem):
        try:
            raise NotIntError
        except NotIntError:
            print("Введено не число")
            
    else:
        result.append(int(elem))