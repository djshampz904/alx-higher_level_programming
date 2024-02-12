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
        self.assertEqual(base.Base().id, 4)

    def test_rectangle_class(self):
        base.Base._Base__nb_objects = 0
        self.assertEqual(rectangle.Rectangle(10, 2).id, 1)
        self.assertEqual(rectangle.Rectangle(2, 10).id, 2)
        self.assertEqual(rectangle.Rectangle(10, 2, 0, 0, 12).id, 12)
        self.assertEqual(rectangle.Rectangle(2, 10, 0, 0, 13).id, 13)
        self.assertEqual(rectangle.Rectangle(10, 2, 0, 0, 14).id, 14)

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
        self.assertEqual(rect.__str__(), "[Rectangle] (89) 10/10 - 10/10")

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

    def test_create(self):
        base.Base._Base__nb_objects = 0
        r1 = rectangle.Rectangle(3, 5, 1, 9)
        r1_dictionary = r1.to_dictionary()
        r2 = rectangle.Rectangle.create(**r1_dictionary)
        self.assertEqual(r1.__str__(), r2.__str__())
        self.assertFalse(r1 is r2)

    def test_load_from_file(self):
        base.Base._Base__nb_objects = 0
        r1 = rectangle.Rectangle(10, 7, 2, 8)
        r2 = rectangle.Rectangle(2, 4)
        list_rectangles_input = [r1, r2]
        rectangle.Rectangle.save_to_file(list_rectangles_input)
        list_rectangles_output = rectangle.Rectangle.load_from_file()
        self.assertEqual(list_rectangles_output[0].__str__(), r1.__str__())
        self.assertEqual(list_rectangles_output[1].__str__(), r2.__str__())

    def test_square_load_from_file(self):
        base.Base._Base__nb_objects = 0
        s1 = square.Square(5)
        s2 = square.Square(7, 9, 1)
        list_squares_input = [s1, s2]
        square.Square.save_to_file(list_squares_input)
        list_squares_output = square.Square.load_from_file()
        self.assertEqual(list_squares_output[0].__str__(), s1.__str__())
        self.assertEqual(list_squares_output[1].__str__(), s2.__str__())

    def test_square_update_kwargs(self):
        base.Base._Base__nb_objects = 0
        sqr = square.Square(5)
        sqr.update(size=7, y=1, x=9, id=10)
        self.assertEqual(sqr.__str__(), "[Square] (10) 9/1 - 7")

    def test_square_str(self):
        base.Base._Base__nb_objects = 0
        self.assertEqual(square.Square(5).__str__(), "[Square] (1) 0/0 - 5")

    def test_square_area(self):
        base.Base._Base__nb_objects = 0
        self.assertEqual(square.Square(5).area(), 25)

    def test_square_display(self):
        base.Base._Base__nb_objects = 0
        self.assertEqual(square.Square(2).display(), None)

    def test_square_exeptions(self):
        with self.assertRaises(TypeError):
            square.Square("2")
        with self.assertRaises(ValueError):
            square.Square(2, 3, -1)

    def test_square_size(self):
        base.Base._Base__nb_objects = 0
        sqr = square.Square(5)
        self.assertEqual(sqr.size, 5)
        sqr.size = 10
        self.assertEqual(sqr.size, 10)
        with self.assertRaises(TypeError):
            sqr.size = "9"
        with self.assertRaises(ValueError):
            sqr.size = -10
        with self.assertRaises(ValueError):
            sqr.size = 0
        with self.assertRaises(ValueError):
            sqr.size = 0

    def test_square_update(self):
        base.Base._Base__nb_objects = 0
        sqr = square.Square(5)
        sqr.update(10)
        self.assertEqual(sqr.id, 10)

    def test_square_update_kwargs(self):
        base.Base._Base__nb_objects = 0
        sqr = square.Square(5)
        sqr.update(size=7, y=1, x=9, id=10)
        self.assertEqual(sqr.__str__(), "[Square] (10) 9/1 - 7")

    def test_square_to_dictionary(self):
        base.Base._Base__nb_objects = 0
        self.assertEqual(square.Square(10, 2, 1).to_dictionary(),
                         {'id': 1, 'x': 2, 'size': 10, 'y': 1})

if __name__ == "__main__":
    unittest.main()