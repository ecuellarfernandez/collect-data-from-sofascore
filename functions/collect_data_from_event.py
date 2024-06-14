import requests
import json

def get_match_data(event_id):
    url = f"https://www.sofascore.com/api/v1/event/{event_id}/statistics"
    response = requests.get(url)
    data = response.json()
    return data

def process_match_data(data):
    match_stats = {}
    if 'statistics' in data:
        for stat in data['statistics']:
            if stat.get('period') == 'ALL' and 'groups' in stat:
                for group in stat['groups']:
                    for item in group['statisticsItems']:
                        if item['key'] in ['expectedGoals', 'bigChanceCreated', 'totalShotsOnGoal', 'goalkeeperSaves', 'cornerKicks', 'fouls', 'passes', 'freeKicks', 'yellowCards', 'redCards', 'totalShotsInsideBox', 'totalShotsOutsideBox', 'bigChanceScored', 'touchesInOppBox', 'duelWonPercent', 'dispossessed', 'interceptionWon', 'ballRecovery', 'goalsPrevented']:
                            match_stats[item['key']] = {'local': item['homeValue'], 'away': item['awayValue']}
    else:
        print(f"Error: No 'statistics' in data for event_id {data.get('event_id', 'Unknown')}")
    return match_stats
event_ids = [11368614]
all_match_stats = {}

for event_id in event_ids:
    data = get_match_data(event_id)
    match_stats = process_match_data(data)
    all_match_stats[event_id] = match_stats

print(json.dumps(all_match_stats, indent=4))