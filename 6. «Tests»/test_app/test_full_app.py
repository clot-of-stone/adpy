import json
from io import StringIO
from pathlib import Path
from unittest import main, TestCase
from unittest.mock import Mock, patch

import app
from app import (directories,
                 documents,
                 get_doc_owner_name,
                 check_document_existence,
                 get_all_doc_owners_names,
                 show_all_docs_info,
                 remove_doc_from_shelf,
                 show_document_info,
                 add_new_shelf,
                 append_doc_to_shelf,
                 add_new_doc,
                 delete_doc,
                 get_doc_shelf,
                 move_doc_to_shelf
                 )


def overwrite_data():
    shelves = f'{Path().absolute()}\\fixtures\\dirs.json'
    catalog = f'{Path().absolute()}\\fixtures\\docs.json'
    with open(shelves, 'r', encoding='utf-8') as dirs:
        directories = json.load(dirs)
    with open(catalog, 'r', encoding='utf-8') as docs:
        documents = json.load(docs)
    return documents, directories


class TestFunction(TestCase):

    def test_check_document_existence(self):
        is_there = 1
        is_not_there = 0
        self.assertEqual(is_there, check_document_existence('11-2'))
        self.assertEqual(is_not_there, check_document_existence(''))

    @patch('builtins.input', side_effect=[
        '2207 876234',
        '10006',
        '5455 028765',
        'qwerty'
    ])
    def test_get_doc_owner_name(self, mock_input_get_doc_owner_name):
        self.assertEqual('Василий Гупкин', get_doc_owner_name())
        self.assertEqual('Аристарх Павлов', get_doc_owner_name())
        self.assertEqual(None, get_doc_owner_name())
        self.assertEqual(None, get_doc_owner_name())

    def test_get_all_doc_owners_names(self):
        reference = {'Аристарх Павлов', 'Геннадий Покемонов', 'Василий Гупкин'}
        result = get_all_doc_owners_names()
        self.assertEqual(reference, result)

    def test_remove_doc_from_shelf(self):
        remove_doc_from_shelf('10006')
        remove_doc_from_shelf('11-2')
        self.assertNotIn('10006', directories)
        self.assertNotIn('11-2', directories)
        self.assertIsNone(remove_doc_from_shelf('test_doc'))

    @patch('builtins.input', side_effect=['2', '5'])
    def test_add_new_shelf(self, mock_input_add_new_shelf):
        result_if_is_there = add_new_shelf()
        result_if_is_not_there = add_new_shelf()
        add_new_shelf('13')
        self.assertTrue(result_if_is_there == ('2', False))
        self.assertTrue(result_if_is_not_there == ('5', True))
        self.assertIn('13', directories)

    def test_append_doc_to_shelf(self):
        append_doc_to_shelf('1', '1')
        append_doc_to_shelf('Ex', '2')
        append_doc_to_shelf('333', '3')
        append_doc_to_shelf('P4SS', '4')
        self.assertIn('1', directories['1'])
        self.assertIn('Ex', directories['2'])
        self.assertIn('333', directories['3'])
        self.assertIn('P4SS', directories['4'])
        app.documents, app.directories = overwrite_data()

    @patch('builtins.input', side_effect=['2207 876234', '10006', 'DELIVER'])
    def test_delete_doc(self, mock_input_delete_doc):
        result_1 = delete_doc()
        result_2 = delete_doc()
        result_3 = delete_doc()
        self.assertEqual(('2207 876234', True), result_1)
        self.assertEqual(('10006', True), result_2)
        self.assertEqual(None, result_3)
        app.documents, app.directories = overwrite_data()

    @patch('builtins.input', side_effect=['11-2', 'DELIVER'])
    def test_get_doc_shelf(self, mock_input_get_doc_shelf):
        shelf_number_returned = get_doc_shelf()
        self.assertIn('11-2', directories[str(shelf_number_returned)])
        result_if_not_there = get_doc_shelf()
        self.assertIsNone(result_if_not_there)

    def test_move_doc_to_shelf(self):
        """\nВНИМАНИЕ!!!
        Вторая часть данного теста проваливается,
        поскольку обнаружена недоработка в тестируемой программе -
        эта функция не должна создавать новый документ в директории,
        она должна только переместить существующий документ. В противном же
        случае при вводе номера несуществующего документа предпочтительнее
        было бы увидеть соответствующее сообщение."""
        print(self.test_move_doc_to_shelf.__doc__)
        with patch('builtins.input', new=Mock(side_effect=['11-2', '3'])):
            move_doc_to_shelf()
            self.assertIn('11-2', app.directories['3'])
        with patch('builtins.input', new=Mock(side_effect=['test_doc',
                                                           'test_shelf'])):
            move_doc_to_shelf()
            self.assertNotIn('test_doc', app.directories['test_shelf'])

    def test_show_document_info(self):
        doc = {
            'type': 'test_type',
            'number': 'test_number',
            'name': 'test_name'
        }
        with patch('sys.stdout', new=StringIO()) as line:
            show_document_info(doc)
            reference = 'test_type "test_number" "test_name"'
            self.assertEqual(reference, line.getvalue().strip())

    def test_show_all_docs_info(self):
        reference = f'Список всех документов:\n\npassport "2207 876234" ' \
                    f'"Василий Гупкин"\ninvoice "11-2" "Геннадий ' \
                    f'Покемонов"\ninsurance "10006" "Аристарх Павлов"'
        with patch('sys.stdout', new=StringIO()) as lines:
            show_all_docs_info()
            self.assertEqual(reference, lines.getvalue().strip())

    def test_add_new_doc(self):
        with patch('builtins.input', new=Mock(side_effect=[
            'test_number',
            'test_type',
            'test_owner',
            'test_shelf'
        ])):
            doc = {
                "type": 'test_type',
                "number": 'test_number',
                "name": 'test_owner'
            }
            reference = 'test_shelf'
            res = add_new_doc()
            self.assertEqual(reference, res)
            self.assertIn(doc, documents)
            self.assertIn('test_number', directories[reference])


if __name__ == '__main__':
    main()
