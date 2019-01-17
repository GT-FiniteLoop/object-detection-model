import argparse
import sys
import unittest

sys.path.append('..')
from model import detect
from util import threshold

class TestFirearmType(unittest.TestCase):
    def test_firearm_unpresent(self):
        score = detect("")
        self.assertTrue(score > threshold)

    def test_firearm_umbrella(self):
        score = detect("")
        self.assertTrue(score > threshold)

    def test_firearm_phone(self):
        score = detect("")
        self.assertTrue(score > threshold)

    def test_firearm_hand(self):
        score = detect("")
        self.assertTrue(score > threshold)

    def test_firearm_long(self):
        score = detect("")
        self.assertTrue(score > threshold)

    def test_firearm_toy(self):
        score = detect("")
        self.assertTrue(score > threshold)

    def test_firearm_water(self):
        score = detect("")
        self.assertTrue(score > threshold)

    def test_firearm_flare(self):
        score = detect("")
        self.assertTrue(score > threshold)


if __name__ == '__main__':
    # parser = argparse.ArgumentParser()
    # parser.add_argument('--threshold', default='75')
    # TestDistance.threshold = float(parser.parse_args().threshold)
    unittest.main()
