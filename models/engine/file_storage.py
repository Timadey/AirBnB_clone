"""This modeule defines that file storage class"""


class FileStorage:
    """The ``FileStorage`` class serializes instances to a JSON
    file and deserializes JSON file to instances.
    It helps to store object in json formats in a file.
    """

    @property
    def file_path(self):
        """
        file_path (string): path to the JSON file for example file.json

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
        objects (dictionary): Stores all object by ``<class name>.id

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
        """
        class_name = obj['__class__']
        id = obj['id']
        key = class_name + '.' + id
        self.__objects['key'] = obj

    def save(self):
        """Serializes objects in the class to the JSON file"""
        pass
