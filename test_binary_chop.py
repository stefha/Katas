import unittest
from Binary_chop import chop, chop_recursive, chop_modular, chop_simple_structure, simple_chop, binary_chop_iterative, \
    binary_chop_recursive_new, binary_chop_iterative_2, binary_chop_recursive_2


class TestBinaryChop(unittest.TestCase):

    def test_chop(self):
        self.assertEqual(-1, chop(3, []))
        self.assertEqual(-1, chop(3, [1]))
        self.assertEqual(0, chop(1, [1]))
        #
        self.assertEqual(-1, chop(3, [0, 1]))
        self.assertEqual(0, chop(1, [1, 5]))
        self.assertEqual(1, chop(1, [0, 1]))
        #
        self.assertEqual(0, chop(1, [1, 3, 5]))
        self.assertEqual(1, chop(3, [1, 3, 5]))
        self.assertEqual(2, chop(5, [1, 3, 5]))
        self.assertEqual(-1, chop(0, [1, 3, 5]))
        self.assertEqual(-1, chop(2, [1, 3, 5]))
        self.assertEqual(-1, chop(4, [1, 3, 5]))
        self.assertEqual(-1, chop(6, [1, 3, 5]))
        #
        self.assertEqual(0, chop(1, [1, 3, 5, 7]))
        self.assertEqual(1, chop(3, [1, 3, 5, 7]))
        self.assertEqual(2, chop(5, [1, 3, 5, 7]))
        self.assertEqual(3, chop(7, [1, 3, 5, 7]))
        self.assertEqual(-1, chop(0, [1, 3, 5, 7]))
        self.assertEqual(-1, chop(2, [1, 3, 5, 7]))
        self.assertEqual(-1, chop(4, [1, 3, 5, 7]))
        self.assertEqual(-1, chop(6, [1, 3, 5, 7]))
        self.assertEqual(-1, chop(8, [1, 3, 5, 7]))

    def test_chop_recursive(self):
        self.assertEqual(-1, chop_recursive(3, []))
        self.assertEqual(-1, chop_recursive(3, [1]))
        self.assertEqual(0, chop_recursive(1, [1]))
        #
        self.assertEqual(-1, chop_recursive(3, [0, 1]))
        self.assertEqual(0, chop_recursive(1, [1, 5]))
        self.assertEqual(1, chop_recursive(1, [0, 1]))
        #

        self.assertEqual(0, chop_recursive(1, [1, 3, 5]))
        self.assertEqual(1, chop_recursive(3, [1, 3, 5]))
        self.assertEqual(2, chop_recursive(5, [1, 3, 5]))
        self.assertEqual(-1, chop_recursive(0, [1, 3, 5]))
        self.assertEqual(-1, chop_recursive(2, [1, 3, 5]))
        self.assertEqual(-1, chop_recursive(4, [1, 3, 5]))
        self.assertEqual(-1, chop_recursive(6, [1, 3, 5]))
        #
        self.assertEqual(0, chop_recursive(1, [1, 3, 5, 7]))
        self.assertEqual(1, chop_recursive(3, [1, 3, 5, 7]))
        self.assertEqual(2, chop_recursive(5, [1, 3, 5, 7]))
        self.assertEqual(3, chop_recursive(7, [1, 3, 5, 7]))
        self.assertEqual(-1, chop_recursive(0, [1, 3, 5, 7]))
        self.assertEqual(-1, chop_recursive(2, [1, 3, 5, 7]))
        self.assertEqual(-1, chop_recursive(4, [1, 3, 5, 7]))
        self.assertEqual(-1, chop_recursive(6, [1, 3, 5, 7]))
        self.assertEqual(-1, chop_recursive(8, [1, 3, 5, 7]))

    def test_chop_modular(self):
        self.assertEqual(-1, chop_modular(3, []))
        self.assertEqual(-1, chop_modular(3, [1]))
        self.assertEqual(0, chop_modular(1, [1]))
        #
        self.assertEqual(-1, chop_modular(3, [0, 1]))
        self.assertEqual(0, chop_modular(1, [1, 5]))
        self.assertEqual(1, chop_modular(1, [0, 1]))
        #
        self.assertEqual(0, chop_modular(1, [1, 3, 5]))
        self.assertEqual(1, chop_modular(3, [1, 3, 5]))
        self.assertEqual(2, chop_modular(5, [1, 3, 5]))
        self.assertEqual(-1, chop_modular(0, [1, 3, 5]))
        self.assertEqual(-1, chop_modular(2, [1, 3, 5]))
        self.assertEqual(-1, chop_modular(4, [1, 3, 5]))
        self.assertEqual(-1, chop_modular(6, [1, 3, 5]))
        #
        self.assertEqual(0, chop_modular(1, [1, 3, 5, 7]))
        self.assertEqual(1, chop_modular(3, [1, 3, 5, 7]))
        self.assertEqual(2, chop_modular(5, [1, 3, 5, 7]))
        self.assertEqual(3, chop_modular(7, [1, 3, 5, 7]))
        self.assertEqual(-1, chop_modular(0, [1, 3, 5, 7]))
        self.assertEqual(-1, chop_modular(2, [1, 3, 5, 7]))
        self.assertEqual(-1, chop_modular(4, [1, 3, 5, 7]))
        self.assertEqual(-1, chop_modular(6, [1, 3, 5, 7]))
        self.assertEqual(-1, chop_modular(8, [1, 3, 5, 7]))

    def test_chop_simple_structure(self):
        self.assertEqual(-1, chop_simple_structure(3, []))
        self.assertEqual(-1, chop_simple_structure(3, [1]))
        self.assertEqual(0, chop_simple_structure(1, [1]))
        #
        self.assertEqual(-1, chop_simple_structure(3, [0, 1]))
        self.assertEqual(0, chop_simple_structure(1, [1, 5]))
        self.assertEqual(1, chop_simple_structure(1, [0, 1]))
        #
        self.assertEqual(0, chop_simple_structure(1, [1, 3, 5]))
        self.assertEqual(1, chop_simple_structure(3, [1, 3, 5]))
        self.assertEqual(2, chop_simple_structure(5, [1, 3, 5]))
        self.assertEqual(-1, chop_simple_structure(0, [1, 3, 5]))
        self.assertEqual(-1, chop_simple_structure(2, [1, 3, 5]))
        self.assertEqual(-1, chop_simple_structure(4, [1, 3, 5]))
        self.assertEqual(-1, chop_simple_structure(6, [1, 3, 5]))
        #
        self.assertEqual(0, chop_simple_structure(1, [1, 3, 5, 7]))
        self.assertEqual(1, chop_simple_structure(3, [1, 3, 5, 7]))
        self.assertEqual(2, chop_simple_structure(5, [1, 3, 5, 7]))
        self.assertEqual(3, chop_simple_structure(7, [1, 3, 5, 7]))
        self.assertEqual(-1, chop_simple_structure(0, [1, 3, 5, 7]))
        self.assertEqual(-1, chop_simple_structure(2, [1, 3, 5, 7]))
        self.assertEqual(-1, chop_simple_structure(4, [1, 3, 5, 7]))
        self.assertEqual(-1, chop_simple_structure(6, [1, 3, 5, 7]))
        self.assertEqual(-1, chop_simple_structure(8, [1, 3, 5, 7]))

    def test_simple_chop(self):
        self.assertEqual(-1, simple_chop(3, []))
        self.assertEqual(-1, simple_chop(3, [1]))
        self.assertEqual(0, simple_chop(1, [1]))
        #
        self.assertEqual(-1, simple_chop(3, [0, 1]))
        self.assertEqual(0, simple_chop(1, [1, 5]))
        self.assertEqual(1, simple_chop(1, [0, 1]))
        #
        self.assertEqual(0, simple_chop(1, [1, 3, 5]))
        self.assertEqual(1, simple_chop(3, [1, 3, 5]))
        self.assertEqual(2, simple_chop(5, [1, 3, 5]))
        self.assertEqual(-1, simple_chop(0, [1, 3, 5]))
        self.assertEqual(-1, simple_chop(2, [1, 3, 5]))
        self.assertEqual(-1, simple_chop(4, [1, 3, 5]))
        self.assertEqual(-1, simple_chop(6, [1, 3, 5]))
        #
        self.assertEqual(0, simple_chop(1, [1, 3, 5, 7]))
        self.assertEqual(1, simple_chop(3, [1, 3, 5, 7]))
        self.assertEqual(2, simple_chop(5, [1, 3, 5, 7]))
        self.assertEqual(3, simple_chop(7, [1, 3, 5, 7]))
        self.assertEqual(-1, simple_chop(0, [1, 3, 5, 7]))
        self.assertEqual(-1, simple_chop(2, [1, 3, 5, 7]))
        self.assertEqual(-1, simple_chop(4, [1, 3, 5, 7]))
        self.assertEqual(-1, simple_chop(6, [1, 3, 5, 7]))
        self.assertEqual(-1, simple_chop(8, [1, 3, 5, 7]))

    def test_chop_iterative(self):
        self.assertEqual(-1, binary_chop_iterative(3, []))
        self.assertEqual(-1, binary_chop_iterative(3, [1]))
        self.assertEqual(0, binary_chop_iterative(1, [1]))
        #
        self.assertEqual(-1, binary_chop_iterative(3, [0, 1]))
        self.assertEqual(0, binary_chop_iterative(1, [1, 5]))
        self.assertEqual(1, binary_chop_iterative(1, [0, 1]))
        #
        self.assertEqual(0, binary_chop_iterative(1, [1, 3, 5]))
        self.assertEqual(1, binary_chop_iterative(3, [1, 3, 5]))
        self.assertEqual(2, binary_chop_iterative(5, [1, 3, 5]))
        self.assertEqual(-1, binary_chop_iterative(0, [1, 3, 5]))
        self.assertEqual(-1, binary_chop_iterative(2, [1, 3, 5]))
        self.assertEqual(-1, binary_chop_iterative(4, [1, 3, 5]))
        self.assertEqual(-1, binary_chop_iterative(6, [1, 3, 5]))
        #
        self.assertEqual(0, binary_chop_iterative(1, [1, 3, 5, 7]))
        self.assertEqual(1, binary_chop_iterative(3, [1, 3, 5, 7]))
        self.assertEqual(2, binary_chop_iterative(5, [1, 3, 5, 7]))
        self.assertEqual(3, binary_chop_iterative(7, [1, 3, 5, 7]))
        self.assertEqual(-1, binary_chop_iterative(0, [1, 3, 5, 7]))
        self.assertEqual(-1, binary_chop_iterative(2, [1, 3, 5, 7]))
        self.assertEqual(-1, binary_chop_iterative(4, [1, 3, 5, 7]))
        self.assertEqual(-1, binary_chop_iterative(6, [1, 3, 5, 7]))
        self.assertEqual(-1, binary_chop_iterative(8, [1, 3, 5, 7]))

    def test_chop_recursive_new(self):
        self.assertEqual(-1, binary_chop_recursive_new(3, []))
        self.assertEqual(-1, binary_chop_recursive_new(3, [1]))
        self.assertEqual(0, binary_chop_recursive_new(1, [1]))
        #
        self.assertEqual(-1, binary_chop_recursive_new(3, [0, 1]))
        self.assertEqual(0, binary_chop_recursive_new(1, [1, 5]))
        self.assertEqual(1, binary_chop_recursive_new(1, [0, 1]))
        #
        self.assertEqual(0, binary_chop_recursive_new(1, [1, 3, 5]))
        self.assertEqual(1, binary_chop_recursive_new(3, [1, 3, 5]))
        self.assertEqual(2, binary_chop_recursive_new(5, [1, 3, 5]))
        self.assertEqual(-1, binary_chop_recursive_new(0, [1, 3, 5]))
        self.assertEqual(-1, binary_chop_recursive_new(2, [1, 3, 5]))
        self.assertEqual(-1, binary_chop_recursive_new(4, [1, 3, 5]))
        self.assertEqual(-1, binary_chop_recursive_new(6, [1, 3, 5]))
        #
        self.assertEqual(0, binary_chop_recursive_new(1, [1, 3, 5, 7]))
        self.assertEqual(1, binary_chop_recursive_new(3, [1, 3, 5, 7]))
        self.assertEqual(2, binary_chop_recursive_new(5, [1, 3, 5, 7]))
        self.assertEqual(3, binary_chop_recursive_new(7, [1, 3, 5, 7]))
        self.assertEqual(-1, binary_chop_recursive_new(0, [1, 3, 5, 7]))
        self.assertEqual(-1, binary_chop_recursive_new(2, [1, 3, 5, 7]))
        self.assertEqual(-1, binary_chop_recursive_new(4, [1, 3, 5, 7]))
        self.assertEqual(-1, binary_chop_recursive_new(6, [1, 3, 5, 7]))
        self.assertEqual(-1, binary_chop_recursive_new(8, [1, 3, 5, 7]))

    def test_chop_iterative_2(self):
        self.assertEqual(-1, binary_chop_iterative_2(3, []))
        self.assertEqual(-1, binary_chop_iterative_2(3, [1]))
        self.assertEqual(0, binary_chop_iterative_2(1, [1]))
        #
        self.assertEqual(-1, binary_chop_iterative_2(3, [0, 1]))
        self.assertEqual(0, binary_chop_iterative_2(1, [1, 5]))
        self.assertEqual(1, binary_chop_iterative_2(1, [0, 1]))
        #
        self.assertEqual(0, binary_chop_iterative_2(1, [1, 3, 5]))
        self.assertEqual(1, binary_chop_iterative_2(3, [1, 3, 5]))
        self.assertEqual(2, binary_chop_iterative_2(5, [1, 3, 5]))
        self.assertEqual(-1, binary_chop_iterative_2(0, [1, 3, 5]))
        self.assertEqual(-1, binary_chop_iterative_2(2, [1, 3, 5]))
        self.assertEqual(-1, binary_chop_iterative_2(4, [1, 3, 5]))
        self.assertEqual(-1, binary_chop_iterative_2(6, [1, 3, 5]))
        #
        self.assertEqual(0, binary_chop_iterative_2(1, [1, 3, 5, 7]))
        self.assertEqual(1, binary_chop_iterative_2(3, [1, 3, 5, 7]))
        self.assertEqual(2, binary_chop_iterative_2(5, [1, 3, 5, 7]))
        self.assertEqual(3, binary_chop_iterative_2(7, [1, 3, 5, 7]))
        self.assertEqual(-1, binary_chop_iterative_2(0, [1, 3, 5, 7]))
        self.assertEqual(-1, binary_chop_iterative_2(2, [1, 3, 5, 7]))
        self.assertEqual(-1, binary_chop_iterative_2(4, [1, 3, 5, 7]))
        self.assertEqual(-1, binary_chop_iterative_2(6, [1, 3, 5, 7]))
        self.assertEqual(-1, binary_chop_iterative_2(8, [1, 3, 5, 7]))

    def test_chop_recursive_2(self):
        self.assertEqual(-1, binary_chop_recursive_2(3, []))
        self.assertEqual(-1, binary_chop_recursive_2(3, [1]))
        self.assertEqual(0, binary_chop_recursive_2(1, [1]))
        #
        self.assertEqual(-1, binary_chop_recursive_2(3, [0, 1]))
        self.assertEqual(0, binary_chop_recursive_2(1, [1, 5]))
        self.assertEqual(1, binary_chop_recursive_2(1, [0, 1]))
        #
        self.assertEqual(0, binary_chop_recursive_2(1, [1, 3, 5]))
        self.assertEqual(1, binary_chop_recursive_2(3, [1, 3, 5]))
        self.assertEqual(2, binary_chop_recursive_2(5, [1, 3, 5]))
        self.assertEqual(-1, binary_chop_recursive_2(0, [1, 3, 5]))
        self.assertEqual(-1, binary_chop_recursive_2(2, [1, 3, 5]))
        self.assertEqual(-1, binary_chop_recursive_2(4, [1, 3, 5]))
        self.assertEqual(-1, binary_chop_recursive_2(6, [1, 3, 5]))
        #
        self.assertEqual(0, binary_chop_recursive_2(1, [1, 3, 5, 7]))
        self.assertEqual(1, binary_chop_recursive_2(3, [1, 3, 5, 7]))
        self.assertEqual(2, binary_chop_recursive_2(5, [1, 3, 5, 7]))
        self.assertEqual(3, binary_chop_recursive_2(7, [1, 3, 5, 7]))
        self.assertEqual(-1, binary_chop_recursive_2(0, [1, 3, 5, 7]))
        self.assertEqual(-1, binary_chop_recursive_2(2, [1, 3, 5, 7]))
        self.assertEqual(-1, binary_chop_recursive_2(4, [1, 3, 5, 7]))
        self.assertEqual(-1, binary_chop_recursive_2(6, [1, 3, 5, 7]))
        self.assertEqual(-1, binary_chop_recursive_2(8, [1, 3, 5, 7]))
