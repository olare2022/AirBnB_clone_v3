#!/usr/bin/python3
<<<<<<< HEAD
'''
    Testing the file_storage module.
'''

import os
import time
import json
import unittest
import models
from models import storage
from models.base_model import BaseModel
from models.state import State
from models.engine.file_storage import FileStorage

db = os.getenv("HBNB_TYPE_STORAGE")


@unittest.skipIf(db == 'db', "Testing DBstorage only")
class testFileStorage(unittest.TestCase):
    '''
        Testing the FileStorage class
    '''

    def setUp(self):
        '''
            Initializing classes
        '''
        self.storage = FileStorage()
        self.my_model = BaseModel()

    def tearDown(self):
        '''
            Cleaning up.
        '''

        try:
            os.remove("file.json")
        except FileNotFoundError:
            pass

    def test_all_return_type(self):
        '''
            Tests the data type of the return value of the all method.
        '''
        storage_all = self.storage.all()
        self.assertIsInstance(storage_all, dict)

    def test_new_method(self):
        '''
            Tests that the new method sets the right key and value pair
            in the FileStorage.__object attribute
        '''
        self.storage.new(self.my_model)
        key = str(self.my_model.__class__.__name__ + "." + self.my_model.id)
        self.assertTrue(key in self.storage._FileStorage__objects)

    def test_objects_value_type(self):
        '''
            Tests that the type of value contained in the FileStorage.__object
            is of type obj.__class__.__name__
        '''
        self.storage.new(self.my_model)
        key = str(self.my_model.__class__.__name__ + "." + self.my_model.id)
        val = self.storage._FileStorage__objects[key]
        self.assertIsInstance(self.my_model, type(val))

    def test_save_file_exists(self):
        '''
            Tests that a file gets created with the name file.json
        '''
        self.storage.save()
        self.assertTrue(os.path.isfile("file.json"))

    def test_save_file_read(self):
        '''
            Testing the contents of the files inside the file.json
        '''
        self.storage.save()
        self.storage.new(self.my_model)

        with open("file.json", encoding="UTF8") as fd:
            content = json.load(fd)

        self.assertTrue(type(content) is dict)

    def test_the_type_file_content(self):
        '''
            testing the type of the contents inside the file.
        '''
        self.storage.save()
        self.storage.new(self.my_model)

        with open("file.json", encoding="UTF8") as fd:
            content = fd.read()

        self.assertIsInstance(content, str)

    def test_reaload_without_file(self):
        '''
            Tests that nothing happens when file.json does not exists
            and reload is called
        '''

        try:
            self.storage.reload()
            self.assertTrue(True)
        except:
            self.assertTrue(False)

    def test_delete(self):
        '''
            Test delete method
        '''
        fs = FileStorage()
        new_state = State()
        fs.new(new_state)
        state_id = new_state.id
        fs.save()
        fs.delete(new_state)
        with open("file.json", encoding="UTF-8") as fd:
            state_dict = json.load(fd)
        for k, v in state_dict.items():
            self.assertFalse(state_id == k.split('.')[1])

    def test_model_storage(self):
        '''
            Test State model in Filestorage
        '''
        self.assertTrue(isinstance(storage, FileStorage))

    def test_get(self):
        '''
            Test if get method retrieves obj requested
        '''
        new_state = State(name="NewYork")
        storage.new(new_state)
        key = "State.{}".format(new_state.id)
        result = storage.get("State", new_state.id)
        self.assertTrue(result.id, new_state.id)
        self.assertIsInstance(result, State)

    def test_count(self):
        '''
            Test if count method returns expected number of objects
        '''
        old_count = storage.count("State")
        new_state1 = State(name="NewYork")
        storage.new(new_state1)
        new_state2 = State(name="Virginia")
        storage.new(new_state2)
        new_state3 = State(name="California")
        storage.new(new_state3)
        self.assertEqual(old_count + 3, storage.count("State"))
=======
"""
Contains the TestFileStorageDocs classes
"""

