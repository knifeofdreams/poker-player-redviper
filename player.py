class Player:
    VERSION = "YOLO VIPER"

    def betRequest(self, game_state):

        ONE_HIGH_CARD = game_state['players'][game_state['in_action']]['hole_cards'][0]['rank'] == 'A' or \
                        game_state['players'][game_state['in_action']]['hole_cards'][0]['rank'] == 'Q' or \
                        game_state['players'][game_state['in_action']]['hole_cards'][0]['rank'] == 'K' or \
                        game_state['players'][game_state['in_action']]['hole_cards'][0]['rank'] == 'J'

        OTHER_HIGH_CARD = game_state['players'][game_state['in_action']]['hole_cards'][0]['rank'] == 'A' or \
                          game_state['players'][game_state['in_action']]['hole_cards'][0]['rank'] == 'Q' or \
                          game_state['players'][game_state['in_action']]['hole_cards'][0]['rank'] == 'K' or \
                          game_state['players'][game_state['in_action']]['hole_cards'][0]['rank'] == 'J'

        ACE_PAIR = game_state['players'][game_state['in_action']]['hole_cards'][0]['rank'] == 'A' and \
                   game_state['players'][game_state['in_action']]['hole_cards'][1]['rank'] == 'A'
        if ACE_PAIR:
            return game_state['players'][game_state['in_action']]['stack']
        elif ONE_HIGH_CARD:
            return game_state['players'][game_state['in_action']]['stack']/6
        else:
            return 100

    def showdown(self, game_state):
        pass

