#!/usr/bin/python3
"""Defines the FileStorage class."""
import json
import os


class FileStorage:
    """Serializes instances to JSON and deserializes JSON to instances."""

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Return the dictionary __objects."""
        return FileStorage.__objects

    def new(self, obj):
        """Set in __objects the obj with key <obj class name>.id."""
        key = f"{obj.__class__.__name__}.{obj.id}"
        FileStorage.__objects[key] = obj

    def save(self):
        """Serialize __objects to the JSON file (path: __file_path)."""
        odict = {k: v.to_dict() for k, v in FileStorage.__objects.items()}
        with open(FileStorage.__file_path, "w", encoding="utf-8") as f:
            json.dump(odict, f)

    def reload(self):
        """Deserialize the JSON file to __objects if the file exists."""
        if not os.path.isfile(FileStorage.__file_path):
            return
        from models.base_model import BaseModel
        classes = {"BaseModel": BaseModel}
        try:
            with open(FileStorage.__file_path, "r", encoding="utf-8") as f:
                obj_dict = json.load(f)
                for k, v in obj_dict.items():
                    cls_name = v.get("__class__")
                    if cls_name in classes:
                        self.new(classes[cls_name](**v))
        except Exception:
            pass
