import argparse
import sys
import unittest

sys.path.append('..')
from model import detect
from util import threshold

class TestDistance(unittest.TestCase):
    def test_firearm_distance_close(self):
        score = detect("")
        self.assertTrue(score > threshold)

    def test_firearm_distance_10_ft(self):
        score = detect("")
        self.assertTrue(score > threshold)

    def test_firearm_distance_20_ft(self):
        score = detect("")
        self.assertTrue(score > threshold)

    def test_firearm_distance_30_ft(self):
        score = detect("")
        self.assertTrue(score > threshold)


if __name__ == '__main__':
    # parser = argparse.ArgumentParser()
    # parser.add_argument('--threshold', default='75')
    # TestDistance.threshold = float(parser.parse_args().threshold)
    unittest.main()
