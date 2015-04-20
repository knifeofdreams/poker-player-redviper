import unittest
import json
from pprint import pprint

from player import Player

class PlayerTest(unittest.TestCase):
    def setUp(self):
        self.player = Player()
        self.game_state = {}

        with open('gamestate.json') as json_file:
            self.game_state = json.load(json_file)

    def test_bet_request_should_return_integer(self):
        self.assertIsInstance(self.player.betRequest(self.game_state), int)

    def test_bet_1000_when_ace_pair(self):
        with open('gamestate.json') as json_file:
            game_state = json.load(json_file)
        print game_state['players'][game_state['in_action']]['hole_cards'][0]['rank']
        self.assertEqual(self.player.betRequest(self.game_state), 1000)

if __name__ == '__main__':
    unittest.main()