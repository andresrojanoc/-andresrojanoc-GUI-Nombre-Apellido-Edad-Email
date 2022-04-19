#! python3
import json

class TestingListKeys:

    def list_keys(self):
        view_lst = []
        for key, value in self.model.items():
            temp_key = key
            temp_value = value
            temp_keys = list(temp_value.keys())
            view_lst.append([(str(temp_keys[i])+": "+str(temp_value[temp_keys[i]]))  for i in range(len(temp_keys)) ])
        return view_lst

class TestingAddKeys:

    def add_keys(self, Nombre, Apellido, Edad, Email):
        self.model[Nombre] = {"Nombre": Nombre, "Apellido": Apellido, "Edad": Edad, "Email": Email}

        with open(json_file, 'w') as file:
            json.dump(self.model, file)

class TestingRemoveKeys:

    def remove_key(self, Nombre, Apellido, Edad, Email):
        deletion_key = None

        for key, value in self.model.items():
            temp_key = key
            if temp_key == Nombre:
                deletion_key = Nombre

        if deletion_key != None:
            del self.model[deletion_key]
            with open(json_file, 'w') as file:
                json.dump(self.model, file)

class TestingModifyKeys:

    def modify_key(self, Nombre, Apellido, Edad, Email):
        modification_key = None

        for key, value in self.model.items():
            temp_key = key
            if temp_key == Nombre:
                modification_key = Nombre

        if modification_key != None:
            self.model[modification_key] = {"Nombre": Nombre, "Apellido": Apellido, "Edad": Edad, "Email": Email}
            with open(json_file, 'w') as file:
                json.dump(self.model, file)


class Testing(TestingListKeys,TestingAddKeys,TestingRemoveKeys,TestingModifyKeys):

    def __init__(self,data_file):
        global json_file
        json_file=data_file
        try:
            with open(data_file) as file:
                self.model = json.load(file)
        except FileNotFoundError:
            self.model = dict()
