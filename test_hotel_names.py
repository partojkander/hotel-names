import unittest

from hamcrest import assert_that, is_not, ends_with, starts_with, contains_string

from hotel_names import hotel_names


class TestHotelNames(unittest.TestCase):
    def test_get_hotel_name(self):
        name = hotel_names.get_hotel_name()
        assert_that(name, is_not(None))

    def test_custom_adjective(self):
        custom_adjective = "Hideous"
        name = hotel_names.get_hotel_name(adjective=custom_adjective)
        assert_that(name, starts_with(custom_adjective))

    def test_custom_noun(self):
        custom_noun = "Watermelon"
        name = hotel_names.get_hotel_name(noun=custom_noun)
        assert_that(name, contains_string(custom_noun))

    def test_custom_suffix(self):
        custom_suffix = "and Chocolat"
        name = hotel_names.get_hotel_name(suffix=custom_suffix)
        assert_that(name, ends_with(custom_suffix))

