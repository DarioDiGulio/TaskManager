import unittest
from unittest import TestCase

from src.base.Id import Id


class IdTest(TestCase):
    def test_value(self):
        self.assertEqual(Id(1).value, 1)

    def test_equality(self):
        self.assertEqual(Id(1), Id(1))


if __name__ == '__main__':
    unittest.main()
