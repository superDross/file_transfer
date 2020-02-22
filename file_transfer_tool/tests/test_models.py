from django.test import TestCase

from file_transfer_tool.models import Files


class FilesTest(TestCase):
    fixtures = ["db.json"]

    def setUp(self):
        self.file = Files.objects.first()

    def test_str_method(self):
        self.assertEqual(self.file.name, "test")
