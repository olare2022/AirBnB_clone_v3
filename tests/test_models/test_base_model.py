#!/usr/bin/python3
<<<<<<< HEAD

'''
    All the test for the base_model are implemented here.
'''

import unittest
import sys
import datetime
from models.base_model import BaseModel
from io import StringIO
from os import getenv

storage = getenv("HBNB_TYPE_STORAGE", "fs")


class TestBase(unittest.TestCase):
    '''
        Testing the base class model.
    '''
    def setUp(self):
        '''
            Initializing instance.
        '''
        self.my_model = BaseModel()
        self.my_model.name = "Binita Rai"
        self.new = BaseModel()

    def TearDown(self):
        '''
            Removing instance.
        '''
        del self.my_model

    def test_id_type(self):
        '''
            Checks that the type of the id is string.
        '''
        self.assertEqual("<class 'str'>", str(type(self.my_model.id)))

    def test_ids_differ(self):
        '''
            Checks that the ids between two instances are different.
        '''
        new_model = BaseModel()
        self.assertNotEqual(new_model.id, self.my_model.id)

    def test_name(self):
        '''
            Checks that an attribute can be added.
        '''
        self.assertEqual("Binita Rai", self.my_model.name)

    def test_a_updated_created_equal(self):
        '''
            Checks that both dates are equal.
        '''
        self.assertEqual(self.my_model.updated_at.year,
                         self.my_model.created_at.year)

    def test_str_overide(self):
        '''
            Checks that the right message gets printed.
        '''
        backup = sys.stdout
        inst_id = self.my_model.id
        capture_out = StringIO()
        sys.stdout = capture_out
        print(self.my_model)

        cap = capture_out.getvalue().split(" ")
        self.assertEqual(cap[0], "[BaseModel]")

        self.assertEqual(cap[1], "({})".format(inst_id))
        sys.stdout = backup

    def test_to_dict_type(self):
        '''
            Checks that the to_dict method return type.
        '''

        self.assertEqual("<class 'dict'>",
                         str(type(self.my_model.to_dict())))

    def test_to_dict_class(self):
        '''
            Checks that the __class__ key exists.
        '''

        self.assertEqual("BaseModel", (self.my_model.to_dict())["__class__"])

    def test_to_dict_type_updated_at(self):
        '''
            Checks the type of the value of updated_at.
        '''
        self.assertEqual("<class 'str'>",
                         str(type((self.my_model.to_dict())["updated_at"])))

    def test_to_dict_type_created_at(self):
        '''
            Checks the type of the value of created_at.
        '''
        tmp = self.my_model.to_dict()
        self.assertEqual("<class 'str'>", str(type(tmp["created_at"])))

    def test_kwargs_instantiation(self):
        '''
            Test that an instance is created using the
            key value pair.
        '''
        my_model_dict = self.my_model.to_dict()
        new_model = BaseModel(**my_model_dict)
        self.assertEqual(new_model.id, self.my_model.id)

    def test_type_created_at(self):
        '''
            Test that the new_model's updated_at
            data type is datetime.
        '''
        my_model_dict = self.my_model.to_dict()
        new_model = BaseModel(my_model_dict)
        self.assertTrue(isinstance(new_model.created_at, datetime.datetime))

    def test_type_updated_at(self):
        '''
            Test that the new_model's created_at
            data type is datetime.
        '''
        my_model_dict = self.my_model.to_dict()
        new_model = BaseModel(my_model_dict)
        self.assertTrue(isinstance(new_model.updated_at, datetime.datetime))

    def test_compare_dict(self):
        '''
            Test that the new_model's and my_model's
            dictionary values are same.
        '''
        my_model_dict = self.my_model.to_dict()
        new_model = BaseModel(**my_model_dict)
        new_model_dict = new_model.to_dict()
        self.assertEqual(my_model_dict, new_model_dict)

    def test_instance_diff(self):
        '''
            Test that the my_model and new_model are
            not the same instance.
        '''
        my_model_dict = self.my_model.to_dict()
        new_model = BaseModel(my_model_dict)
        self.assertNotEqual(self.my_model, new_model)

    @unittest.skipIf(storage == "db", "Testing database storage only")
    def test_save(self):
        '''
            Checks that after updating the instance; the dates differ in the
            updated_at attribute.
        '''
        old_update = self.new.updated_at
        self.new.save()
        self.assertNotEqual(self.new.updated_at, old_update)

    @unittest.skipIf(storage != "db", "Testing if using DBStorage")
    def test_basemodel_hasattr(self):
        '''
            Checks Class attributes
        '''
        self.assertTrue(hasattr(self.new, "id"))
        self.assertTrue(hasattr(self.new, "created_at"))
        self.assertTrue(hasattr(self.new, "updated_at"))

    @unittest.skipIf(storage != "db", "Testing if using DBStorage")
    def test_basemodel_attrtype(self):
        '''
            Check is attributes type
        '''
        new2 = BaseModel
        self.assertFalse(isinstance(new2.id, str))
        self.assertFalse(isinstance(new2.created_at, str))
        self.assertFalse(isinstance(new2.updated_at, str))
=======
"""Test BaseModel for expected behavior and documentation"""
from datetime import datetime
import inspect
import models
import pep8 as pycodestyle
import time
import unittest
from unittest import mock
BaseModel = models.base_model.BaseModel
module_doc = models.base_model.__doc__


