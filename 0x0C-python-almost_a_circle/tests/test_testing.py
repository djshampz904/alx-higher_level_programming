import unittest
from models import base, rectangle, square

class TestMaxInteger(unittest.TestCase):
    """ Test base class """

    def test_base_class(self):
        base.Base._Base__nb_objects = 0
        self.assertEqual(base.Base().id, 1)
        self.assertEqual(base.Base().id, 2)
        self.assertEqual(base.Base(id=10).id, 10)
        self.assertEqual(base.Base().id, 3)

    def test_rectangle_class(self):
        base.Base._Base__nb_objects = 0
        self.assertEqual(rectangle.Rectangle(10, 2).id, 1)
        self.assertEqual(rectangle.Rectangle(2, 10).id, 2)
        self.assertEqual(rectangle.Rectangle(10, 2, 0, 0, 12).id, 12)
        self.assertEqual(rectangle.Rectangle(2, 10, 0, 0, 13).id, 13)

    def test_rectangle_exeptions(self):
        with self.assertRaises(TypeError):
            rectangle.Rectangle(10, "2")
        with self.assertRaises(ValueError):
            rectangle.Rectangle(10, 2, 3, -1)

    def test_rectangle_area(self):
        base.Base._Base__nb_objects = 0
        self.assertEqual(rectangle.Rectangle(10, 2).area(), 20)
        self.assertEqual(rectangle.Rectangle(2, 10).area(), 20)

    def test_rectangle_display(self):
        base.Base._Base__nb_objects = 0
        self.assertEqual(rectangle.Rectangle(2, 3).display(), None)

    def test_rectangle_str(self):
        base.Base._Base__nb_objects = 0
        self.assertEqual(rectangle.Rectangle(4, 6, 2, 1, 12).__str__(), "[Rectangle] (12) 2/1 - 4/6")

    def test_rectangle_update(self):
        base.Base._Base__nb_objects = 0
        rect = rectangle.Rectangle(10, 10, 10, 10, 10)
        rect.update(89)
        self.assertEqual(rect.__str__(), "[Rectangle] (10) 10/10 - 89/10")

    def test_rectangle_update_kwargs(self):
        base.Base._Base__nb_objects = 0
        rect = rectangle.Rectangle(10, 10, 10, 10, 10)
        rect.update(height=1)
        self.assertEqual(rect.__str__(), "[Rectangle] (10) 10/10 - 10/1")

    def test_square_class(self):
        base.Base._Base__nb_objects = 0
        self.assertEqual(square.Square(10).id, 1)

    def test_square_update(self):
        base.Base._Base__nb_objects = 0
        sqr = square.Square(5)
        sqr.update(10)
        self.assertEqual(sqr.id, 10)

    def test_to_dictionary(self):
        base.Base._Base__nb_objects = 0
        self.assertEqual(rectangle.Rectangle(10, 2, 1, 9).to_dictionary(), {'x': 1, 'y': 9, 'id': 1, 'height': 2, 'width': 10})

    def test_square_to_dictionary(self):
        base.Base._Base__nb_objects = 0
        self.assertEqual(square.Square(10, 2, 1).to_dictionary(), {'id': 1, 'x': 2, 'size': 10, 'y': 1})

    def test_save_to_file(self):
        base.Base._Base__nb_objects = 0
        rectangle.Rectangle.save_to_file([rectangle.Rectangle(10, 7, 2, 8), rectangle.Rectangle(2, 4)])
        with open("Rectangle.json", "r") as file:
            self.assertEqual(len(file.read()), 105)

    def test_from_json_string(self):
        base.Base._Base__nb_objects = 0
        list_input = [
            {'id': 89, 'width': 10, 'height': 4}, {'id': 7, 'width': 1, 'height': 7}
        ]
        json_list_input = rectangle.Rectangle.to_json_string(list_input)
        list_output = rectangle.Rectangle.from_json_string(json_list_input)
        self.assertEqual(list_output, list_input)


