import unittest

from hamcrest import assert_that, is_not, ends_with

from hotel_names import hotel_names


class TestHotelNames(unittest.TestCase):
    def test_get_hotel_name(self):
        name = hotel_names.get_hotel_name()
        assert_that(name, is_not(None))

    def test_suffix(self):
        suffix = "and Chocolat"
        name = hotel_names.get_hotel_name(suffix=suffix)
        assert_that(name, ends_with(suffix))

