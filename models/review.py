"""
The review model
"""

from models.base_model import BaseModel


class Review(BaseModel):
    """The review model. It inherits the Basemodel
    """
    place_id = ""
    user_id = ""
    text = ""
