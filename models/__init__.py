#!/usr/bin/python3
"""The initialization module"""

from models.engine.file_storage import FileStorage
storage = FileStorage()
storage.reload()
