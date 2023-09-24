from django.test import SimpleTestCase
from . import remove_dup


class ViewsTest(SimpleTestCase):

    def test_make_list_unique(self):
        "Test making a list unique"
        sample_items = [1, 1, 2, 3, 3, 4, 4, 5, 6]
        res = remove_dup.remove_duplicate(sample_items)
        self.assertEqual(res, [1, 2, 3, 4, 5, 6])
