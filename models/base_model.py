#!/usr/bin/python3
'''
base_model.py
'''

from datetime import datetime
import uuid

import models


class BaseModel:
    def __init__(self, **kwargs):
        if kwargs:
            for key in kwargs.keys():
                if key != "__class__":
                    if key not in ["created_at", "updated_at"]:
                        self.__setattr__(key, kwargs[key])
                    else:
                        self.__setattr__(key, datetime.fromisoformat(kwargs[key]))

        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)

    def __str__(self):
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        to_dict = self.__dict__
        to_dict["__class__"] = self.__class__.__name__
        to_dict['created_at'] = self.created_at.strftime("%Y-%m-%dT%H:%M:%S.%f")
        to_dict['updated_at'] = self.updated_at.strftime("%Y-%m-%dT%H:%M:%S.%f")

        return to_dict
