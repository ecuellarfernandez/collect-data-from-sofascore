import pandas as pd

# Lee los archivos CSV
df1 = pd.read_csv('../results_rounds/19_20/match_stats_0.csv')
df2 = pd.read_csv('../results_rounds/19_20/cleaned_data.csv')

# Crea una función para invertir los datos si el 'event_id' se repite
def invert_data(df):
    # Encuentra los 'event_id' que se repiten
    duplicate_ids = df[df.duplicated('event_id')]['event_id']

    # Invierte los datos para los 'event_id' que se repiten
    for id in duplicate_ids:
        df.loc[df['event_id'] == id, ['local', 'visitante']] = df.loc[df['event_id'] == id, ['visitante', 'local']].values

    return df

# Aplica la función al DataFrame
df1 = invert_data(df1)

# Une los DataFrames
merged_df = pd.merge(df1, df2, left_on='event_id', right_on='event_id', how='inner')

# Guarda el DataFrame unido en un nuevo archivo CSV
merged_df.to_csv('../results_rounds/19_20/merged_data.csv', index=False)