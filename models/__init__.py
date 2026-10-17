#!/usr/bin/python3
"""Package initializer for models module."""
from models.engine.file_storage import FileStorage

storage = FileStorage()
storage.reload()