import json
import unittest
from unittest.mock import patch

from src.app import app
from src.exceptions import InvalidDateFormat
from tests.mocks import FakeResponse


class TestFlaskApp(unittest.TestCase):
    def setUp(self):
        self._app = app
        self._app.config.update({"TESTING": True})

    def test_home_page_should_return_expected_message(self):
        with self._app.test_client() as test_client:
            expected_response = FakeResponse(data=b"Welcome to Calendar App. Please visit url: 'hostname:port/date' to try it.", status_code=200)

            # Hitting home page
            actual_response = test_client.get("/")

            self.assertEqual(expected_response.status_code, actual_response.status_code)
            self.assertEqual(expected_response.data, actual_response.data)

    @patch("src.app.get_date_matrix")
    def test_date_page_should_return_expected_message_for_valid_date(self, stub_get_date_matrix):
        dummy_date = "2022-02-27"
        expected_date_matrix = b"[[30, 31, 1, 2, 3, 4, 5], [6, 7, 8, 9, 10, 11, 12], [13, 14, 15, 16, 17, 18, 19], [20, 21, 22, 23, 24, 25, 26], [27, 28, 1, 2, 3, 4, 5], [6, 7, 8, 9, 10, 11, 12]]"
        stub_get_date_matrix.get_date_matrix.return_value = json.loads(expected_date_matrix.decode())
        expected_response = FakeResponse(data=expected_date_matrix, status_code=200)

        with self._app.test_client() as test_client:
            # Hitting home page
            actual_response = test_client.get(f"/{dummy_date}")

            self.assertEqual(expected_response.status_code, actual_response.status_code)
            self.assertEqual(expected_response.data, actual_response.data)

    @patch("src.app.get_date_matrix")
    def test_date_page_should_return_400_for_invalid_date(self, stub_get_date_matrix):
        dummy_date = "2022-02-27"
        stub_get_date_matrix.get_date_matrix.side_effect = InvalidDateFormat("unittest-invalid-date")
        expected_response = FakeResponse(data="unittest-invalid-date", status_code=400)

        with self._app.test_client() as test_client:
            # Hitting home page
            actual_response = test_client.get(f"/{dummy_date}")

            self.assertEqual(expected_response.status_code, actual_response.status_code)
            self.assertEqual(expected_response.data, actual_response.data.decode())

    @patch("src.app.get_date_matrix")
    def test_date_page_should_return_500_for_unexpected_server_side_error(self, stub_get_date_matrix):
        dummy_date = "2022-02-27"
        stub_get_date_matrix.get_date_matrix.side_effect = Exception("unittest-server-side-exception")
        expected_response = FakeResponse(data="Server side issue", status_code=500)

        with self._app.test_client() as test_client:
            # Hitting home page
            actual_response = test_client.get(f"/{dummy_date}")

            self.assertEqual(expected_response.status_code, actual_response.status_code)
            self.assertEqual(expected_response.data, actual_response.data.decode())


if __name__ == "__main__":
    unittest.main()
