# -*- coding: utf-8 -*-

from .context import binFile

import unittest

target_file = './tests/TestData/binFile_Test/binary.dat'

class BasicTestSuite(unittest.TestCase):
    """Basic test cases."""

    def setUp(self):
        contents = b'0123456789abcdef0123456789abcdef'
        with open(target_file, 'wb') as f:
            f.write(contents)

    def tearDown(self):
        contents = b'0123456789abcdef0123456789abcdef'
        with open(target_file, 'wb') as f:
            f.write(contents)

    def test_absolute_truth_and_meaning(self):
        assert True

    def test_read_binFile_from_start(self):
        contents = binFile.read_bytes_from_file(target_file, 0, 16)
        self.assertEqual(contents, b'0123456789abcdef')

        contents = binFile.read_bytes_from_file(target_file, 0, 32)
        self.assertEqual(contents, b'0123456789abcdef0123456789abcdef')
    
    def test_read_binFile_from_middle(self):
        contents = binFile.read_bytes_from_file(target_file, 3, 1)
        self.assertEqual(contents, b'3')

        contents = binFile.read_bytes_from_file(target_file, 8, 8)
        self.assertEqual(contents, b'89abcdef')

        contents = binFile.read_bytes_from_file(target_file, 16, 8)
        self.assertEqual(contents, b'01234567')

        contents = binFile.read_bytes_from_file(target_file, 16, 16)
        self.assertEqual(contents, b'0123456789abcdef')

    def test_write_binFile_from_start(self):
        binFile.write_bytes_to_file(target_file, 0, b'9876543210')
        contents = binFile.read_bytes_from_file(target_file, 0, 32)
        self.assertEqual(contents, b'9876543210abcdef0123456789abcdef')

    def test_write_binFile_in_middle(self):
        binFile.write_bytes_to_file(target_file, 10, b'fedcba')
        contents = binFile.read_bytes_from_file(target_file, 0, 32)
        self.assertEqual(contents, b'0123456789fedcba0123456789abcdef')

    def test_write_binFile_in_tail(self):
        binFile.write_bytes_to_file(target_file, 16, b'fedcba9876543210')
        contents = binFile.read_bytes_from_file(target_file, 0, 32)
        self.assertEqual(contents, b'0123456789abcdeffedcba9876543210')


if __name__ == '__main__':
    unittest.main()
