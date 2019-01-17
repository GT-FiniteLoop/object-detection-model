import argparse
import sys
import unittest

sys.path.append('..')
from model import detect
from util import threshold

class TestWeatherConditions(unittest.TestCase):
    def test_firearm_indoor(self):
        score = detect("")
        self.assertTrue(score > threshold)

    def test_firearm_outdoor_clear(self):
        score = detect("")
        self.assertTrue(score > threshold)

    def test_firearm_outdoor_overcast(self):
        score = detect("")
        self.assertTrue(score > threshold)

    def test_firearm_outdoor_rain(self):
        score = detect("")
        self.assertTrue(score > threshold)

    def test_firearm_outdoor_fog(self):
        score = detect("")
        self.assertTrue(score > threshold)

    def test_firearm_outdoor_snow(self):
        score = detect("")
        self.assertTrue(score > threshold)


if __name__ == '__main__':
    # parser = argparse.ArgumentParser()
    # parser.add_argument('--threshold', default='75')
    # TestDistance.threshold = float(parser.parse_args().threshold)
    unittest.main()
