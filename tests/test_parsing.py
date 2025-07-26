import unittest
from country_picker.utils import parse_country_names


class TestCountryParsing(unittest.TestCase):
    """Test cases for JSON parsing logic."""

    def test_parse_country_names_valid_data(self):
        """Test parsing valid country data."""
        test_data = [
            {"name": "United States", "code": "US"},
            {"name": "Canada", "code": "CA"},
            {"name": "Mexico", "code": "MX"}
        ]
        expected = ["United States", "Canada", "Mexico"]
        result = parse_country_names(test_data)
        self.assertEqual(result, expected)

    def test_parse_country_names_missing_name(self):
        """Test parsing data with missing name fields."""
        test_data = [
            {"name": "United States", "code": "US"},
            {"code": "CA"},  # Missing name
            {"name": "Mexico", "code": "MX"}
        ]
        expected = ["United States", "Mexico"]
        result = parse_country_names(test_data)
        self.assertEqual(result, expected)

    def test_parse_country_names_empty_data(self):
        """Test parsing empty data."""
        result = parse_country_names([])
        self.assertEqual(result, [])

    def test_parse_country_names_invalid_data(self):
        """Test parsing invalid data."""
        result = parse_country_names("invalid")
        self.assertEqual(result, [])

    def test_parse_country_names_none_data(self):
        """Test parsing None data."""
        result = parse_country_names(None)
        self.assertEqual(result, [])


if __name__ == "__main__":
    unittest.main()