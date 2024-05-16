import requests
import pandas as pd

def collect_data_from_all_rounds_of_a_season(url_base, csv_destination):
    # Iterates over the range of 1 to 39
    for i in range(1, 39):
        # Changes the last number of the URL
        url = url_base + str(i)

        # Makes a GET request to the URL
        response = requests.get(url)

        # Gets the JSON data
        data = response.json()

        # Converts the JSON data into a DataFrame
        df = pd.DataFrame(data)

        # Saves the DataFrame in a CSV file
        df.to_csv(f"{csv_destination}/round_{i}.csv", index=False)