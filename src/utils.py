import json


def load():
    with open(r'C:\Users\User\Desktop\PyCharm_Projects\Term_4\13_1\Examples\data\data.json',
              'r', encoding='utf8') as file:
        print(file)
        operations = json.load(file)
        return operations


print(load)
