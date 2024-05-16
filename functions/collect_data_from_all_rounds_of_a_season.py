import requests
import pandas as pd

def collect_data_from_all_rounds_of_a_season(url_base, csv_destination):
    print("Starting collect_data_from_all_rounds_of_a_season function...")

    # Iterates over the range of 1 to 39
    for i in range(1, 39):
        # Changes the last number of the URL
        url = url_base + str(i)

        print(f"Making request to: {url}...")

        # Makes a GET request to the URL
        response = requests.get(url)

        # Gets the JSON data
        data = response.json()

        # Converts the JSON data into a DataFrame
        df = pd.DataFrame(data)

        # Saves the DataFrame in a CSV file
        csv_file = f"{csv_destination}/round_{i}.csv"
        df.to_csv(csv_file, index=False)

        print(f"Data saved to: {csv_file}")

    print("collect_data_from_all_rounds_of_a_season function finished.")