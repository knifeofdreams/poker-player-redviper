class Player:
    VERSION = "Such viper"

    def betRequest(self, game_state):
        if game_state['players'][game_state['in_action']]['hole_cards'][0]['rank'] == 'A' and game_state['players'][game_state['in_action']]['hole_cards'][1]['rank'] == 'A':
            return game_state['players'][game_state['in_action']]['stack']/6
        else:
            return 100

    def showdown(self, game_state):
        pass