class TestBaseModelDocs(unittest.TestCase):
    """Tests to check the documentation and style of BaseModel class"""

    @classmethod
    def setUpClass(self):
        """Set up for docstring tests"""
        self.base_funcs = inspect.getmembers(BaseModel, inspect.isfunction)

    def test_pep8_conformance(self):
        """Test that models/base_model.py conforms to PEP8."""
        for path in ['models/base_model.py',
                     'tests/test_models/test_base_model.py']:
            with self.subTest(path=path):
                errors = pycodestyle.Checker(path).check_all()
                self.assertEqual(errors, 0)

    def test_module_docstring(self):
        """Test for the existence of module docstring"""
        self.assertIsNot(module_doc, None,
                         "base_model.py needs a docstring")
        self.assertTrue(len(module_doc) > 1,
                        "base_model.py needs a docstring")

    def test_class_docstring(self):
        """Test for the BaseModel class docstring"""
        self.assertIsNot(BaseModel.__doc__, None,
                         "BaseModel class needs a docstring")
        self.assertTrue(len(BaseModel.__doc__) >= 1,
                        "BaseModel class needs a docstring")

    def test_func_docstrings(self):
        """Test for the presence of docstrings in BaseModel methods"""
        for func in self.base_funcs:
            with self.subTest(function=func):
                self.assertIsNot(
                    func[1].__doc__,
                    None,
                    "{:s} method needs a docstring".format(func[0])
                )
                self.assertTrue(
                    len(func[1].__doc__) > 1,
                    "{:s} method needs a docstring".format(func[0])
                )


class TestBaseModel(unittest.TestCase):
    """Test the BaseModel class"""
    def test_instantiation(self):
        """Test that object is correctly created"""
        inst = BaseModel()
        self.assertIs(type(inst), BaseModel)
        inst.name = "Holberton"
        inst.number = 89
        attrs_types = {
            "id": str,
            "created_at": datetime,
            "updated_at": datetime,
            "name": str,
            "number": int
        }
        for attr, typ in attrs_types.items():
            with self.subTest(attr=attr, typ=typ):
                self.assertIn(attr, inst.__dict__)
                self.assertIs(type(inst.__dict__[attr]), typ)
        self.assertEqual(inst.name, "Holberton")
        self.assertEqual(inst.number, 89)

    def test_datetime_attributes(self):
        """Test that two BaseModel instances have different datetime objects
        and that upon creation have identical updated_at and created_at
        value."""
        tic = datetime.now()
        inst1 = BaseModel()
        toc = datetime.now()
        self.assertTrue(tic <= inst1.created_at <= toc)
        time.sleep(1e-4)
        tic = datetime.now()
        inst2 = BaseModel()
        toc = datetime.now()
        self.assertTrue(tic <= inst2.created_at <= toc)
        self.assertEqual(inst1.created_at, inst1.updated_at)
        self.assertEqual(inst2.created_at, inst2.updated_at)
        self.assertNotEqual(inst1.created_at, inst2.created_at)
        self.assertNotEqual(inst1.updated_at, inst2.updated_at)

    def test_uuid(self):
        """Test that id is a valid uuid"""
        inst1 = BaseModel()
        inst2 = BaseModel()
        for inst in [inst1, inst2]:
            uuid = inst.id
            with self.subTest(uuid=uuid):
                self.assertIs(type(uuid), str)
                self.assertRegex(uuid,
                                 '^[0-9a-f]{8}-[0-9a-f]{4}'
                                 '-[0-9a-f]{4}-[0-9a-f]{4}'
                                 '-[0-9a-f]{12}$')
        self.assertNotEqual(inst1.id, inst2.id)

    def test_to_dict(self):
        """Test conversion of object attributes to dictionary for json"""
        my_model = BaseModel()
        my_model.name = "Holberton"
        my_model.my_number = 89
        d = my_model.to_dict()
        expected_attrs = ["id",
                          "created_at",
                          "updated_at",
                          "name",
                          "my_number",
                          "__class__"]
        self.assertCountEqual(d.keys(), expected_attrs)
        self.assertEqual(d['__class__'], 'BaseModel')
        self.assertEqual(d['name'], "Holberton")
        self.assertEqual(d['my_number'], 89)

    def test_to_dict_values(self):
        """test that values in dict returned from to_dict are correct"""
        t_format = "%Y-%m-%dT%H:%M:%S.%f"
        bm = BaseModel()
        new_d = bm.to_dict()
        self.assertEqual(new_d["__class__"], "BaseModel")
        self.assertEqual(type(new_d["created_at"]), str)
        self.assertEqual(type(new_d["updated_at"]), str)
        self.assertEqual(new_d["created_at"], bm.created_at.strftime(t_format))
        self.assertEqual(new_d["updated_at"], bm.updated_at.strftime(t_format))

    def test_str(self):
        """test that the str method has the correct output"""
        inst = BaseModel()
        string = "[BaseModel] ({}) {}".format(inst.id, inst.__dict__)
        self.assertEqual(string, str(inst))

    @mock.patch('models.storage')
    def test_save(self, mock_storage):
        """Test that save method updates `updated_at` and calls
        `storage.save`"""
        inst = BaseModel()
        old_created_at = inst.created_at
        old_updated_at = inst.updated_at
        inst.save()
        new_created_at = inst.created_at
        new_updated_at = inst.updated_at
        self.assertNotEqual(old_updated_at, new_updated_at)
        self.assertEqual(old_created_at, new_created_at)
        self.assertTrue(mock_storage.new.called)
        self.assertTrue(mock_storage.save.called)
>>>>>>> 0e0c3809a0163bc9e78f5689a9145452a504827f
