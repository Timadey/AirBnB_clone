"""
The user model
"""

from models.base_model import BaseModel


class User(BaseModel):
    """The user model. It inherits the Basemodel
    """
    email = ""
    password = ""
    first_name = ""
    last_name = ""
