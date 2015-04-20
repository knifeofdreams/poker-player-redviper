import unittest
import json

from player import Player

class PlayerTest(unittest.TestCase):
    def setUp(self):
        self.player = Player()
        self.game_state = {}

        with open('APairGameState.json') as json_file:
            self.game_state = json.load(json_file)

    def test_bet_request_should_return_integer(self):
        self.assertIsInstance(self.player.betRequest(self.game_state), int)

    def test_bet_1800_when_ace_pair(self):
        with open('APairGameState.json') as json_file:
            game_state = json.load(json_file)
        self.assertEqual(self.player.betRequest(game_state), 1800)

    def test_bet_600_when_pair(self):
        with open('PairGameState.json') as json_file:
            game_state = json.load(json_file)
        self.assertEqual(self.player.betRequest(game_state), 600)

if __name__ == '__main__':
    unittest.main()