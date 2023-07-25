import pytest
from main import documents, directories, get_name_piople, get_num_shelf, add_doc
from API_Ya import YaUploader as api_ya
# Задача №1 unit-tests
@pytest.mark.parametrize("doc_num", ["2207 876234", "11-2","10006"])
def test_get_name_piople(doc_num):
    list_doc = []
    for it in documents:
        list_doc.append(it['number'])
        if doc_num in it.values():
            assert get_name_piople(doc_num) == it['name']
            return
    # assert doc_num in list_doc, "Человек с указанным номера документа не найден"

@pytest.mark.parametrize("doc_num", ["2207 876234", "11-2","10002"])
def test_get_num_shelf(doc_num):
    list_doc = []
    for num_shelf, it in directories.items():
        list_doc.append(it)
        if doc_num in it:
            assert get_num_shelf(doc_num) == f'Полка номер {num_shelf}'
            return
    # assert doc_num in list_doc, "Человек с указанным номера документа не найден"

@pytest.mark.parametrize(
    "num, type_d, name, num_shelf", [
        ("7878 876234", "passport", "Гадя Петрович", "3"),
        ("1111 232323", "passport", "Петя Петрович", "2")
    ]
)
def test_add_doc(num, type_d, name, num_shelf):
    check_documents_dict = {"type": type_d, "number": num, "name": name}
    add_doc(num, type_d, name, num_shelf)
    assert check_documents_dict in documents and num in directories[num_shelf]

# Задача №2 Автотест API Яндекса
def test_api_ya_not_success():
    obj_ya = api_ya('1') # указываем токен ya
    assert obj_ya.upload('test') != 201

def test_api_ya_success():
    obj_ya = api_ya('1') # указываем токен ya
    assert obj_ya.upload('test') == 201 or obj_ya.upload('test') == 409, "ошибка создания директории"