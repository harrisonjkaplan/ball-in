# Query nba.live.endpoints for the score board of GameID 0022000180 = NYK vs BOS
# Simple PlayByPlay Loop demonstrating data usage
from nba_api.live.nba.endpoints import playbyplay
from nba_api.stats.static import players

pbp = playbyplay.PlayByPlay('0042200217')
line = "{action_number}: {period}:{clock} {player_id} ({action_type})"
actions = pbp.get_dict()['game']['actions'] #plays are referred to in the live data as `actions`
print(len(actions))
for action in actions:
    player_name = ''
    player = players.find_player_by_id(action['personId'])
    if player is not None:
        player_name = player['full_name']
    print(line.format(action_number=action['actionNumber'],period=action['period'],clock=action['clock'],action_type=action['actionType'],player_id=player_name))
