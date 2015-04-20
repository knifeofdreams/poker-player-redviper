class Player:
    VERSION = "Default Python folding player"

    def betRequest(self, game_state):
        if game_state['players'][game_state['in_action']]['hole_cards'][0]['rank'] == 'A' and game_state['players'][game_state['in_action']]['hole_cards'][1]['rank'] == 'A':
            return 1000
        else:
            return 100

    def showdown(self, game_state):
        pass

