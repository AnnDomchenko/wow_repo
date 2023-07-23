import json
import xml.dom.minidom
import xml.etree.ElementTree as ET

import xmltodict
from dict2xml import dict2xml

"""
Завдання XML:

    Завдання 1: Збереження словника у форматі XML: Конвертуйте словник у формат XML та збережіть його у файл з розширенням ".xml".
"""

cats = {
    'catlovers': True,
    'cat1': {
        'color': 'red',
        'age': 10,
        'food': {
            'dryfood': 'Brit',
            'wetfood': 'Sheba'
        }
    },
    'cat2': {
        'color': 'black',
        'age': 5,
        'food': {
            'dryfood': 'Whiskas',
            'wetfood': 'Kitikat',
            'water':{
                'milk': '10',
                'waterr':'15'
            }
        },
    'cat3': {
        'color': 'white',
        'age': 7,
        'food':{
            'dryfood':'Monge',
            'disease': 'kidneys'
        }
    },
    'mine':'Lopes'
    }
}

# xml_file=dict2xml(cats)
# print(xml_file)
#
# print(cats.keys())
# print(cats.values())
#
#
# def challenging_xml(our_filename, our_dict) -> None:
#     root = ET.Element('pets')
#     for key, value in our_dict.items():
#         pet = ET.SubElement(root, key)
#         for key1, value1 in our_dict.items():
#             if isinstance(value, dict):
#                 sub_element = ET.SubElement(pet, key1)
#                 for subkey, subvalue in value.items():
#                     sub_sub_element = ET.SubElement(sub_element, subkey)
#                     sub_sub_element.text = str(subvalue)
#             else:
#                 element = ET.SubElement(pet, key)
#                 element.text = str(value)
#     tree = ET.ElementTree(root)
#     tree.write(f'{our_filename}.xml')
#
#
# challenging_xml('filename_with_xml', cats)

"""
Завдання 2: Читання XML-файлу: Відкрийте XML-файл та розпарсіть його, щоб отримати дані зі словника у Python.
"""

# def xml_parser(ourfile:str) -> dict:
#     with open(ourfile) as ouf:
#         parsed=xmltodict.parse(ouf.read())
#         return parsed
#
# xml_parser('filename_with_xml.xml')
"""
Завдання JSON:

    Завдання 3: Збереження словника у форматі JSON: Конвертуйте словник у формат JSON та збережіть його у файл з розширенням ".json".
"""


def dict_into_json_func(json_file: str, data: dict):
    with open(f'{json_file}.json', 'w') as file:
        json.dump(data, file)


dict_into_json_func('kitties', data=cats)
"""   
    Завдання 4: Читання JSON-файлу: Відкрийте JSON-файл та завантажте його дані у Python як словник.
"""

def json_into_dict_func(file):
    with open(file) as dicti:
        print(json.load(dicti))

json_into_dict_func('kitties.json')
"""
Завдання XML та JSON:

    Завдання 5: Конвертація з XML до JSON: Завантажте XML-файл, розпарсіть його та конвертуйте у формат JSON. Потім збережіть словник у форматі JSON.
"""

def open_xml(file):
    with open(file) as f:
        parsed=xmltodict.parse(f.read())
        return parsed

def dict_to_json(file, data):
    with open(file, 'w') as file:
        json.dump(data, file)

a=open_xml('filename_with_xml.xml')
dict_to_json("fail.json", a)
