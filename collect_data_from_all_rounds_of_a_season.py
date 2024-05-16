import requests
import pandas as pd

# URL base
url_base = "https://www.sofascore.com/api/v1/unique-tournament/8/season/37223/events/round/"

# Itera sobre el rango de 1 a 39
for i in range(1, 39):
    # Cambia el último número de la URL
    url = url_base + str(i)

    # Haz una solicitud GET a la URL
    response = requests.get(url)

    # Obtiene los datos JSON
    data = response.json()

    # Convierte los datos JSON en un DataFrame
    df = pd.DataFrame(data)
    # Guarda el DataFrame en un archivo CSV
    #GUARDARlo en la carpeta /results_rounds/22_23/rounds
    df.to_csv(f"result_rounds/21_22/rounds/round_{i}.csv", index=False)