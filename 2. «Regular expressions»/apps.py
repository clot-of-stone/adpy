import re
import csv
from pprint import pprint
# читаем адресную книгу в формате CSV в список contacts_list


with open("phonebook_raw.csv", encoding='utf-8') as f:
    rows = csv.reader(f, delimiter=",")
    contacts_list = list(rows)


# TODO 1: выполните пункты 1-3 ДЗ
# ваш код
def order(database):
    names_ordered = [database[0]]
    for item in database[1:]:
        if item[0].count(' ') == 1:
            full_name = item[0].split()
            item[0], item[1] = full_name[0], full_name[1]
            names_ordered.append(item)
        elif item[1].count(' ') == 1:
            full_name = item[1].split()
            item[1], item[2] = full_name[0], full_name[1]
            names_ordered.append(item)
        elif item[0].count(' ') == 2:
            full_name = item[0].split()
            item[0], item[1], item[2] = full_name[0], full_name[1], full_name[2]
            names_ordered.append(item)
    return names_ordered


def regulate_phones():
    pattern = r"(\+7|8)\s*\(?(\d{3})\)? ?-?(\d{3})-?(\d{2})-?(\d{2}) ?\(?(доб.)?\s*((\d+))?\)?"
    phone_sub = r"+7(\2)\3-\4-\5"
    phone_sub_add = r"+7(\2)\3-\4-\5 доб.\8"
    phone_list = order(contacts_list)
    for item in phone_list:
        for phone in item:
            if re.findall(pattern, phone):
                if 'доб.' in phone:
                    number = re.sub(pattern, phone_sub_add, phone)
                    index = item.index(phone)
                    item[index] = number
                else:
                    corr_number = re.sub(pattern, phone_sub, phone)
                    index = item.index(phone)
                    item[index] = corr_number
    return phone_list


def merge_duplicates():
    final_list = regulate_phones()
    result_list = []
    draft_list = []
    for item in final_list:
        if [item[0], item[1]] not in draft_list:
            draft_list.append([item[0], item[1]])
            result_list.append(item)
        else:
            index = draft_list.index([item[0], item[1]])
            result_list[index].extend(item)
            roam = []
            for unit in result_list[index]:
                if unit not in roam:
                    roam.append(unit)
            result_list[index] = roam
    return result_list


# # TODO 2: сохраните получившиеся данные в другой файл
# код для записи файла в формате CSV
def run():
    with open("phonebook.csv", "w", encoding='utf-8') as file:
        datawriter = csv.writer(file, delimiter=',')
        # Вместо contacts_list подставьте свой список
        datawriter.writerows(merge_duplicates())
        print('Файл \'phonebook.csv\' записан!')
