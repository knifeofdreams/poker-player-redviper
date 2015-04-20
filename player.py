class Player:
    VERSION = "Clever Viper"

    def betRequest(self, game_state):

        ACE_PAIR = game_state['players'][game_state['in_action']]['hole_cards'][0]['rank'] == 'A' and \
                   game_state['players'][game_state['in_action']]['hole_cards'][1]['rank'] == 'A'


        PAIR = game_state['players'][game_state['in_action']]['hole_cards'][0]['rank'] == \
                   game_state['players'][game_state['in_action']]['hole_cards'][1]['rank']

        ONE_HIGH_CARD = game_state['players'][game_state['in_action']]['hole_cards'][0]['rank'] == 'A' or \
                        game_state['players'][game_state['in_action']]['hole_cards'][0]['rank'] == 'Q' or \
                        game_state['players'][game_state['in_action']]['hole_cards'][0]['rank'] == 'K' or \
                        game_state['players'][game_state['in_action']]['hole_cards'][0]['rank'] == 'J'

        OTHER_HIGH_CARD = game_state['players'][game_state['in_action']]['hole_cards'][0]['rank'] == 'A' or \
                          game_state['players'][game_state['in_action']]['hole_cards'][0]['rank'] == 'Q' or \
                          game_state['players'][game_state['in_action']]['hole_cards'][0]['rank'] == 'K' or \
                          game_state['players'][game_state['in_action']]['hole_cards'][0]['rank'] == 'J'


        if ACE_PAIR:
            return game_state['players'][game_state['in_action']]['stack']
        elif PAIR:
            return game_state['players'][game_state['in_action']]['stack']/3
        elif ONE_HIGH_CARD or OTHER_HIGH_CARD:
            return game_state['players'][game_state['in_action']]['stack']/6
        else:
            return 100

    def showdown(self, game_state):
        pass

