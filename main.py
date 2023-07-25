
documents = [
    {"type": "passport", "number": "2207 876234", "name": "Василий Гупкин"},
    {"type": "invoice", "number": "11-2", "name": "Геннадий Покемонов"},
    {"type": "insurance", "number": "10006", "name": "Аристарх Павлов"}
]
directories = {
    '1': ['2207 876234', '11-2'],
    '2': ['10006'],
    '3': []
}
def get_name_piople(doc_f):
    rez = "Человек с указанным номера документа не найден"
    for doc in documents:
        if doc_f == doc['number']:
            # rez = f'Документ выдан на имя: {doc["name"]}'
            rez = doc["name"]
            break
    return rez

def get_num_shelf(docf):
    rez = "Человек с указанным номера документа не найден"
    for indx, item_doc in directories.items():
        if docf in item_doc:
            rez = f'Полка номер {indx}'
    return rez

def print_list_doc():
    for doc in documents:
        print(f'passport "{doc["number"]}" "{doc["name"]}"')
    return ''


def add_doc(num, type_d, name, num_shelf):

    if num_shelf not in directories.keys():
        print("Вы указали не существующую полку")
    else:
        documents.append({"type": type_d, "number": num, "name": name})
        directories[num_shelf].append(num)
    return

# Задание №2
def delete_doc():
    num = input('Укажите номер документа: ')
    for doc in documents:
        if num == doc['number']:
            del doc['number']
            break
    for indx, num_doc in directories.items():
        if num in num_doc:
            del directories[indx]
            return
    print("Нет такого документа")
    return ''


def move_doc():
    num_doc = input('Укажите номер документа: ')
    num_shelf = input('Укажите номер полки: ')
    if num_shelf not in directories.keys():
        return print('Вы указали не существующую полку')
    for indx, doc_it in directories.items():
        if num_doc in doc_it:
            doc_it.remove(num_doc)
            directories[num_shelf].append(num_doc)
            print('Документ перенесен на новую полку')
            return
    print('Вы указали не существующий номер документа')
    return ''


def add_shelf():
    num_shelf = input('Укажите номер полки: ')
    if str(num_shelf) in directories.keys():
        print('Такая полка уже существует!')
        return ''
    directories[str(num_shelf)] = []


def main():
    while True:
        command = input().lower()
        if command == "p":
            doc_f = input('Укажите номер документа: ')
            print(get_name_piople(doc_f))
        elif command == "s":
            docf = input('Укажите номер документа: ')
            print(get_num_shelf(docf))
        elif command == "l":
            print_list_doc()
        elif command == "a":
            num = input('Укажите номер документа: ')
            type_d = input('Укажите тип документа: ')
            name = input('Укажите имя клиента: ')
            num_shelf = input('Укажите номер полки: ')
            add_doc(num,type_d,name,num_shelf)
        elif command == "d":
            delete_doc()
        elif command == "m":
            move_doc()
        elif command == "as":
            add_shelf()

        elif command == "q":
            print('Goodbye')
            break
        else:
            print("Неверно введена команда. Попробуйте еще раз!")



# main()