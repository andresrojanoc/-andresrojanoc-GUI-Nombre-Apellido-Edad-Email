#! python3
import unittest
import json
from back import Testing
from back import TestingListKeys
from back import TestingAddKeys
from back import TestingRemoveKeys
from back import TestingModifyKeys

class TestTesting(unittest.TestCase):

    def setUp(self):
        print('setUp')
        self.data = Testing("no.json")

    def test_list_keys(self):
        self.data.model.clear()
        self.data.model["A"] = {"Nombre": "A", "Apellido": "A2", "Edad": "1", "Email": "a@correo.com"}
        self.data.model["B"] = {"Nombre": "B", "Apellido": "B2", "Edad": "2", "Email": "b@correo.com"}
        self.data.model["C"] = {"Nombre": "C", "Apellido": "C2", "Edad": "3", "Email": "c@correo.com"}
        entry_list = TestingListKeys.list_keys(self.data)
        test_dictionary2 = dict()
        test_dictionary2["A"] = {"Nombre": "A", "Apellido": "A2", "Edad": "1", "Email": "a@correo.com"}
        test_dictionary2["B"] = {"Nombre": "B", "Apellido": "B2", "Edad": "2", "Email": "b@correo.com"}
        test_dictionary2["C"] = {"Nombre": "C", "Apellido": "C2", "Edad": "3", "Email": "c@correo.com"}
        view_lst = []
        for row in entry_list:
            entry = [row[0][8:],row[1][10:],row[2][6:],row[3][7:]]
            view_lst.append(entry)
        A_entry = [self.data.model["A"]["Nombre"], self.data.model["A"]["Apellido"], self.data.model["A"]["Edad"], self.data.model["A"]["Email"]]
        B_entry = [self.data.model["B"]["Nombre"], self.data.model["B"]["Apellido"], self.data.model["B"]["Edad"], self.data.model["B"]["Email"]]
        C_entry = [self.data.model["C"]["Nombre"], self.data.model["C"]["Apellido"], self.data.model["C"]["Edad"], self.data.model["C"]["Email"]]
        view_lst2 = [A_entry,B_entry,C_entry]
        self.assertEqual(view_lst[0],view_lst2[0])


    def test_add_keys(self):
        TestingAddKeys.add_keys(self.data,"A","B","1","a@correo.com")
        model = dict()
        model["A"] = {"Nombre": "A", "Apellido": "B", "Edad": "1", "Email": "a@correo.com"}
        self.assertEqual(self.data.model,model)


    def test_remove_key(self):
        self.data.model.clear()
        self.data.model["A"] = {"Nombre": "A", "Apellido": "B", "Edad": "1", "Email": "a@correo.com"}
        TestingRemoveKeys.remove_key(self.data,"A","B","1","a@correo.com")
        self.assertEqual(bool(self.data.model),False)
        self.data.model.clear()
        self.data.model["A"] = {"Nombre": "A", "Apellido": "B", "Edad": "1", "Email": "a@correo.com"}
        self.data.model["C"] = {"Nombre": "C", "Apellido": "D", "Edad": "2", "Email": "c@correo.com"}
        TestingRemoveKeys.remove_key(self.data,"A","B","1","a@correo.com")
        self.assertEqual(bool(("A" in self.data.model)),False)

    def test_modify_key(self):
        self.data.model.clear()
        self.data.model["A"] = {"Nombre": "A", "Apellido": "B", "Edad": "1", "Email": "a@correo.com"}
        self.data.model["C"] = {"Nombre": "C", "Apellido": "D", "Edad": "2", "Email": "c@correo.com"}
        TestingModifyKeys.modify_key(self.data,"C","random1","3","random_c@correo.com")
        test_dictionary = dict()
        test_dictionary["C"] = {"Nombre": "C", "Apellido": "random1", "Edad": "3", "Email": "random_c@correo.com"}
        self.assertEqual(self.data.model["C"],test_dictionary["C"])
        test_dictionary["A"] = {"Nombre": "A", "Apellido": "random2", "Edad": "4", "Email": "random_a@correo.com"}
        self.assertNotEqual(self.data.model["A"],test_dictionary["A"])
        TestingModifyKeys.modify_key(self.data,"A","random2","4","random_a@correo.com")
        self.assertEqual(self.data.model["A"],test_dictionary["A"])

if __name__ == '__main__':
    unittest.main(verbosity=2)
    unittest.main()
