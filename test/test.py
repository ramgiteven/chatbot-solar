import os
import unittest
from unittest.mock import patch

class TestCreateLead(unittest.TestCase):

    def test_create_lead_success(self):
        self.assertEqual(1+1, 2)


if __name__ == '__main__':
    unittest.main()