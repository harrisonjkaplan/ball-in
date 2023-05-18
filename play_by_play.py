# Query nba.live.endpoints for the score board of GameID 0022000180 = NYK vs BOS
# Simple PlayByPlay Loop demonstrating data usage
from nba_api.live.nba.endpoints import playbyplay
from nba_api.stats.static import players

class Team_Stats():
    def _init__(self,id):
        name = name
        turnovers = []
        offensive_rebounds = []
        defensive_rebounds = []

    
    def add_action(self,action):
        self.actions.append(action)


def contains_player(game_players,name):
    for player in game_players:
        if player.name == name:
            return True
    return False

def get_index_by_name(name, my_list):
    for index, item in enumerate(my_list):
        if item.name == name:
            return index
    return -1
turnovers = []
def get_play_stats():
    pbp = playbyplay.PlayByPlay('0042200301')
    print(type(pbp))
    line = "{action_number}: {period}:{clock} {player_id} ({action_type})"
    bos_stats = Team_Stats(1610612738)
    mia_stats = Team_Stats(1610612748)
    actions = pbp.get_dict()['game']['actions'] #plays are referred to in the live data as `actions`
    game_players = []
    print(len(actions))
    print(type(actions))


    for action in actions:
        if action['actionType'] == 'turnover' and action['teamId'] == 1610612738:
            bos_stats.turnovers.append({action['subType']})

    print(len(turnovers))
    print(turnovers)


            

get_play_stats()




# player business
        # print(action)
        # player_name = ''
        # player = players.find_player_by_id(action['personId'])
        # if player is not None:
        #     player_name = player['full_name']
            # if contains_player(game_players,player_name) == False:
            #     new_player = Player(player_name)
            #     game_players.append(new_player)
            
                
                # new_player.add_action(action['actionType'])
        # print(line.format(action_number=action['actionNumber'],period=action['period'],clock=action['clock'],action_type=action['actionType'],player_id=player_name))
