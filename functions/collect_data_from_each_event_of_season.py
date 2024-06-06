import requests
import json
import pandas as pd
import time  # Import the time module

def get_match_data(event_id):
    print(f"Fetching data for event_id: {event_id}")
    url = f"https://www.sofascore.com/api/v1/event/{event_id}/statistics"
    response = requests.get(url)
    data = response.json()
    time.sleep(1)  # Add a delay of 1 second
    return data

def process_match_data(data):
    print("Processing match data...")
    match_stats = {}
    periods = ['ALL', '1ST', '2ND']
    if 'statistics' in data:
        for stat in data['statistics']:
            if stat.get('period') in periods and 'groups' in stat:
                for group in stat['groups']:
                    for item in group['statisticsItems']:
                        if item['key'] in ['expectedGoals', 'bigChanceCreated', 'totalShotsOnGoal', 'goalkeeperSaves', 'cornerKicks', 'fouls', 'passes', 'freeKicks', 'yellowCards', 'redCards', 'totalShotsInsideBox', 'totalShotsOutsideBox', 'bigChanceScored', 'touchesInOppBox', 'duelWonPercent', 'dispossessed', 'interceptionWon', 'ballRecovery', 'goalsPrevented']:
                            match_stats[stat.get('period').lower() + '_local_' + item['key']] = item['homeValue']
                            match_stats[stat.get('period').lower() + '_away_' + item['key']] = item['awayValue']
    else:
        print(f"Error: No 'statistics' in data for event_id {data.get('event_id', 'Unknown')}")
    return match_stats

# Read the CSV file and get the event_id
df = pd.read_csv('../results_rounds/23_24/cleaned_data.csv')
event_ids = df['event_id'].unique()

all_match_stats = {}

for event_id in event_ids:
    data = get_match_data(event_id)
    match_stats = process_match_data(data)
    all_match_stats[event_id] = match_stats

# Convert the dictionary into a DataFrame and write the DataFrame to a CSV file
df_stats = pd.DataFrame(all_match_stats).T
print("Saving DataFrame to CSV file...")
df_stats.to_csv('../results_rounds/23_24/match_stats_0.csv')
print("Task completed.")