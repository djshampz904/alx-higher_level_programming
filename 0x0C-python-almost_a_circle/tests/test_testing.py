import unittest
import models.base as base
import models.rectangle as rectangle
import models.square as square


class TestMaxInteger(unittest.TestCase):
    """ Test base class """

    def test_base_class(self):
        # Create instances of Base class
        base1 = base.Base()
        base2 = base.Base()
        base3 = base.Base(id=10)
        base4 = base.Base()

        # Check if id is assigned correctly
        self.assertEqual(base1.id, 1)
        self.assertEqual(base2.id, 2)
        self.assertEqual(base3.id, 10)
        self.assertEqual(base4.id, 3)

        base.Base._Base__nb_objects = 0

    def test_rectangle_class(self):
        # Create instances of Rectangle class
        rect1 = rectangle.Rectangle(10, 2)
        rect2 = rectangle.Rectangle(2, 10)
        rect3 = rectangle.Rectangle(10, 2, 0, 0, 12)
        rect4 = rectangle.Rectangle(2, 10, 0, 0, 13)

        # Check if id is assigned correctly
        self.assertEqual(rect1.id, 1)
        self.assertEqual(rect2.id, 2)
        self.assertEqual(rect3.id, 12)
        self.assertEqual(rect4.id, 13)
        self.assertEqual(rect1.width, 10)
        self.assertEqual(rect1.height, 2)

        base.Base._Base__nb_objects = 0

    def test_rectangle_exeptions(self):
        # Test exceptions
        with self.assertRaises(TypeError):
            rectangle.Rectangle(10, "2")
        with self.assertRaises(ValueError):
            rectangle.Rectangle(10, 2, 3, -1)
        with self.assertRaises(TypeError):
            rectangle.Rectangle(10, 2, 3, "12")
        with self.assertRaises(TypeError):
            rectangle.Rectangle(10, 2, 3, [12])
        with self.assertRaises(ValueError):
            rectangle.Rectangle(10, 2, 3, -12)

        """reset"""
        base.Base._Base__nb_objects = 0

    def test_rectangle_area(self):
        # Test area method
        rect1 = rectangle.Rectangle(10, 2)
        rect2 = rectangle.Rectangle(2, 10)
        rect3 = rectangle.Rectangle(10, 2, 0, 0, 12)
        rect4 = rectangle.Rectangle(2, 10, 0, 0, 13)

        self.assertEqual(rect1.area(), 20)
        self.assertEqual(rect2.area(), 20)
        self.assertEqual(rect3.area(), 20)
        self.assertEqual(rect4.area(), 20)

        base.Base._Base__nb_objects = 0

    def test_rectangle_display(self):
        # Test display method
        rect1 = rectangle.Rectangle(2, 3)
        rect2 = rectangle.Rectangle(3, 2)
        rect3 = rectangle.Rectangle(2, 3, 2, 2)
        rect4 = rectangle.Rectangle(3, 2, 2, 2)

        self.assertEqual(rect1.display(), None)
        self.assertEqual(rect2.display(), None)
        self.assertEqual(rect3.display(), None)
        self.assertEqual(rect4.display(), None)

        base.Base._Base__nb_objects = 0
        
    def test_rectangle_str(self):
        # Test __str__ method
        rect1 = rectangle.Rectangle(4, 6, 2, 1, 12)
        rect2 = rectangle.Rectangle(5, 5, 1)
        rect3 = rectangle.Rectangle(2, 3)
        rect4 = rectangle.Rectangle(3, 2, 2, 2)

        self.assertEqual(rect1.__str__(), "[Rectangle] (12) 2/1 - 4/6")
        self.assertEqual(rect2.__str__(), "[Rectangle] (1) 1/0 - 5/5")
        self.assertEqual(rect3.__str__(), "[Rectangle] (2) 0/0 - 2/3")
        self.assertEqual(rect4.__str__(), "[Rectangle] (3) 2/2 - 3/2")

        base.Base._Base__nb_objects = 0
    
    def test_rectangle_update(self):
        # Test update method
        rect1 = rectangle.Rectangle(10, 10, 10, 10, 10)
        rect2 = rectangle.Rectangle(10, 10, 10, 10, 10)
        rect3 = rectangle.Rectangle(10, 10, 10, 10, 10)
        rect4 = rectangle.Rectangle(10, 10, 10, 10, 10)

        rect1.update(89)
        self.assertEqual(rect1.__str__(), "[Rectangle] (89) 10/10 - 10/10")
        rect2.update(89, 2)
        self.assertEqual(rect2.__str__(), "[Rectangle] (89) 10/10 - 2/10")
        rect3.update(89, 2, 3)
        self.assertEqual(rect3.__str__(), "[Rectangle] (89) 10/10 - 2/3")
        rect4.update(89, 2, 3, 4)
        self.assertEqual(rect4.__str__(), "[Rectangle] (89) 4/10 - 2/3")

        base.Base._Base__nb_objects = 0
        
    def test_rectangle_update_kwargs(self):
        # Test update method with kwargs
        rect1 = rectangle.Rectangle(10, 10, 10, 10, 10)
        rect2 = rectangle.Rectangle(10, 10, 10, 10, 10)
        rect3 = rectangle.Rectangle(10, 10, 10, 10, 10)
        rect4 = rectangle.Rectangle(10, 10, 10, 10, 10)

        rect1.update(height=1)
        self.assertEqual(rect1.__str__(), "[Rectangle] (10) 10/10 - 10/1")
        rect2.update(width=1, x=2)
        self.assertEqual(rect2.__str__(), "[Rectangle] (10) 2/10 - 1/10")
        rect3.update(y=1, width=2, x=3, id=89)
        self.assertEqual(rect3.__str__(), "[Rectangle] (89) 3/1 - 2/10")
        rect4.update(x=1, height=2, y=3, width=4)
        self.assertEqual(rect4.__str__(), "[Rectangle] (10) 1/3 - 4/2")

        base.Base._Base__nb_objects = 0
    
    def test_square_class(self):
        # Create instances of Square class
        sqr1 = square.Square(10)
        sqr2 = square.Square(2)
        sqr3 = square.Square(10, 0, 0, 12)
        sqr4 = square.Square(2, 0, 0, 13)
        sqr5 = square.Square(5)

        # Check if id is assigned correctly
        self.assertEqual(sqr1.id, 1)
        self.assertEqual(sqr2.id, 2)
        self.assertEqual(sqr3.id, 12)
        self.assertEqual(sqr4.id, 13)
        self.assertEqual(sqr1.size, 10)
        

        base.Base._Base__nb_objects = 0