import re

mail = input("Введите e-mail: ")
result = {}
if re.search("[ ]", mail):
    raise ValueError("Неправильный e-mail: %s" % (mail))
result["username"] = re.search('[\w]+', mail).group()
try:
    result["domain"] = re.search('@[\D]+(?:(\.)[\D]+)', mail).group()
except AttributeError:
    raise ValueError("Неправильный e-mail: %s" % (mail))
print(result)