from datetime import datetime
import inspect
import models
from models.engine import file_storage
from models.amenity import Amenity
from models.base_model import BaseModel
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User
import json
import os
import pep8
import unittest
FileStorage = file_storage.FileStorage
classes = {"Amenity": Amenity, "BaseModel": BaseModel, "City": City,
           "Place": Place, "Review": Review, "State": State, "User": User}


class TestFileStorageDocs(unittest.TestCase):
    """Tests to check the documentation and style of FileStorage class"""
    @classmethod
    def setUpClass(cls):
        """Set up for the doc tests"""
        cls.fs_f = inspect.getmembers(FileStorage, inspect.isfunction)

    def test_pep8_conformance_file_storage(self):
        """Test that models/engine/file_storage.py conforms to PEP8."""
        pep8s = pep8.StyleGuide(quiet=True)
        result = pep8s.check_files(['models/engine/file_storage.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_pep8_conformance_test_file_storage(self):
        """Test tests/test_models/test_file_storage.py conforms to PEP8."""
        pep8s = pep8.StyleGuide(quiet=True)
        result = pep8s.check_files(['tests/test_models/test_engine/\
test_file_storage.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_file_storage_module_docstring(self):
        """Test for the file_storage.py module docstring"""
        self.assertIsNot(file_storage.__doc__, None,
                         "file_storage.py needs a docstring")
        self.assertTrue(len(file_storage.__doc__) >= 1,
                        "file_storage.py needs a docstring")

    def test_file_storage_class_docstring(self):
        """Test for the FileStorage class docstring"""
        self.assertIsNot(FileStorage.__doc__, None,
                         "FileStorage class needs a docstring")
        self.assertTrue(len(FileStorage.__doc__) >= 1,
                        "FileStorage class needs a docstring")

    def test_fs_func_docstrings(self):
        """Test for the presence of docstrings in FileStorage methods"""
        for func in self.fs_f:
            self.assertIsNot(func[1].__doc__, None,
                             "{:s} method needs a docstring".format(func[0]))
            self.assertTrue(len(func[1].__doc__) >= 1,
                            "{:s} method needs a docstring".format(func[0]))


class TestFileStorage(unittest.TestCase):
    """Test the FileStorage class"""
    @unittest.skipIf(models.storage_t == 'db', "not testing file storage")
    def test_all_returns_dict(self):
        """Test that all returns the FileStorage.__objects attr"""
        storage = FileStorage()
        new_dict = storage.all()
        self.assertEqual(type(new_dict), dict)
        self.assertIs(new_dict, storage._FileStorage__objects)

    @unittest.skipIf(models.storage_t == 'db', "not testing file storage")
    def test_new(self):
        """test that new adds an object to the FileStorage.__objects attr"""
        storage = FileStorage()
        save = FileStorage._FileStorage__objects
        FileStorage._FileStorage__objects = {}
        test_dict = {}
        for key, value in classes.items():
            with self.subTest(key=key, value=value):
                instance = value()
                instance_key = instance.__class__.__name__ + "." + instance.id
                storage.new(instance)
                test_dict[instance_key] = instance
                self.assertEqual(test_dict, storage._FileStorage__objects)
        FileStorage._FileStorage__objects = save

    @unittest.skipIf(models.storage_t == 'db', "not testing file storage")
    def test_save(self):
        """Test that save properly saves objects to file.json"""
        storage = FileStorage()
        new_dict = {}
        for key, value in classes.items():
            instance = value()
            instance_key = instance.__class__.__name__ + "." + instance.id
            new_dict[instance_key] = instance
        save = FileStorage._FileStorage__objects
        FileStorage._FileStorage__objects = new_dict
        storage.save()
        FileStorage._FileStorage__objects = save
        for key, value in new_dict.items():
            new_dict[key] = value.to_dict()
        string = json.dumps(new_dict)
        with open("file.json", "r") as f:
            js = f.read()
        self.assertEqual(json.loads(string), json.loads(js))
>>>>>>> 0e0c3809a0163bc9e78f5689a9145452a504827f
