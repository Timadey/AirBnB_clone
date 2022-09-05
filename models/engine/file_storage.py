#!/usr/bin/python3
"""This modeule defines that file storage class"""


import json


class FileStorage:
    """The ``FileStorage`` class serializes instances to a JSON
    file and deserializes JSON file to instances.
    It helps to store object in json formats in a file.
    """
    __objects = {}
    __file_path = "objects.json"

    @property
    def file_path(self):
        """
        file_path (string): path to the JSON file. Default is ``objects.json``
        at root directory

        Raises:
            TypeError: if the file_path is not of type string
        """
        return self.__file_path

    @file_path.setter
    def file_path(self, value):
        if not type(value) == str:
            raise TypeError("File path can only be a string")
        self.__file_path = value

    @property
    def objects(self):
        """
        objects (dictionary): Stores all object with ``<class name>.id``
        as key

        Raises:
            TypeError: if the value to set is not a dictionary

        Example:
            BaseModel object with id=1212122, the key will be
            BaseModel.1212121212
        """
        return self.__objects

    @objects.setter
    def objects(self, value):
        if not type(value) == dict:
            raise TypeError("Value of object can only be of type dict")
        self.__objects = value

    def all(self):
        """Returns all objects in a file JSON"""
        return self.__objects

    def new(self, obj):
        """Add the ``obj`` to the __object dictionary with key
        ``<obj class name>.id``

        Args:obj (dict): dictionary containing attributes of objects to create

        Raises:TypeError: if ``obj`` is not a dictionary
        """
        # if not type(obj) == dict:
        #     raise TypeError("Arg obj can only be of type dict")
        class_name = obj.get('__class__')
        id = obj.get('id')
        key = class_name + '.' + id
        self.__objects[key] = obj

    def save(self):
        """Serializes objects in the filestorage to the JSON file"""
        with open(self.__file_path, mode="w", encoding="utf-8") as file:
            json.dump(self.__objects, file, indent="\t")
        return "OK"

    def reload(self):
        """Deserializes the JSON file to filestorage if the file_path exists
            The deserialized objects are stored in __objects of filestorage
        """
        try:
            with open(self.__file_path, mode='r',
                      encoding="utf-8") as json_file:
                self.__objects = json.load(json_file)
        except OSError:
            pass
