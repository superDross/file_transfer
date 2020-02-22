from django.test import TestCase
from django.urls import reverse

from file_transfer_tool.models import Files


class UploadTest(TestCase):
    fixtures = ["db.json"]

    def test_upload_file(self):
        with open("file_transfer_tool/tests/test.txt") as f:
            response = self.client.post(
                "/upload/",
                {
                    "name": "test_name",
                    "description": "big",
                    "password": "pass",
                    "file": f,
                },
            )
        file = Files.objects.filter(name="test_name")
        self.assertEqual(response.status_code, 200)
        self.assertTrue(file.exists())


class DownloadTest(TestCase):
    fixtures = ["db.json"]

    def test_download_file_with_incorrect_password(self):
        response = self.client.post(
            "/download/a730c99e8dc548249e2ce6649de31436/",
            {"password": "incorrect_password"},
        )
        self.assertEqual(response.status_code, 401)

    def test_download_with_correct_password(self):
        response = self.client.post(
            "/download/a730c99e8dc548249e2ce6649de31436/", {"password": "password"},
        )
        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            response.get("Content-Disposition"),
            "attachment; filename=temp.txt",
        )

    def test_invalid_id_in_url(self):
        response = self.client.get(
            "/download/not_an_valid_id", {"password": "password"}, follow=True
        )
        self.assertEqual(response.status_code, 404)
        self.assertTrue("File Does Not Exist" in response.content.decode("utf-8"))
