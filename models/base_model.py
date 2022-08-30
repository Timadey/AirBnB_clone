#!/usr/bin/python3
"""
The parent module
"""


from datetime import datetime


class BaseModel():
    """
    The parent class that all classes of AirBnB inherits\n
    It handles the initialization, serialization and
    deserialization of all instances

    Attributes:
        ``id (string)``: a ``uuid`` assigned when an instance
        is created that uniquely identifies an instance
        ``created_at (datetime)``: current datetime when an instance is created
        ``updated_at (datetime)``: current datetime when an instance is updated
    """

    def __init__(self):
        """
        Initializes the BaseModel
        """
        import uuid
        from datetime import datetime
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = self.created_at

    def __str__(self):
        return f"[BaseModel] ({self.id}) {self.__dict__}"

    def save(self):
        """Updates the public instance attribute ``updated_at``
        with the current datetime
        """
        self.updated_at = datetime.now()

    def to_dict(self):
        """
        Returns:
            A dictionary containing all keys/values of ``__dict__``
            of the instance

        Note:
            A key ``__class__`` is added to the dictionary with
            the class name of the object.
            The ``created_at`` and ``updated_at`` are converted
            to string object in ISO format ``%Y-%m-%dT%H:%M:%S.%f``
        """

        class_dict = self.__dict__
        class_dict['__class__'] = "BaseModel"
        class_dict['created_at'] = datetime.isoformat(
            class_dict['created_at'])
        class_dict['updated_at'] = datetime.isoformat(
            class_dict['updated_at'])
        return class_dict
