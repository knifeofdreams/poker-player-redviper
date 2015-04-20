import unittest

from player import Player

class PlayerTest(unittest.TestCase):
    def setUp(self):
        self.player = Player()

    def test_bet_request_should_return_integer(self):
        self.assertIsInstance(self.player.betRequest({}), int)

if __name__ == '__main__':
    unittest.main()