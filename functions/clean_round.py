import pandas as pd
pd.set_option('display.max_columns', None)
import ast

# Carga el archivo CSV en un DataFrame
df = pd.read_csv('../results_rounds/23_24/rounds/round_1.csv', converters={'events': ast.literal_eval})

# Define una función para extraer los valores requeridos
def extract_values(event):
    home_team = event['homeTeam']['name'].replace(' ', '')
    away_team = event['awayTeam']['name'].replace(' ', '')
    home_score = event['homeScore']['current']
    away_score = event['awayScore']['current']
    winner_code = event['winnerCode']

    # Crea dos filas para cada fila original
    row1 = {
        'match': f"{home_team}_{away_team}",
        'team': home_team,
        'opponent': away_team,
        'team_score': home_score,
        'opponent_score': away_score,
        'result': 'win' if winner_code == 1 else 'loss' if winner_code == 2 else 'draw'
    }
    row2 = {
        'match': f"{away_team}_{home_team}",
        'team': away_team,
        'opponent': home_team,
        'team_score': away_score,
        'opponent_score': home_score,
        'result': 'win' if winner_code == 2 else 'loss' if winner_code == 1 else 'draw'
    }

    return [row1, row2]

# Aplica la función a la columna 'events' y crea un nuevo DataFrame
new_rows = [row for event in df['events'] for row in extract_values(event)]
new_df = pd.DataFrame(new_rows)

print(new_df)
#guardarlo en un nuevo csv
#new_df.to_csv(f"datos_limpios_1.csv", index=False)
#display all columns


