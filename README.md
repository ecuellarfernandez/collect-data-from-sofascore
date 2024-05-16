# Football Data Analysis Project

This project uses Python to collect, clean, and analyze football match data. The data is obtained from the SofaScore API and stored in CSV files for further analysis.

## Files and Methods

### `collect_data_from_all_rounds_of_a_season.py`

This script collects data from all matches of a football season. It iterates over each round of the season, makes a GET request to the SofaScore API, and saves the data in a CSV file.

### `clean_round.py`

This script loads data from a CSV file, extracts the required values from each event, and creates a new DataFrame with these values. The extracted values include the team names, scores, and winner code. Each event is split into two rows, one for each team.

The `extract_values(event)` method is used to extract the required values from each event. It takes an event as input and returns two rows of data.

### `clean_season.py`

This script loads data from all CSV files in a folder, extracts the required values from each event, and creates a new DataFrame with these values. The extracted values include the team names, scores, winner code, match status, round, and season. Each event is split into two rows, one for each team.

The `remove_accents(input_str)` method is used to remove accents from a string.

The `extract_values(event)` method is used to extract the required values from each event. It takes an event as input and returns two rows of data.

## Usage

To use this project, first run `collect_data_from_all_rounds_of_a_season.py` to collect the match data. Then, run `clean_round.py` to clean the data for each round. Finally, run `clean_season.py` to clean the data for the entire season.