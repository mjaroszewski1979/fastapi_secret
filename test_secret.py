import unittest
import algo
from main import app


class TestAlgo(unittest.TestCase):
    def setUp(self):
        self.result_1 = algo.enc_algo('Password ,.;:!?-123', 222)
        self.result_2 = algo.dec_algo(algo.enc_algo('Password ,.;:!?-123', 222), 222)

# Testing for application existence
    def test_app_exists(self):
        self.assertFalse(app is None)

# Testing for correct output data types
    def test_enc_algo_type(self):
        self.assertIsInstance(self.result_1, str)

    def test_dec_algo_type(self):
        self.assertIsInstance(self.result_2, str)

# Testing for inconsistency in the data received from encryption process
    def test_enc_algo(self):
        self.assertNotEqual(algo.enc_algo('Password ,.;:!?-123', 222), algo.enc_algo('Password ,.;:!?-123', 222))

# Testing for various edge cases
    def test_algo(self):
        self.assertEqual('Password ,.;:!?-123', algo.dec_algo(algo.enc_algo('Password ,.;:!?-123', 222), 222))

    def test_algo(self):
        self.assertEqual('Password ,.;:!?-123', algo.dec_algo(algo.enc_algo('Password ,.;:!?-123', -222), -222))

    def test_algo(self):
        self.assertNotEqual('Password ,.;:!?-123', algo.dec_algo(algo.enc_algo('Password ,.;:!?-123', 111), 222))

    def test_algo(self):
        self.assertEqual(' ,.;:!?', algo.dec_algo(algo.enc_algo(' ,.;:!?', 222), 222))

    def test_algo(self):
        self.assertEqual(' ,.;:!?', algo.dec_algo(algo.enc_algo(' ,.;:!?', -222), -222))

    def test_algo(self):
        self.assertNotEqual(' ,.;:!?', algo.dec_algo(algo.enc_algo(' ,.;:!?', 111), 222))

    def test_algo(self):
        self.assertEqual('123456', algo.dec_algo(algo.enc_algo('123456', 222), 222))

    def test_algo(self):
        self.assertEqual('123456', algo.dec_algo(algo.enc_algo('123456', -222), -222))

    def test_algo(self):
        self.assertNotEqual('123456', algo.dec_algo(algo.enc_algo('123456', 111), 222))


if __name__ == '__main__':
    unittest.main()
