import pandas as pd
import os
import ast
import warnings
from unidecode import unidecode
warnings.filterwarnings(action='ignore', category=FutureWarning)
pd.set_option('display.max_columns', None)

# Define una función para eliminar los acentos
def remove_accents(input_str):
    return unidecode(input_str)

# Define la ruta de la carpeta
folder_path = 'results_rounds/23_24/rounds'

# Crea un DataFrame vacío para almacenar todos los datos
all_data = pd.DataFrame()

# Itera sobre cada archivo en la carpeta
for filename in os.listdir(folder_path):
    if filename.endswith('.csv'):
        # Extrae la ronda y la temporada del nombre del archivo
        ronda = filename.replace('.csv', '').split('_')[1]
        temporada = os.path.basename(os.path.dirname(folder_path))

        # Carga el archivo CSV en un DataFrame
        df = pd.read_csv(os.path.join(folder_path, filename), converters={'events': ast.literal_eval})

        # Define una función para extraer los valores requeridos
        def extract_values(event):
            home_team = remove_accents(event['homeTeam']['name'].replace(' ', ''))
            away_team = remove_accents(event['awayTeam']['name'].replace(' ', ''))

            # Verifica si 'current' está en los diccionarios antes de acceder a él
            home_score = event['homeScore']['current'] if 'current' in event['homeScore'] else None
            away_score = event['awayScore']['current'] if 'current' in event['awayScore'] else None

            # Verifica si 'winnerCode' está en el diccionario antes de acceder a él
            winner_code = event['winnerCode'] if 'winnerCode' in event else None

            # Verifica el estado del partido
            status = event['status']['type']

            # Crea dos filas para cada fila original
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

        # Aplica la función a la columna 'events' y crea un nuevo DataFrame
        new_rows = [row for event in df['events'] for row in extract_values(event)]
        new_df = pd.DataFrame(new_rows)

        # Agrega el nuevo DataFrame al DataFrame principal
        all_data = pd.concat([all_data, new_df])

# Ordena el DataFrame por 'temporada' y luego por 'ronda'
all_data.sort_values(by=['season', 'round'], inplace=True)

# Resetea el índice del DataFrame
all_data.reset_index(drop=True, inplace=True)

# Muestra el DataFrame principal
print(all_data.tail(20))

# Guardarlo en un excel
# all_data.to_csv(f"datos_limpios_23_24_a.csv", index=False)