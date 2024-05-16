import pandas as pd
import os
import ast
import warnings
from unidecode import unidecode

def clean_season(folder_path):
    warnings.filterwarnings(action='ignore', category=FutureWarning)
    pd.set_option('display.max_columns', None)

    def remove_accents(input_str):
        return unidecode(input_str)

    all_data = pd.DataFrame()

    for filename in os.listdir(folder_path):
        if filename.endswith('.csv'):
            ronda = filename.replace('.csv', '').split('_')[1]
            temporada = os.path.basename(os.path.dirname(folder_path))

            df = pd.read_csv(os.path.join(folder_path, filename), converters={'events': ast.literal_eval})

            def extract_values(event):
                home_team = remove_accents(event['homeTeam']['name'].replace(' ', ''))
                away_team = remove_accents(event['awayTeam']['name'].replace(' ', ''))

                home_score = event['homeScore']['current'] if 'current' in event['homeScore'] else None
                away_score = event['awayScore']['current'] if 'current' in event['awayScore'] else None

                winner_code = event['winnerCode'] if 'winnerCode' in event else None

                status = event['status']['type']

                row1 = {
                    'match': f"{home_team}_{away_team}",
                    'team': home_team,
                    'opponent': away_team,
                    'team_score': home_score,
                    'opponent_score': away_score,
                    'result': 'win' if winner_code == 1 else 'loss' if winner_code == 2 else 'draw' if winner_code is not None else None,
                    'status': status,
                    'round': ronda,
                    'season': temporada
                }
                row2 = {
                    'match': f"{away_team}_{home_team}",
                    'team': away_team,
                    'opponent': home_team,
                    'team_score': away_score,
                    'opponent_score': home_score,
                    'result': 'win' if winner_code == 2 else 'loss' if winner_code == 1 else 'draw' if winner_code is not None else None,
                    'status': status,
                    'round': ronda,
                    'season': temporada
                }

                return [row1, row2]

            new_rows = [row for event in df['events'] for row in extract_values(event)]
            new_df = pd.DataFrame(new_rows)

            all_data = pd.concat([all_data, new_df])

    all_data.sort_values(by=['season', 'round'], inplace=True)

    all_data.reset_index(drop=True, inplace=True)

    # Save the DataFrame to a CSV file in the parent directory of the given folder path
    all_data.to_csv(os.path.join(os.path.dirname(folder_path), 'cleaned_data.csv'), index=False)

    return all_data